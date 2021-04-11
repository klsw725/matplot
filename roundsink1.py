import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

import pandas as pd

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 25
plt.rcParams['figure.figsize'] = (21,9)

color_dict = ['#0000FF','#FF0000']

plt.rcParams['font.size'] = 30

def open_file(file_name, *args):
    names = []
    for i in args:
        names.append(i)
    df = pd.read_csv(file_name,names=names)
    return df

def total_data(df,column):
    total = 0
    for i in range(0,len(df[column])):
        total = total + df[column][i]
    return total

df_o = [open_file('OLP1000_10_5.csv',"index","blackout","sink", "canttransmit")]

df_m = [open_file('MLP1000_10_5.csv',"index","blackout","sink","canttransmit")]

df_s = [open_file('SLP1000_10_5.csv',"index","blackout","sink","canttransmit")]

df_c = [open_file('CLP1000_10_5.csv',"index","blackout","sink","canttransmit")]
# plt.tight_layout(rect=(10,0,0,1))
# plt.subplots_adjust(left=0.01)
osink = []
totalo = 0
for j in range(0,len(df_o[0]['sink'])):
    if j % 12 == 11:
        totalo = totalo + df_o[0]['sink'][j]
        totalo = totalo / (1024*1024)
        osink.append(totalo)
        totalo = 0

osink_avg = []
totalo = 0
for i in range(0,len(osink)):
    totalo = totalo + osink[i]
    if(i%4==3):
        totalo = totalo /4
        osink_avg.append(totalo)
        totalo = 0

msink = []
totalo = 0
for j in range(0,len(df_m[0]['sink'])):
    if j % 12 == 11:
        totalo = totalo + df_m[0]['sink'][j]
        # totalo = totalo/5
        totalo = totalo / (1024*1024)
        msink.append(totalo)
        totalo = 0

msink_avg = []
totalo = 0
for i in range(0,len(msink)):
    totalo = totalo + msink[i]
    if(i%4==3):
        totalo = totalo /4
        msink_avg.append(totalo)
        totalo = 0

ssink = []
totalo = 0
for j in range(0,len(df_s[0]['sink'])):
    if j % 12 == 11:
        # for i in range(0, 5):
        totalo = totalo + df_s[0]['sink'][j]
        # totalo = totalo/5
        totalo = totalo / (1024*1024)
        ssink.append(totalo)
        totalo = 0

ssink_avg = []
totalo = 0
for i in range(0,len(ssink)):
    totalo = totalo + ssink[i]
    if(i%4==3):
        totalo = totalo / 4
        ssink_avg.append(totalo)
        totalo = 0

csink = []
totalo = 0
for j in range(0,len(df_c[0]['sink'])):
    if j % 12 == 11:
        # for i in range(0, 5):
        totalo = totalo + df_c[0]['sink'][j]
        # totalo = totalo/5
        totalo = totalo / (1024*1024)
        csink.append(totalo)
        totalo = 0

csink_avg = []
totalo = 0
for i in range(0,len(csink)):
    totalo = totalo + csink[i]
    if(i%4==3):
        totalo = totalo /4
        csink_avg.append(totalo)
        totalo = 0


plt.ylim(0,max(max(ssink_avg), max(osink_avg), max(csink_avg), max(msink_avg)))
plt.xlim(0,len(msink_avg))

for_stick = []
for i in np.arange(0,max(max(ssink_avg), max(osink_avg), max(csink_avg), max(msink_avg))+2,2):
    for_stick.append(format(i,","))
for_stick[0]=0

plt.yticks([i for i in np.arange(0,max(max(ssink_avg), max(osink_avg), max(csink_avg), max(msink_avg))+2, 2)],for_stick)
# plt.xlim(0,len(osink_avg)-30)

for_xtick = []
for i in range(0,len(msink_avg)+660,120):
    if i == 0:
        for_xtick.append("")
    else:
        for_xtick.append(i)

plt.xticks([i for i in range(0,len(msink_avg)+30,30)], for_xtick)
plt.plot(range(0,len(osink_avg)), osink_avg, marker='^', color='blue', label='LBDD', markevery=6, markersize=10)
plt.plot(range(0,len(ssink_avg)), ssink_avg, marker='*', color='green', label='Line shift', markevery=6, markersize=10)
plt.plot(range(0,len(csink_avg)), csink_avg, marker='h', color='black', label='LARCMS', markevery=6, markersize=10)
plt.plot(range(0,len(msink_avg)), msink_avg, marker='s', color='red', label="Proposed scheme", markevery=6, markersize=10)

plt.legend(loc=1)
plt.xlabel('Simulation time (Rounds)', labelpad=10)
plt.ylabel('Amount of gathered data at the sink (MB)', labelpad=10)

ax = plt.gca()
ax.tick_params(which='major', direction='in', length = 7)

plt.savefig('roundsink.png',bbox_inches='tight')
plt.savefig('roundsink.pdf',bbox_inches='tight')
plt.show()

