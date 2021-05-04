import matplotlib.pyplot as plt

import inputData as id

plt.rcParams['font.size'] = 30


osink1 = []
osink = []
totalo = 0
for j in range(0,len(id.df_o[0]['blackout'])):
    for i in range(0, 5):
        totalo = totalo + id.df_o[i+5]['blackout'][j]
    totalo = totalo/5
    totalo = totalo * 5 / 60
    osink1.append(totalo)
    totalo = 0

for j in range(0,len(osink1)):
    totalo = totalo + osink1[j]
    if j % 12 == 11:
        osink.append(totalo)
        totalo = 0


osink_avg = []
totalo = 0
for i in range(0,len(osink)):
    totalo = totalo + osink[i]
    # if(i%4==3):
    #     totalo = totalo /4
    osink_avg.append(totalo)
    totalo = 0

msink1 = []
msink = []
totalo = 0
for j in range(0,len(id.df_m[0]['blackout'])):
    for i in range(0, 5):
        totalo = totalo + id.df_m[i+5]['blackout'][j]
    totalo = totalo/5
    totalo = totalo * 5 / 60
    msink1.append(totalo)
    totalo = 0

for j in range(0,len(msink1)):
    totalo = totalo + msink1[j]
    if j % 12 == 11:
        msink.append(totalo)
        totalo = 0

msink_avg = []
totalo = 0
for i in range(0,len(msink)):
    totalo = totalo + msink[i]
    # if(i%4==3):
    #     totalo = totalo /4
    msink_avg.append(totalo)
    totalo = 0

ssink1 = []
ssink = []
totalo = 0
for j in range(0,len(id.df_s[0]['blackout'])):
    for i in range(0, 5):
        totalo = totalo + id.df_s[i+5]['blackout'][j]
    totalo = totalo/5
    totalo = totalo * 5 / 60
    ssink1.append(totalo)
    totalo = 0

for j in range(0,len(ssink1)):
    totalo = totalo + ssink1[j]
    if j % 12 == 11:
        ssink.append(totalo)
        totalo = 0

ssink_avg = []
totalo = 0
for i in range(0,len(ssink)):
    totalo = totalo + ssink[i]
    # if(i%4==3):
    #     totalo = totalo /4
    ssink_avg.append(totalo)
    totalo = 0

csink1 = []
csink = []
totalo = 0
for j in range(0,len(id.df_c[0]['blackout'])):
    for i in range(0, 5):
        totalo = totalo + id.df_c[i+5]['blackout'][j]
    totalo = totalo/5
    totalo = totalo * 5 / 60
    csink1.append(totalo)
    totalo = 0

for j in range(0,len(csink1)):
    totalo = totalo + csink1[j]
    if j % 12 == 11:
        csink.append(totalo)
        totalo = 0

csink_avg = []
totalo = 0
for i in range(0,len(csink)):
    totalo = totalo + csink[i]
    # if(i%4==3):
    #     totalo = totalo /4
    csink_avg.append(totalo)
    totalo = 0

plt.ylim(min(msink_avg),max(max(ssink_avg), max(osink_avg), max(csink_avg), max(msink_avg))+200)
plt.xlim(0,len(msink_avg))
for_yticks = []

# for i in range(0,1100,100):
#     for_yticks.append(format(i,","))
#
# plt.yticks([i for i in range(0,1100,100)],for_yticks)
# plt.xlim(0,len(osink_avg)-30)

for_xtick = []
for i in range(0,len(msink_avg)+120,120):
    if i == 0:
        for_xtick.append("")
    else:
        for_xtick.append(i)

plt.xticks([i for i in range(0,len(msink_avg)+120,120)], for_xtick)
plt.plot(range(0,len(osink_avg)), osink_avg, marker='^', color='blue', label='LBDD', markevery=24, markersize=10)
plt.plot(range(0,len(ssink_avg)), ssink_avg, marker='*', color='green', label='Single Line shift', markevery=24, markersize=10)
plt.plot(range(0,len(csink_avg)), csink_avg, marker='h', color='black', label='LARCMS', markevery=24, markersize=10)
plt.plot(range(0,len(msink_avg)), msink_avg, marker='s', color='red', label="Proposed scheme", markevery=24, markersize=10)

plt.legend(loc=2)
plt.xlabel('Simulation time (Rounds)', labelpad=10)
plt.ylabel('Blackout time (Hours)', labelpad=10)

ax = plt.gca()
ax.tick_params(which='major', direction='in', length = 15)
ax.tick_params(axis='y', which='major', direction='in', length = 7)

plt.savefig('roundblackout.png',bbox_inches='tight',padding=0)
plt.savefig('roundblackout.pdf',bbox_inches='tight',padding=0)
plt.show()

