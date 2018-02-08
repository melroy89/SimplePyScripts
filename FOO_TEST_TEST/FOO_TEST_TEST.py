#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'ipetrash'


#
# import requests
# rs1 = requests.get('http://www.erkc-info.ru/index.php/counters/general-information/water')
# open('rs1.html', 'wb').write(rs1.content)
#
# rs2 = requests.get('http://www.erkc-info.ru/index.php/2011-07-13-08-14-16')
# open('rs2.html', 'wb').write(rs2.content)
#
# quit()

headers = {
    "SOAPAction": 'REQUEST',
    # "Accept": "binary/octet-stream, text/xml",
}
data = open('example_rq.xml', 'rb').read()
url = 'http://smev-mvf.test.gosuslugi.ru:7777/gateway/services/SID0003663/wsdl'

import requests
rs = requests.post(url, data=data, headers=headers)
print(rs)

open('example_rs.xml', 'wb').write(rs.content)

from bs4 import BeautifulSoup
root = BeautifulSoup(rs.content, 'html.parser')
print(root.prettify())
