#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# SOURCE: https://github.com/boppreh/keyboard/blob/master/examples/pressed_keys.py


"""
Prints the scan code of all currently pressed keys.
Updates on every keyboard event.
"""

import keyboard


def print_pressed_keys(e):
    line = ', '.join(str(code) for code in keyboard._pressed_events)
    # '\r' and end='' overwrites the previous line.
    # ' ' * 40 prints 40 spaces at the end to ensure the previous line is cleared.
    print('\r' + line + ' ' * 40, end='')


keyboard.hook(print_pressed_keys)
keyboard.wait()
