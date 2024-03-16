#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 10:58:33 2024

@author: sofiapeleteiro
"""

import pandas as pd
import scipy.stats as ss
from datetime import datetime
from plotnine import *
from scipy.stats import binom, norm, hypergeom, poisson, expon, uniform
import matplotlib.pyplot as plt

customerprime=pd.read_excel("Customers_prime_weekend.xlsx")


customerprime.shape
customerprime.describe()

time= "Effective_To_Date"
type(time)



