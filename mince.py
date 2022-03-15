#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Mince: aktuální kurzy měn

import sys, io
import pystray                                   # system tray ikona - pip install pystray
from forex_python.converter import CurrencyRates # aktualni kurzy men - pip install forex_python
import pandas as Pds                             # prace s dataframy a tabulkami jako podklad pro grafy - pip install pandas
from matplotlib import pyplot as Plt             # grafy - pip install matplotlib
from datetime import datetime as Dt              # datum a cas - pip install datetime

# nacteni vlastni knihovny men
import fiat # promenne: eur, usd, czk, gbp, chf, pln, rub

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

# Main
if __name__ == "__main__":

    euro = Mena(fiat.eur)
    koruna = Mena(fiat.czk)
    #eurczk = MenovyPar(euro.abbr, koruna.abbr)

    now = Dt.now()
    #print(now.strftime('%Y-%m-%d %H:%M:%S'));

    #if (eurczk and euro and koruna):
        # 1 € = 24.867 Kč
        #print(euro.currencyListing(1) + ' = ' + koruna.currencyListing(eurczk.currentRate()))
    
    # nacteni datasetu dennich kurzu
    c = CurrencyRates()
    print(c.get_rates('EUR'))
    print(c.get_rates('USD'))
    print(c.get_rates('CZK'))
    print(c.get_rates('GBP'))
    print(c.get_rates('CHF'))
    print(c.get_rates('PLN'))
    print(c.get_rates('RUB'))

