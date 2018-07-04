#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ﷽
from datetime import datetime, timedelta
import time
from strftime import strftime


# get the timezone. i prefer using this approach because it's more understandable :p
offset      = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone
tz          = offset / 60 / 60 * -1

dtz         = 7 - int(tz)
datenow     = datetime.now() + timedelta(hours=dtz)
datebase    = datetime.strptime('1 1 1800', '%d %m %Y')
tomorrow    = datenow + timedelta(days=1) + timedelta(hours=dtz)

# array to get the pasaran
pasaran     = ('Pon', 'Wage', 'Kliwon', 'Legi', 'Pahing')
# array to get the date name in javanese
dino        = ('Minggu', 'Senen', 'Seloso', 'Rebo', 'Kemis', 'Jemuwah', 'Septu')

# find the difference between now and base date, in days
if datenow > datebase:
    diff        = datenow - datebase
else:
    diff        = datebase - datenow
diffdays    = diff.days

# find the modulo by 5

modulo      = diffdays % 5

# find out wether now is day or night
dn          = strftime(datenow,"%p")
hn          = int(strftime(datenow,"%I"))


if dn == "PM" and hn > 5 and hn != 12:
    rtnow       = dino[int(strftime(datenow,"%w"))] + " " + pasaran[modulo]
    diff        = tomorrow - datebase
    diffdays    = diff.days
    modulo      = diffdays % 5
    print ("Saiki dino "+ rtnow + ", malem " + dino[int(strftime(tomorrow,"%w"))]+" "+pasaran[modulo])
else:
    print ("Saiki dino " + dino[int(strftime(datenow,"%w"))]+" "+ pasaran[modulo])
