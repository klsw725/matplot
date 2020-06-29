import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

import inputData as id

# plt.rcParams['figure.figsize'] = (16,12)
plt.rcParams['font.size'] = 30
# plt.tight_layout(rect=(10,0,0,1))
# plt.subplots_adjust(left=0.01)
osink = []
totalo = 0
for j in range(0,len(id.df_o[0]['sink'])):
    if j % 6 == 5:
        for i in range(0, 5):
            totalo = totalo + id.df_o[i+5]['sink'][j]
        totalo = totalo/5
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
for j in range(0,len(id.df_m[0]['sink'])):
    if j % 6 == 5:
        for i in range(0, 5):
            totalo = totalo + id.df_m[i+5]['sink'][j]
        totalo = totalo/5
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


plt.ylim(min(osink_avg),4)
plt.xlim(0,len(msink_avg))

for_stick = []
for i in np.arange(0,max(osink_avg)+0.5,0.5):
    for_stick.append(format(i,","))
for_stick[0]=0

plt.yticks([i for i in np.arange(0,max(osink_avg)+0.5,0.5)],for_stick)
# plt.xlim(0,len(osink_avg)-30)

for_xtick = []
for i in range(0,35,5):
    if i == 0:
        for_xtick.append("")
    else:
        for_xtick.append(i)

plt.xticks([i for i in range(0,len(osink_avg)+30,30)], for_xtick)
plt.plot(range(0,len(osink_avg)), osink_avg, marker='^', color='blue', label='OLP', markevery=6, markersize=10)
plt.plot(range(0,len(msink_avg)), msink_avg, marker='s', color='red', label="Proposed scheme", markevery=6, markersize=10)

plt.legend()
plt.xlabel('Simulation time (days)', labelpad=10)
plt.ylabel('Amount of gathered data at the sink (MB)', labelpad=10)

ax = plt.gca()
ax.tick_params(which='major', direction='in', length = 7)

plt.savefig('roundsink.png',bbox_inches='tight')
plt.show()

