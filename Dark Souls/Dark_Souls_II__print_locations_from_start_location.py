#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from common import get_links_location


# NOTE: Способ поиска локаций, начиная с начальной и через переходы локаций искать другие сработал, однако
# часть локаций потерялись -- не всегда на одной странице локации указывает переход на следующую, но это
# может быть в обратную сторону
# Поэтому, для большей надежности лучше использовать скрипт Dark_Souls_II__print_locations.py

def print_transitions(url: str, title: str, visited_locations: set, links: set, log=True):
    title = title.strip().title()
    if title in visited_locations:
        return

    log and print(title, url)
    visited_locations.add(title)

    locations = get_links_location(url)
    if not locations:
        return locations

    if log:
        # Сначала напечатаем все связанные локации
        for x in locations:
            print('    {} -> {}'.format(x.title, x.url))

        print()

    # Поищем у этих локаций связанные с ними локации
    for x in locations:
        # Проверяем что локации с обратной связью не занесены
        if (x.title, title) not in links:
            links.add((title, x.title))

        print_transitions(x.url, x.title, visited_locations, links, log)


if __name__ == '__main__':
    visited_locations = set()
    links = set()

    url_start_location = 'http://ru.darksouls.wikia.com/wiki/Междумирье'
    print_transitions(url_start_location, 'Междумирье', visited_locations, links)

    print()
    print(len(visited_locations), sorted(visited_locations))
    print(len(links), sorted(links))
