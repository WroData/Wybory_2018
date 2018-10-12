#Wiem że kod nie jest ani efektywny, ani ładny. Oceniając go weź poszę pod uwagę,
# że jest to mj pierwszy kod w Pythonie
# wiem ze dałoby sie to wpisać w funkcję a nie kopiować wielokrotnie

from lxml import html
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from bs4 import BeautifulSoup as bsoup
#'import lxml.html as lh

#okręg 1
page = requests.get('https://wybory2018.pkw.gov.pl/pl/geografia/026401/city_council/1')
tree = html.fromstring(page.content)
Okreg1 = pd.read_html(page.text)

#okręg 2
page = requests.get('https://wybory2018.pkw.gov.pl/pl/geografia/026401/city_council/2')
tree = html.fromstring(page.content)
Okreg2 = pd.read_html(page.text)

#okręg 3
page = requests.get('https://wybory2018.pkw.gov.pl/pl/geografia/026401/city_council/3')
tree = html.fromstring(page.content)
Okreg3 = pd.read_html(page.text)

#okręg 4
page = requests.get('https://wybory2018.pkw.gov.pl/pl/geografia/026401/city_council/4')
tree = html.fromstring(page.content)
Okreg4 = pd.read_html(page.text)

#okręg 5
page = requests.get('https://wybory2018.pkw.gov.pl/pl/geografia/026401/city_council/5')
tree = html.fromstring(page.content)
Okreg5 = pd.read_html(page.text)

#okręg 6
page = requests.get('https://wybory2018.pkw.gov.pl/pl/geografia/026401/city_council/6')
tree = html.fromstring(page.content)
Okreg6 = pd.read_html(page.text)

#okręg 7
page = requests.get('https://wybory2018.pkw.gov.pl/pl/geografia/026401/city_council/7')
tree = html.fromstring(page.content)
Okreg7 = pd.read_html(page.text)




JEDYNKI = pd.DataFrame()
#Partia Zieloni
PARTIA = "Zieloni"
NR_KOMITETU = 1

