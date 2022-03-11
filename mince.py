#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Mince: aktuální kurzy měn

import sys, io
import pystray                                   # system tray ikona - pip install pystray
from forex_python.converter import CurrencyRates # aktualni kurzy men - pip install forex_python
import pandas as pds                             # prace s dataframy a tabulkami jako podklad pro grafy - pip install pandas
from matplotlib import pyplot as plt             # grafy - pip install matplotlib
