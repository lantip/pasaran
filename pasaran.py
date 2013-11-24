#!/usr/bin/env python
from datetime import datetime, timedelta

datenow     = datetime.now()
datebase    = datetime.strptime('1 1 1800', '%d %m %Y')
tomorrow    = datenow + timedelta(days=1)

# array to get the pasaran
pasaran     = ['Pon', 'Wage', 'Kliwon', 'Legi', 'Pahing']
# array to get the date name in javanese
dino        = ['Minggu', 'Senen', 'Seloso', 'Rebo', 'Kemis', 'Jemuwah', 'Septu']

# find the difference between now and base date, in days
diff        = datenow - datebase
diffdays    = diff.days

# find the modulo by 5

modulo      = diffdays % 5

# find out wether now is day or night
dn          = datenow.strftime("%p")
hn          = int(datenow.strftime("%I"))

if dn == "PM" and hn > 5:
    diff        = tomorrow - datebase
    diffdays    = diff.days
    modulo      = diffdays % 5
    print "Saiki malem " + dino[int(tomorrow.strftime("%w"))]+" "+pasaran[modulo]
else:
    print "Saiki dino " + dino[int(datenow.strftime("%w"))]+" "+ pasaran[modulo]
