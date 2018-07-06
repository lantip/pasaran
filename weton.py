#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ﷽
from datetime import datetime, timedelta, date
import sys, time, argparse
import collections
import io, os
from strftime import strftime

parser = argparse.ArgumentParser(description='Mencari Weton, Geblak dan Pasaran')
parser.add_argument('-w','--weton', help='Masukkan tanggal untuk mencari weton. \
    format tanggal dd-mm-yyyy')
parser.add_argument('-g','--geblak',help='Masukkan tanggal meninggal \
    untuk mencari 7 dino, 40 dino, dan seterusnya. Format tanggal dd-mm-yyyy')
parser.add_argument('-p','--pasaran',help='Masukkan hari dan pasaran \
    untuk mencari tanggal masehi untuk kombinasi itu. Format "senin wage"')
parser.add_argument('-pw','--pawukon',help='Masukkan tanggal masehi untuk mencari pawukon. \
    Format tanggal dd-mm-yyyy')

args = parser.parse_args()

# constant variable for coloring output
TXT_WHITE = "\033[1;37m"
TXT_GRAY = "\033[0;37m"
TXT_CYAN = "\033[0;36m"
TXT_PURPLE = "\033[0;35m"
TXT_BLUE = "\033[0;34m"
TXT_YELLOW = "\033[0;33m"
TXT_BOLD_GREEN = "\033[1;32m"
TXT_BOLD_RED = "\033[0;31m"
TXT_DEFAULT = "\033[0m"
TXT_BOLD_DEFAULT = "\033[1;39m"

# coba generate ascii untuk wuku
def generate_ascii(url, imgname):
    from asciisciit.asciiart import AsciiImage
    from PIL import Image
    if 'http' in url:
        import requests
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
            images = Image.open(io.BytesIO(r.content)) 
            img = AsciiImage(images, 0.1, True)
            print(img)
    else:
        images = Image.open(url) 
        img = AsciiImage(images, 0.1, True)
        print(img)


# formula untuk mencari pasaran
def pasaran_formula(dateinput):
    datebase    = datetime.strptime('1 1 1800', '%d %m %Y')

    # find the difference between now and base date, in days
    if dateinput > datebase:
        diff        = dateinput - datebase
    else:
        diff    = datebase - dateinput
    diffdays    = diff.days

    # find the modulo by 5
    modulo      = diffdays % 5
    return modulo

# formula untuk mencari weekday
def WeekFinder(weekday, pasar, year):
    WEEK    = {'senin':0,'selasa':1,'rabu':2,'kamis':3,'jumat':4,'sabtu':5,'minggu':6}
    MONTH   = {'januari':1,'februari':2,'maret':3,'april':4,'mei':5,'juni':6,\
    'juli':7,'agustus':8,'september':9,'oktober':10,'november':11,'desember':12}
    PASARAN = {'pon':0, 'wage':1, 'kliwon':2, 'legi':3, 'pahing':4}

    year    = int(year)
    day     = WEEK[weekday]
    month   = MONTH['januari']
    dt      = date(year,int(month),1)
    dow_lst = []
    while dt.weekday() != day:
        dt = dt + timedelta(days=1)
    lst_month = MONTH.values()
    #lst_month.sort()
    for mont in lst_month:
        while dt.month == mont:
            modulo = pasaran_formula(datetime.combine(dt,datetime.min.time()))
            if modulo == PASARAN[pasar]:
                dow_lst.append(dt)
            dt = dt + timedelta(days=7)
    return dow_lst

# array to get the pasaran
pasaran     = ('Pon', 'Wage', 'Kliwon', 'Legi', 'Pahing')
# array to get the date name in javanese
dino        = ('Minggu', 'Senen', 'Seloso', 'Rebo', 'Kemis', 'Jemuwah', 'Septu')


if args.weton:
    dateinput   = datetime.strptime(args.weton, '%d-%m-%Y')
    modulo      = pasaran_formula(dateinput)
    print (TXT_YELLOW + ("Tanggal %s iku nagadinane %s %s" % \
        (args.weton, dino[int(strftime(dateinput,"%w"))], pasaran[modulo]) ))
    print (TXT_DEFAULT)

if args.geblak:
    GEBLAKS = { '1. Geblake':0, '2. Telung dinane':3, '3. Pitung dinane':7,
                '4. Patang puluh dinane': 40, '5. Nyatus dinane': 100,
                '6. Pendhak I dinane': 354, '7. Pendhak II dinane': 708,
                '8. Nyewu dinane': 1000 }
    od = collections.OrderedDict(sorted(GEBLAKS.items()))
    dateinput   = datetime.strptime(args.geblak, '%d-%m-%Y')

    for k,v in od.items():
        date_pasar = dateinput + timedelta(days=int(v))
        modulo     = pasaran_formula(date_pasar)
        print (TXT_YELLOW + (str(k)+" jenat: %s, %s %s" % \
            (strftime(date_pasar, '%d-%m-%Y'), dino[int(strftime(date_pasar, "%w"))], pasaran[modulo])))
        print (TXT_DEFAULT)

if args.pasaran:
    var         = args.pasaran.split()
    year        = input('Mencari pasaran di Tahun: '+'\n')
    listdays    = WeekFinder(var[0].lower(), var[1].lower(), year)
    for key,day in enumerate(listdays):
        print (TXT_YELLOW+var[0]+" "+var[1]+TXT_DEFAULT+" ("+str(key)+") :"+strftime(day,"%d-%m-%Y"))

if args.pawukon:
    dateinput   = datetime.strptime(args.pawukon, '%d-%m-%Y')
    datebase    = datetime.strptime('21 5 2000', '%d %m %Y')
    rentang     = dateinput - datebase
    rentang     = (rentang.days)
    #base_a      = (rentang % 210) + 210
    wk_cek      = rentang % 210
    nm_wuku     = int(wk_cek/7)
    modulo      = pasaran_formula(dateinput)
    wuku_list = ["Sinto / Sinta","Landep","Wukir","Kurantil","Tolu","Gumbrek / Gumbreg","Warigalit / Wariga Alit","Warigagung / Wariga Agung","Julungwangi / Julangwangi","Sungsang","Galungan","Kuningan","Langkir","Mondisijo / Mandasiya","Julungpujut","Pahang","Kuruwekut / Kuru Welut","Marakeh","Tambir","Medangkungan","Maktal","Waye","Menahil / Manahil","Prangbakat","Bolo / Bala","Wugu","Wayang","Kulawu","Dukut","Watagunung / Watu Gunung"]
    print(dateinput.strftime('%d %B %Y')+' iku dino '+dino[int(strftime(dateinput, "%w"))]+' '+pasaran[modulo]+', wuku: '+wuku_list[nm_wuku])
    script_dir = os.path.dirname(__file__)
    generate_ascii(os.path.join(script_dir,'images/'+str(nm_wuku)+'.jpg'), wuku_list[nm_wuku])
    

if not args.weton and not args.geblak and not args.pasaran and not args.pawukon:
    print (parser.print_help())





