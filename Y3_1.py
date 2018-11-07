#coding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime as dt
from pandas import DataFrame

k = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ak = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

kekka = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hurimuki = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]

#読み込み
df2 = pd.read_csv ('some2.csv', header = None, skiprows = 1)
#print(df2)

for i in range(len(df2)):
    for j in range(-5, 26):
        if(j-0.5 <= df2[2][i] < j+0.5):
            k[j+5] += df2[1][i]
            ak[j+5] += 1
#print(k[30])
#print(ak)

for i in range(31):
    kekka[i] = k[i] / ak[i]

#print(kekka)

data2 =  {'average':kekka, 'hurimuki': hurimuki}
frameY3 = DataFrame(data2)

print(frameY3)
frameY3.to_csv('Y3_1.csv')