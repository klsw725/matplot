import matplotlib.pyplot as plt

import inputData as id

from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset
from matplotlib.patches import Rectangle
from matplotlib import gridspec

plt.rcParams['font.size'] = 30
plt.rcParams['figure.figsize'] = (21,9)

def zoomingBox(ax1, roi, ax2, color='red', linewidth=3):
    ax1.add_patch(Rectangle([roi[0],roi[2]], roi[1]-roi[0], roi[3]-roi[2],**dict([('fill',False), ('linestyle','dashed'), ('color',color), ('linewidth',linewidth)]) ))
    srcCorners = [[roi[0],roi[2]], [roi[0],roi[3]], [roi[1],roi[2]], [roi[1],roi[3]]]
    dstCorners = ax2.get_position().corners()
    srcBB = ax1.get_position()
    dstBB = ax2.get_position()
    if (dstBB.min[0]>srcBB.max[0] and dstBB.max[1]<srcBB.min[1]) or (dstBB.max[0]<srcBB.min[0] and dstBB.min[1]>srcBB.max[1]):
        src = [0, 3]; dst = [0, 3]
    elif (dstBB.max[0]<srcBB.min[0] and dstBB.max[1]<srcBB.min[1]) or (dstBB.min[0]>srcBB.max[0] and dstBB.min[1]>srcBB.max[1]):
        src = [1, 2]; dst = [1, 2]
    elif dstBB.max[1] < srcBB.min[1]:
        src = [0, 2]; dst = [1, 3]
    elif dstBB.min[1] > srcBB.max[1]:
        src = [1, 3]; dst = [0, 2]
    elif dstBB.max[0] < srcBB.min[0]:
        src = [0, 1]; dst = [2, 3]
    elif dstBB.min[0] > srcBB.max[0]:
        src = [2, 3]; dst = [0, 1]
    for k in range(2):
        ax1.annotate('', xy=dstCorners[dst[k]], xytext=srcCorners[src[k]], xycoords='figure fraction', textcoords='data', arrowprops=dict([('arrowstyle','-'), ('color',color), ('linewidth',linewidth)]))



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

gs = gridspec.GridSpec(nrows=1, ncols=2, width_ratios=[5,2])


fig =plt.figure()
ax = fig.add_subplot(gs[0])

ax.set_ylim(min(msink_avg),max(max(ssink_avg), max(osink_avg), max(csink_avg), max(msink_avg))+200)
ax.set_xlim(0,len(msink_avg))
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

ax.set_xticks([i for i in range(0,len(msink_avg)+120,120)], for_xtick)
plt.plot(range(0,len(osink_avg)), osink_avg, marker='^', color='blue', label='LBDD', markevery=24, markersize=10)
plt.plot(range(0,len(ssink_avg)), ssink_avg, marker='*', color='green', label='Single Line shift', markevery=24, markersize=10)
plt.plot(range(0,len(csink_avg)), csink_avg, marker='h', color='black', label='LARCMS', markevery=24, markersize=10)
plt.plot(range(0,len(msink_avg)), msink_avg, marker='s', color='red', label="Proposed scheme", markevery=24, markersize=10)

print(len(msink_avg))
plt.legend(loc=2)
ax.set_xlabel('Simulation time (Rounds)', labelpad=10)
ax.set_ylabel('Blackout time (Hours)', labelpad=10)

ax.tick_params(which='major', direction='in', length = 15)
ax.tick_params(axis='y', which='major', direction='in', length = 7)


# plt1 = zoomed_inset_axes(ax, 1, loc='lower right')
x1, x2, y1, y2 = 170,280,150,850
# plt1.plot(range(0,len(osink_avg)), osink_avg, marker='^', color='blue', label='LBDD', markevery=6, markersize=10)
# plt1.plot(range(0,len(ssink_avg)), ssink_avg, marker='*', color='green', label='Single Line shift', markevery=6, markersize=10)
# plt1.plot(range(0,len(csink_avg)), csink_avg, marker='h', color='black', label='LARCMS', markevery=6, markersize=10)
# plt1.plot(range(0,len(msink_avg)), msink_avg, marker='s', color='red', label="Proposed scheme", markevery=6, markersize=10)
# # plt1.axis([x1, x2, y1, y2])
# plt1.set_xlim(x1, x2)
# plt1.set_ylim(y1, y2)

# mark_inset(ax,plt1,loc1=1,loc2=3)
ax2 = fig.add_subplot(gs[1])
ax2.plot(list(range(x1,x2)), osink_avg[x1:x2], marker='^', color='blue', label='LBDD', markevery=24, markersize=10)
ax2.plot(list(range(x1,x2)), ssink_avg[x1:x2], marker='*', color='green', label='Single Line shift', markevery=24, markersize=10)
ax2.plot(list(range(x1,x2)), csink_avg[x1:x2], marker='h', color='black', label='LARCMS', markevery=24, markersize=10)
ax2.plot(list(range(x1,x2)), msink_avg[x1:x2], marker='s', color='red', label="Proposed scheme", markevery=24, markersize=10)

ax2.set_ylim(y1, y2)
ax2.set_xlim(x1, x2)
# for_yticks = []

# # for i in range(0,1100,100):
# #     for_yticks.append(format(i,","))
# #
# # plt.yticks([i for i in range(0,1100,100)],for_yticks)
# # plt.xlim(0,len(osink_avg)-30)

# for_xtick = []
# for i in range(0,len(msink_avg)+120,120):
#     if i == 0:
#         for_xtick.append("")
#     else:
#         for_xtick.append(i)

# ax2.set_xticks([i for i in range(0,len(msink_avg)+120,120)], for_xtick)
zoomingBox(ax, [x1, x2, y1, y2], ax2)


plt.savefig('roundblackout.png',bbox_inches='tight',padding=0)
plt.savefig('roundblackout.pdf',bbox_inches='tight',padding=0)
plt.show()