tmp1 = pd.DataFrame(Okreg1[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg2[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg3[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg4[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg5[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg6[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg7[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])


#Kolicja Obywatelska
PARTIA = "Kolicja Obywatelska"
NR_KOMITETU = 2

tmp1 = pd.DataFrame(Okreg1[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg2[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg3[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg4[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg5[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg6[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg7[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])



#Kukiz'15
PARTIA = "Kukiz 15"
NR_KOMITETU = 3

tmp1 = pd.DataFrame(Okreg1[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg2[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg3[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg4[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg5[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg6[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg7[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])




#Prawo i Sprawiedliwosc
PARTIA = "PIS"
NR_KOMITETU = 4

tmp1 = pd.DataFrame(Okreg1[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg2[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg3[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg4[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg5[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg6[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg7[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])




#Jerzy Michalak
PARTIA = "Jerzy Michalak"
NR_KOMITETU = 5

tmp1 = pd.DataFrame(Okreg1[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg2[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg3[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg4[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg5[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg6[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg7[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])




#Bezpartyjny Wrocław
PARTIA = "Bezpartyjny Wroclaw"
NR_KOMITETU = 6

tmp1 = pd.DataFrame(Okreg1[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg2[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg3[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg4[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg5[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg6[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg7[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])




#JESTEŚMY STĄD
PARTIA = "Jestesmy Stad"
NR_KOMITETU = 7

tmp1 = pd.DataFrame(Okreg1[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg2[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg3[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg4[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

#==============================================================================
# tmp1 = pd.DataFrame(Okreg5[NR_KOMITETU]).iloc[0,1]
# tmp = str.split(tmp1)[1]
# if tmp.endswith('a'):
#     tmp = pd.DataFrame([5, PARTIA, tmp1, "Kobieta", 1]).transpose()
# else:
#     tmp = pd.DataFrame([5, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
# JEDYNKI = pd.concat([JEDYNKI, tmp])
#==============================================================================

tmp1 = pd.DataFrame(Okreg6[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

#==============================================================================
# tmp1 = pd.DataFrame(Okreg7[NR_KOMITETU]).iloc[0,1]
# tmp = str.split(tmp1)[1]
# if tmp.endswith('a'):
#     tmp = pd.DataFrame([7, PARTIA, tmp1, "Kobieta", 1]).transpose()
# else:
#     tmp = pd.DataFrame([7, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
# JEDYNKI = pd.concat([JEDYNKI, tmp])
#==============================================================================


#JARKA BOGUSŁAWSKIEGO
PARTIA = "Jarek Boguslawski"
NR_KOMITETU = 8

tmp1 = pd.DataFrame(Okreg1[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg2[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg3[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg4[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg5[NR_KOMITETU - 1]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg6[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg7[NR_KOMITETU - 1]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])




#WOLNI I SOLIDARNI
PARTIA = "Wolni i Solidarni"
NR_KOMITETU = 9

tmp1 = pd.DataFrame(Okreg1[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg2[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg3[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg4[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg5[NR_KOMITETU - 1]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg6[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg7[NR_KOMITETU - 1]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])




#RAFAŁA DUTKIEWICZA - SOJUSZ DLA WROCŁAWIA
PARTIA = "Rafal Dutkiewicz"
NR_KOMITETU = 10

tmp1 = pd.DataFrame(Okreg1[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg2[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg3[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg4[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg5[NR_KOMITETU - 1]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg6[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg7[NR_KOMITETU - 1]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])



#WROCŁAW DLA WSZYSTKICH
PARTIA = "Wroclaw dla Wszytkich"
NR_KOMITETU = 11

tmp1 = pd.DataFrame(Okreg1[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([1, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg2[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([2, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg3[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([3, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg4[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([4, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg5[NR_KOMITETU -1 ]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([5, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg6[NR_KOMITETU]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([6, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])

tmp1 = pd.DataFrame(Okreg7[NR_KOMITETU - 1]).iloc[0,1]
tmp = str.split(tmp1)[1]
if tmp.endswith('a'):
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Kobieta", 1]).transpose()
else:
    tmp = pd.DataFrame([7, PARTIA, tmp1, "Mezczyzna", 0]).transpose()
JEDYNKI = pd.concat([JEDYNKI, tmp])


# zmiana nazw w data frame i typow danych
print(JEDYNKI.columns)
JEDYNKI.columns = ["Okreg", "Partia", "Imie", "Plec", "Plec_bin"]
JEDYNKI.dtypes
JEDYNKI.iloc [:,0] = pd.to_numeric(JEDYNKI.iloc [:,0])
JEDYNKI.iloc [:,4] = pd.to_numeric(JEDYNKI.iloc [:,4])
JEDYNKI.dtypes

#zapiszmy do pliku 
#JEDYNKI.to_csv("Jedynki.csv", sep=';', encoding='utf-8')

# wylicznie sredniej w grupie
groupby_regiment = JEDYNKI['Plec_bin'].groupby(JEDYNKI['Partia'])
list(groupby_regiment)


#wyliczenie srenich dla komitetow
PRC_KOBIET = groupby_regiment.mean()
df_PRC_KOBIET = pd.DataFrame(PRC_KOBIET)
df_PRC_KOBIET.index.name = 'Komitet'
df_PRC_KOBIET.reset_index(inplace=True)

 #posortowanie
df_PRC_KOBIET_sort = df_PRC_KOBIET.sort_values(['Plec_bin', 'Komitet'], ascending=[False, True])

#dodaeni średnije
df_PRC_KOBIET_sort = df_PRC_KOBIET_sort.append({'Komitet': "Srednia" ,
                           'Plec_bin': np.mean(JEDYNKI.iloc[:, 4])},
                          ignore_index=True)






#wykres






def plot_bar_x():
    # this is for plotting purpose
    plt.bar(df_PRC_KOBIET_sort.iloc[:,0], df_PRC_KOBIET_sort.iloc[:,1])
    plt.xlabel('Genre', fontsize=5)
    plt.ylabel('No of Movies', fontsize=5)
    plt.xticks(index, label, fontsize=5, rotation=30)
    plt.title('Market Share for Each Genre 1995-2017')
    plt.show()







#==============================================================================
# 
# 
# 
# 
# 
# Okregi = {}
# 
# for x in range(1, 8):
#     print(str(x))    
#     page = requests.get('https://wybory2018.pkw.gov.pl/pl/geografia/026401/city_council/' 
#         + str(x))
#     tree = html.fromstring(page.content)
#     Okregi["string{0}".format(x)] = pd.read_html(page.text)
# 
#     Okreg_x = pd.read_html(page.text)
# 
#     Okregi.append(Okreg_x)
#     
#==============================================================================
