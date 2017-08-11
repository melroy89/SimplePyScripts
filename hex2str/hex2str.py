#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


def hex2str(hex_string):
    char_list = list()

    for i in range(0, len(hex_string), 2):
        hex2 = hex_string[i] + hex_string[i + 1]
        char = chr(int(hex2, 16))
        char_list.append(char)

    return ''.join(char_list)


if __name__ == '__main__':
    hex_text = "504F53542068747470733A"
    text = hex2str(hex_text)
    print('"{}"'.format(text))
