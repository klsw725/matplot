import matplotlib.pyplot as plt

import inputData as id

plt.rcParams['font.size'] = 30

osink = []
totalo = 0
for j in range(0,len(id.df_o[0]['blackout'])):
    if j % 6 == 5:
        for i in range(0, 5):
            totalo = totalo + id.df_o[i+5]['blackout'][j]
        totalo = totalo/5
        totalo = totalo * 10 / 60
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
for j in range(0,len(id.df_m[0]['blackout'])):
    if j % 6 == 5:
        for i in range(0, 5):
            totalo = totalo + id.df_m[i+5]['blackout'][j]
        totalo = totalo/5
        totalo = totalo * 10 / 60
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

plt.ylim(min(msink_avg),140)
plt.xlim(0,len(msink_avg))
for_yticks = []
for i in range(0,160,20):
    for_yticks.append(format(i,","))

plt.yticks([i for i in range(0,160,20)],for_yticks)
# plt.xlim(0,len(osink_avg)-30)

for_xtick = []
for i in range(0,35,5):
    if i == 0:
        for_xtick.append("")
    else:
        for_xtick.append(i)

plt.xticks([i for i in range(0,len(osink_avg)+30,30)], for_xtick)
plt.plot(range(0,len(osink_avg)), osink_avg, marker='^', color='blue', label='OLP', markevery=6, markersize=10)
plt.plot(range(0,len(msink_avg)), msink_avg, marker='s', color='red', label='Proposed scheme', markevery=6, markersize=10)


plt.legend(loc=2)
plt.xlabel('Simulation time (days)', labelpad=10)
plt.ylabel('Blackout time (Hours)', labelpad=10)

ax = plt.gca()
ax.tick_params(which='major', direction='in', length = 15)
ax.tick_params(axis='y', which='major', direction='in', length = 7)

plt.savefig('roundblackout.png',bbox_inches='tight',padding=0)
plt.show()

