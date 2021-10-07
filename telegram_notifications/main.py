#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import os
import time

from threading import Thread

# pip install python-telegram-bot
from telegram import Update, Bot, ParseMode
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters, CallbackContext, Defaults

import config
import db

from common import get_logger, log_func, reply_error


DATA = {
    'BOT': None,
    'IS_WORKING': True,
}

MESS_MAX_LENGTH = 4096

log = get_logger(__file__)


def sending_notifications():
    while True:
        bot: Bot = DATA['BOT']
        if not bot or not config.CHAT_ID:
            continue

        try:
            for notify in db.Notification.get_unsent():
                # Пауза, если IS_WORKING = False
                while not DATA['IS_WORKING']:
                    time.sleep(0.001)
                    continue

                text = notify.get_html()
                for n in range(0, len(text), MESS_MAX_LENGTH):
                    mess = text[n: n + MESS_MAX_LENGTH]
                    bot.send_message(config.CHAT_ID, mess, parse_mode=ParseMode.HTML)
                notify.set_as_send()

                time.sleep(1)

        except Exception as e:
            log.exception('')

            if config.CHAT_ID:
                text = f'⚠ При отправке уведомления возникла ошибка: {e}'
                bot.send_message(config.CHAT_ID, text)
                time.sleep(60)

        finally:
            time.sleep(1)


@log_func(log)
def on_start(update: Update, context: CallbackContext):
    if not config.CHAT_ID:
        update.message.reply_text('Введите что-нибудь для получения chat_id')


@log_func(log)
def on_request(update: Update, context: CallbackContext):
    message = update.effective_message

    if not config.CHAT_ID:
        text = f'CHAT_ID: {update.effective_chat.id}'
    else:
        command = message.text.lower()
        if command == 'start':
            DATA['IS_WORKING'] = True
        elif command == 'stop':
            DATA['IS_WORKING'] = False

        is_working = DATA['IS_WORKING']
        text = (
            f'Поддерживаемые комманды: <b>start</b>, <b>stop</b>\n'
            f'Рассылка уведомлений: <b>' + ('запущена' if is_working else 'остановлена') + '</b>'
        )

    message.reply_html(text)


def on_error(update: Update, context: CallbackContext):
    reply_error(log, update, context)


def main():
    cpu_count = os.cpu_count()
    workers = cpu_count
    log.debug('System: CPU_COUNT=%s, WORKERS=%s', cpu_count, workers)
    log.debug('CHAT_ID=%s', config.CHAT_ID)

    log.debug('Start')

    updater = Updater(
        config.TOKEN,
        workers=workers,
        defaults=Defaults(run_async=True),
    )
    DATA['BOT'] = updater.bot

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', on_start))
    dp.add_handler(MessageHandler(Filters.text, on_request))

    dp.add_error_handler(on_error)

    updater.start_polling()
    updater.idle()

    log.debug('Finish')


if __name__ == '__main__':
    Thread(target=sending_notifications).start()

    while True:
        try:
            main()
        except:
            log.exception('')

            timeout = 15
            log.info(f'Restarting the bot after {timeout} seconds')
            time.sleep(timeout)
