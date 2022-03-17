#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Mince: aktuální kurzy měn

import sys, io, os.path
import pystray                                   # system tray ikona - pip install pystray
from forex_python.converter import CurrencyRates # aktualni kurzy men - pip install forex_python
import pandas as Pds                             # prace s dataframy a tabulkami jako podklad pro grafy - pip install pandas
from matplotlib import pyplot as Plt             # grafy - pip install matplotlib
from datetime import datetime as Dt, timedelta   # datum a cas - pip install datetime

# nacteni vlastni knihovny men
import fiat # promenne: eur, usd, czk, gbp, chf, pln, rub

ecb_update_time = 990 # odpovida casu 16:30 (prepocet na minuty od pulnoci), kdy ECB aktualizuje denni kurzy

# vytvoreni tridy (objektu) meny
class Mena(object):
    
    def __init__(self, fiatobj):
        for key in fiatobj:
            setattr(self, key, fiatobj[key])
    
    # vypis hodnoty meny a symbolu meny, dle konkretni meny pred nebo za hodnotou
    def currencyListing(self, val):
        if (self.pos_symbol == 1):
            return str(val)+' '+str(self.symbol)
        if (self.pos_symbol == 2):
            return str(self.symbol)+' '+str(val)


# vytvoreni tridy menoveho paru
class MenovyPar(object):

    current_rate = 0

    def __init__(self, fiat1, fiat2):
        self.f1 = fiat1
        self.f2 = fiat2
    
    def __bool__(self):
        global current_rate
        try:
            # pouziti knihovny forex_python
            c = CurrencyRates()
            current_rate = c.get_rate(self.f1, self.f2)
            return True
        except:
            print('Aktualni kurz menoveho paru neni dostupny')
            return False

    def currentRate(self):
        global current_rate
        return current_rate

class DataSet(object):

    data_path = 'datasets/'
    files_suffix = '.py';

    def __init__(self, date):
        
        self.date = Dt.fromisoformat(str(date))
        self.dataset = self.data_path + str(self.date.today()) + self.files_suffix
        
        if (os.path.exists(self.dataset)):
            print('soubor datasetu existuje, tak z neho cti')
        else:
            print('stahni dataset dle date a pak z neho cti')
            self.createDataSet(self.dataset)

    def createDataSet(self, pathfile):
        self.pathfile = pathfile
        #c = CurrencyRates()
        with open(pathfile, 'w') as f:
            #f.write('EUR = {}'.format(c.get_rates('EUR')))
            #f.write('USD = {}'.format(c.get_rates('USD')))
            #f.write('CZK = {}'.format(c.get_rates('CZK')))
            #f.write('GBP = {}'.format(c.get_rates('GBP')))
            #f.write('CHF = {}'.format(c.get_rates('CHF')))
            #f.write('PLN = {}'.format(c.get_rates('PLN')))
            #f.write('RUB = {}'.format(c.get_rates('RUB')))
            f.write(' ')

# Main
if __name__ == "__main__":

    euro = Mena(fiat.eur)
    koruna = Mena(fiat.czk)
    #eurczk = MenovyPar(euro.abbr, koruna.abbr)

    

    #if (eurczk and euro and koruna):
        # 1 € = 24.867 Kč
        #print(euro.currencyListing(1) + ' = ' + koruna.currencyListing(eurczk.currentRate()))
    
    # nacteni datasetu dennich kurzu
    #c = CurrencyRates()
    #print(c.get_rates('EUR'))
    #print(c.get_rates('USD'))
    #print(c.get_rates('CZK'))
    #print(c.get_rates('GBP'))
    #print(c.get_rates('CHF'))
    #print(c.get_rates('PLN'))
    #print(c.get_rates('RUB'))

    # pri otevreni programu kontroluji, zda je pred 16:30 nebo po

    now = Dt.now()
    today = Dt.today()
    td = timedelta(1)
    minutes_from_midnight = (now.hour * 60) + now.minute

    if (minutes_from_midnight > ecb_update_time):
        # je po 16:30
        print('je po 16:30')
        current_daily_rate = DataSet(today)
    
    if (minutes_from_midnight <= ecb_update_time):
        # je pred nebo rovno 16:30
        print('je pred nebo rovno 16:30')
        yesterdays_daily_rate = DataSet(today - td)
