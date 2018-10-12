

from lxml import html
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bsoup

import lxml.html as lh


page = requests.get('https://wybory2018.pkw.gov.pl/pl/geografia/026401/city_council/1')
tree = html.fromstring(page.content)
'print(page)
'print(tree)
'print("kupa")

'print(page.text)
'type(page)
'page.response()




ofile = open(page.text)
soup = bsoup(page.text)
soup.prettify()

tables = soup.find_all("tbody")

storeTable = tables[0].find_all("tr")
storeValueRows = tables[1].find_all("tr")

df = pd.read_html(page.text)
df.head()

#Store the contents of the website under doc
doc = lh.fromstring(page.content)

#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//td+//td')


#Check the length of the first 12 rows
[len(T) for T in tr_elements[:12]]


#This will create a list of buyers:
buyers = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "stat_table", " " ))]')
print(buyers)
np_buyers = np.array(buyers)
print(np_buyers)


# fix HTML
soup = BeautifulSoup(buyers, "html.parser")
for body in soup("tbody"):
    body.unwrap()

df = pd.read_html(str(soup), flavor="bs4")
print(df[0])



#This will create a list of prices
prices = tree.xpath('//td')
print(prices)
