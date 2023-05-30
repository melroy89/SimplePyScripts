#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


from datetime import datetime
import pylab


price_by_date = {
    156802: "2017-04-30",
    147719: "2017-04-02",
    120172: "2017-01-27",
    123787: "2017-02-01",
    127890: "2017-02-11",
    131699: "2017-02-16",
    146452: "2017-03-27",
    148507: "2017-04-09",
    144858: "2017-03-18",
    144209: "2017-03-16",
    126114: "2017-02-06",
    102947: "2017-01-16",
    154404: "2017-04-22",
    141733: "2017-03-11",
    123249: "2017-01-29",
    148008: "2017-04-07",
    112297: "2017-01-19",
    120371: "2017-01-28",
    119923: "2017-01-25",
    127541: "2017-02-10",
    127163: "2017-02-07",
    142911: "2017-03-14",
    151106: "2017-04-10",
    147020: "2017-03-29",
    123598: "2017-01-30",
    136784: "2017-03-05",
    134737: "2017-02-21",
    135507: "2017-02-19",
    135636: "2017-02-20",
    136535: "2017-02-27",
    123866: "2017-02-04",
    143710: "2017-03-15",
    142562: "2017-03-13",
    138833: "2017-03-10",
    153705: "2017-04-20",
    137834: "2017-03-06",
    116076: "2017-01-22",
    90386: "2017-01-15",
    128239: "2017-02-14",
    145136: "2017-03-20",
    146033: "2017-03-22",
    124115: "2017-02-05",
    135158: "2017-02-17",
    145784: "2017-03-21",
    145535: "2017-03-19",
}

# Данные для построения графика
x = list(sorted(price_by_date.keys()))

get_date = lambda date_str: datetime.strptime(date_str, "%Y-%m-%d")
y = list(get_date(price_by_date[key]) for key in sorted(price_by_date.keys()))

pylab.plot(x, y)

pylab.xlabel("Price")
pylab.ylabel("Date")
pylab.grid()
pylab.show()
