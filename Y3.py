#coding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime as dt
from pandas import DataFrame

#読み込み
df2 = pd.read_csv ('heart-2018-07-02-6-Y3.csv', header = None)

#CSVの時間をtimedeltaに変換
tmd2 = pd.to_timedelta(df2[2])

#print(df2)

#データフレーム作成
data2 =  {'heart':df2[1], 'time':tmd2 }
frame2 = DataFrame(data2)

#経過時間
h2 = {}

#k=心拍上昇率
k2 = {}
average0 = 0
count2 = 0

#heart = 心拍数（hert）
heart2 = 0

#アノテーション部分の心拍数を記録
a0 = []

#各CSVのの時間を秒数に変換し63300秒（17：35）を引いて分に直すs
for num in range(865):
    h2[num] = (frame2.time[num].seconds -63300) /60.0

    df2.loc[num, 4] = h2[num]
#print(list)

frame2['time1'] =df2[4]
print(frame2.time1)


for num in range(len(df2)):
    if(frame2.time1[num] <=0):
            heart2 += frame2.heart[num]
            count2 += 1
    else:
        break

average0 = heart2 / count2 + 0.0
print(average0)

for num in range(len(df2)):
    k2[num] = (frame2.heart[num] / average0 )
    df2.loc[num, 5] = k2[num]

frame2['average'] = df2[5]

#10-30秒
A1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  
countA1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#30-60
B1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
countB1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for num in range(len(df2)):
    for cc in range (20):
        if(frame2.time1[num] < 0):
            break
        elif(cc <= frame2.time1[num] and frame2.time1[num] < cc + 0.5):
            A1[cc] += frame2.heart[num]
            countA1[cc] += 1
        elif(cc + 0.5 <= frame2.time1[num] and frame2.time1[num] < cc + 1):
            B1[cc] += frame2.heart[num]
            countB1[cc] += 1
print(A1)
print(countA1)
print()
print(B1)
print(countB1)


Y3_H = np.convolve(frame2.average, np.ones(10)/float(10), 'vaild')
Y3_T = np.convolve(frame2.time1, np.ones(10)/float(10), 'vaild')

#Y3_H = frame2.average
#Y3_T = frame2.time1

dd1 =  {'heart':Y3_H, 'time':Y3_T }
fr1 = DataFrame(dd1)
fr1.to_csv('some2.csv')


#描画
fig = plt.figure()
ax = fig.add_subplot(1,1,1)



ax.plot(Y3_T, Y3_H,  color="r", linewidth = 1.5)
ax.plot(frame2.time1, frame2.average)

plt.vlines(0,0.5, 1.4, colors="k", linestyle="solid")
plt.vlines(20.5,0.5, 1.4, colors="k", linestyle="solid")
ax.legend(loc='lower right')
plt.xlabel('Time [min]',  fontsize = 10)
plt.ylabel('Heart rate ratio to rest state[-]',  fontsize = 10,)
plt.grid()
plt.tick_params(labelsize = 10)
plt.xlim([-5,26])
plt.ylim([0.5,1.4])



plt.show()
