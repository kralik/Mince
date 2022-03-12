#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Realie jednotlivych fiat men
# abbr je zkratka meny dle ISO 4217
# pos_symbol je pozice symbolu vuci hodnote, 1: za, 2: pred hodnotou

from PIL import Image # knihovna pro zpracovani png obrazku - pip install pillow

eur = {
    'name': 'Euro',
    'abbr': 'EUR',
    'symbol': '€',
    'pos_symbol': 1,
    'subunit_use': False,
    'subunit_name': 'Euro cent',
    'subunit_symbol': '',
    'subunit_value': 1/100,
    'flag': Image.open('images/flags/eur.png')
}

usd = {
    'name': 'Americký dolar',
    'abbr': 'USD',
    'symbol': '$',
    'pos_symbol': 2,
    'subunit_use': True,
    'subunit_name': 'Cent',
    'subunit_symbol': '¢',
    'subunit_value': 1/100,
    'flag': Image.open('images/flags/usd.png')
}

czk = {
    'name': 'Česká koruna',
    'abbr': 'CZK',
    'symbol': 'Kč',
    'pos_symbol': 1,
    'subunit_use': False,
    'subunit_name': 'Haléř',
    'subunit_symbol': 'h',
    'subunit_value': 1/100,
    'flag': Image.open('images/flags/czk.png')
}

gbp = {
    'name': 'Libra šterlinků',
    'abbr': 'GBP',
    'symbol': '£',
    'pos_symbol': 1,
    'subunit_use': True,
    'subunit_name': 'Penny',
    'subunit_symbol': 'p',
    'subunit_value': 1/100,
    'flag': Image.open('images/flags/gbp.png')
}

chf = {
    'name': 'Švýcarský frank',
    'abbr': 'CHF',
    'symbol': 'Fr',
    'pos_symbol': 1,
    'subunit_use': True,
    'subunit_name': 'Rapp',
    'subunit_symbol': 'rapp',
    'subunit_value': 1/100,
    'flag': Image.open('images/flags/chf.png')
}

pln = {
    'name': 'Polský zlotý',
    'abbr': 'PLN',
    'symbol': 'zł',
    'pos_symbol': 1,
    'subunit_use': True,
    'subunit_name': 'Groš',
    'subunit_symbol': 'gr',
    'subunit_value': 1/100,
    'flag': Image.open('images/flags/pln.png')
}

rub = {
    'name': 'Ruský rubl',
    'abbr': 'RUB',
    'symbol': '₽',
    'pos_symbol': 1,
    'subunit_use': True,
    'subunit_name': 'Kopějka',
    'subunit_symbol': 'kopějek',
    'subunit_value': 1/100,
    'flag': Image.open('images/flags/rub.png')
}