#!/usr/bin/env python
from datetime import datetime, timedelta
import time


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
diff        = datenow - datebase
diffdays    = diff.days

# find the modulo by 5

modulo      = diffdays % 5

# find out wether now is day or night
dn          = datenow.strftime("%p")
hn          = int(datenow.strftime("%I"))


if dn == "PM" and hn > 5:
    rtnow       = dino[int(datenow.strftime("%w"))] + " " + pasaran[modulo]
    diff        = tomorrow - datebase
    diffdays    = diff.days
    modulo      = diffdays % 5
    print "Saiki dino "+ rtnow + ", malem " + dino[int(tomorrow.strftime("%w"))]+" "+pasaran[modulo]
else:
    print "Saiki dino " + dino[int(datenow.strftime("%w"))]+" "+ pasaran[modulo]
