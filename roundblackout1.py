import matplotlib.pyplot as plt

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

df_m = [open_file('MLP1000_10_5.csv',"index","blackout","sink", "canttransmit")]

df_s = [open_file('SLP1000_10_5.csv',"index","blackout","sink", "canttransmit")]

df_c = [open_file('CLP1000_10_5.csv',"index","blackout","sink", "canttransmit")]


osink = []
totalo = 0
for j in range(0,len(df_o[0]['blackout'])):
    totalo = totalo + df_o[0]['blackout'][j]
    if j % 12 == 11:
        totalo = totalo * 5 / 60
        osink.append(totalo)
        totalo = 0

osink_avg = []
totalo = 0
for i in range(0,len(osink)):
    totalo = totalo + osink[i]
    # if(i%6==5):
    #     totalo = totalo / 6
    osink_avg.append(totalo)
    totalo = 0

msink = []
totalo = 0
for j in range(0,len(df_m[0]['blackout'])):
    totalo = totalo + df_m[0]['blackout'][j]
    if j % 12 == 11:
        totalo = totalo * 5 / 60
        msink.append(totalo)
        totalo = 0

msink_avg = []
totalo = 0
for i in range(0,len(msink)):
    totalo = totalo + msink[i]
    # if(i%6==5):
    #     totalo = totalo / 6
    msink_avg.append(totalo)
    totalo = 0

ssink = []
totalo = 0
for j in range(0,len(df_s[0]['blackout'])):
    totalo = totalo + df_s[0]['blackout'][j]
    if j % 12 == 11:
        totalo = totalo * 5 / 60
        ssink.append(totalo)
        totalo = 0

ssink_avg = []
totalo = 0
for i in range(0,len(ssink)):
    totalo = totalo + ssink[i]
    # if(i%6==5):
    #     totalo = totalo / 6
    ssink_avg.append(totalo)
    totalo = 0

print(ssink_avg)
csink = []
totalo = 0
for j in range(0,len(df_c[0]['blackout'])):
    totalo = totalo + df_c[0]['blackout'][j]
    if j % 12 == 11:
        totalo = totalo * 5 / 60
        csink.append(totalo)
        totalo = 0

csink_avg = []
totalo = 0
for i in range(0,len(csink)):
    totalo = totalo + csink[i]
    # if(i%6==5):
    #     totalo = totalo / 6
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
plt.plot(range(0,len(ssink_avg)), ssink_avg, marker='*', color='green', label='Line shift', markevery=24, markersize=10)
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

