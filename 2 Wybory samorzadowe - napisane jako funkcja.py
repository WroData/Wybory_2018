# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 15:10:05 2018

@author: User
"""


from lxml import html
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def Get_okreng_page(NR_okreg): 
    page = requests.get('https://wybory2018.pkw.gov.pl/pl/geografia/026401/city_council/' + 
                        str(NR_okreg))
    TMP_okreg = pd.read_html(page.text)
    return(TMP_okreg);
    
    
okreg = Get_okreng_page(1)



ALL_data = pd.DataFrame()

def Get_kandydatow(PARTIA, NR_KOMITETU, W_jakich_okregach):
    ALL_data_tmp = pd.DataFrame()
    for x in W_jakich_okregach:
        okreg = Get_okreng_page(x)
        if(NR_KOMITETU > 7 and (x == 5 or x == 7)):
            NR_KOMITETU_TMP = NR_KOMITETU - 1
        else:
            NR_KOMITETU_TMP = NR_KOMITETU
        tmp = pd.DataFrame(okreg[NR_KOMITETU_TMP])
        tmp['Komitet'] = PARTIA
        tmp['Okreg'] = x
        ALL_data_tmp = pd.concat([ALL_data_tmp, tmp])
        print(PARTIA + " okreg: " + str(x))
        
    return(ALL_data_tmp);


ALL_data_tmp = Get_kandydatow(PARTIA = "KW Partia Zieloni", 
               NR_KOMITETU = 1,
               W_jakich_okregach = [1, 2, 3, 4, 5, 6, 7])
ALL_data = pd.concat([ALL_data, ALL_data_tmp])


ALL_data_tmp = Get_kandydatow(PARTIA = "KKW Koalicja Obywatelska", 
               NR_KOMITETU = 2,
               W_jakich_okregach = [1, 2, 3, 4, 5, 6, 7])
ALL_data = pd.concat([ALL_data, ALL_data_tmp])


ALL_data_tmp = Get_kandydatow(PARTIA = "KWW Kukiz'15", 
               NR_KOMITETU = 3,
               W_jakich_okregach = [1, 2, 3, 4, 5, 6, 7])
ALL_data = pd.concat([ALL_data, ALL_data_tmp])


ALL_data_tmp = Get_kandydatow(PARTIA = "KW Prawo i Sprawiedliwość", 
               NR_KOMITETU = 4,
               W_jakich_okregach = [1, 2, 3, 4, 5, 6, 7])
ALL_data = pd.concat([ALL_data, ALL_data_tmp])


ALL_data_tmp = Get_kandydatow(PARTIA = "KWW Bezpartyjny ruch obywatelski Jerzego Michalaka", 
               NR_KOMITETU = 5,
               W_jakich_okregach = [1, 2, 3, 4, 5, 6, 7])
ALL_data = pd.concat([ALL_data, ALL_data_tmp])


ALL_data_tmp = Get_kandydatow(PARTIA = "KW Bezpartyjny Wrocław", 
               NR_KOMITETU = 6,
               W_jakich_okregach = [1, 2, 3, 4, 5, 6, 7])
ALL_data = pd.concat([ALL_data, ALL_data_tmp])


ALL_data_tmp = Get_kandydatow(PARTIA = "KW Jesteśmy Stąd", 
               NR_KOMITETU = 7,
               W_jakich_okregach = [1, 2, 3, 4, 6])
ALL_data = pd.concat([ALL_data, ALL_data_tmp])


ALL_data_tmp = Get_kandydatow(PARTIA = "KWW Jarka Bogusławskiego", 
               NR_KOMITETU = 8,
               W_jakich_okregach = [1, 2, 3, 4, 5, 6, 7])
ALL_data = pd.concat([ALL_data, ALL_data_tmp])


ALL_data_tmp = Get_kandydatow(PARTIA = "KW Wolni i Solidarni", 
               NR_KOMITETU = 9,
               W_jakich_okregach = [1, 2, 3, 4, 5, 6, 7])
ALL_data = pd.concat([ALL_data, ALL_data_tmp])


ALL_data_tmp = Get_kandydatow(PARTIA = "KWW Rafała Dutkiewicza - Sojusz dla Wrocławia", 
               NR_KOMITETU = 10,
               W_jakich_okregach = [1, 2, 3, 4, 5, 6, 7])
ALL_data = pd.concat([ALL_data, ALL_data_tmp])


ALL_data_tmp = Get_kandydatow(PARTIA = "KWW Wroclaw dla Wszytkich", 
               NR_KOMITETU = 11,
               W_jakich_okregach = [1, 2, 3, 4, 5, 6, 7])
ALL_data = pd.concat([ALL_data, ALL_data_tmp])



#zapisz dane
#zapiszmy do pliku 
ALL_data.to_csv("all_data.csv", sep=';', encoding='utf-8')



