#!/usr/bin/env python
from datetime import datetime

datenow     = datetime.today()
datebase    = datetime.strptime('1 1 1800', '%d %m %Y')

pasaran     = ['Pon', 'Wage', 'Kliwon', 'Legi', 'Pahing']

# find the difference between now and base date, in days
diff        = datenow - datebase
diffdays    = diff.days

#find the modulo by 5

modulo      = diffdays % 5

print "Today is " + datenow.strftime("%A")+" "+ pasaran[modulo]
