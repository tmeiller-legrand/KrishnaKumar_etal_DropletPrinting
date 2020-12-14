#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 16:52:38 2020

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("/Users/user/Documents/DPhil_Projects/Droplet-printing/Methods/StrainGrowthCurves/Analysis/TestRavGrowthArea.csv")
data = list(df)
data2 = []
for i in data:
    data2.append(float(i))
data2[11] = np.mean((data2[10],data2[12]))

x = np.arange(0, 105, 5)

model = LinearRegression()
y_exp = np.log(data2)
model.fit(x.reshape((-1,1)), y_exp)
y_new = model.predict(x[:, np.newaxis])
xt2 = (np.log(2)/model.coef_)