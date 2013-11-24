#!/usr/bin/env python
from datetime import datetime

datenow     = datetime.today()
datebase    = datetime.strptime('1 1 1800', '%d %m %Y')

#array to get the pasaran
pasaran     = ['Pon', 'Wage', 'Kliwon', 'Legi', 'Pahing']
#array to get the date name in javanese
dino        = ['Minggu', 'Senen', 'Seloso', 'Rebo', 'Kemis', 'Jemuwah', 'Septu']

# find the difference between now and base date, in days
diff        = datenow - datebase
diffdays    = diff.days

#find the modulo by 5

modulo      = diffdays % 5


print "Saiki dino " + dino[int(datenow.strftime("%w"))]+" "+ pasaran[modulo]
