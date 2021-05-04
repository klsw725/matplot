import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import numpy as np
import seaborn as sns
import pandas as pd

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 25
plt.rcParams['figure.figsize'] = (16,12)

color_dict = ['#0000FF','#FF0000']

plt.rcParams['font.size'] = 20

def open_file(file_name, *args):
    names = []
    for i in args:
        names.append(i)
    df = pd.read_csv(file_name,names=names)
    return df

bm_o = [open_file('OLP_FIELD.csv',"index","x","y", "totalblackout")]

bm_m = [open_file('MLP_FIELD.csv',"index","x","y", "totalblackout")]

bm_s = [open_file('SLP_FIELD.csv',"index","x","y", "totalblackout")]

bm_c = [open_file('CLP_FIELD.csv',"index","x","y", "totalblackout")]

xn = 90
temp_o = np.zeros((int(xn),int(xn)))
temp_m = np.zeros((int(xn),int(xn)))
temp_s = np.zeros((int(xn),int(xn)))
temp_c = np.zeros((int(xn),int(xn)))

for i in bm_o[0]["index"]:
    temp_o[bm_o[0]["y"][i],bm_o[0]["x"][i]] = (bm_o[0]["totalblackout"][i] * 5 / 60)

for i in bm_m[0]["index"]:
    temp_m[bm_m[0]["y"][i],bm_m[0]["x"][i]] = (bm_m[0]["totalblackout"][i] * 5 / 60)

for i in bm_s[0]["index"]:
    temp_s[bm_s[0]["y"][i],bm_s[0]["x"][i]] = (bm_s[0]["totalblackout"][i] * 5 / 60)

for i in bm_c[0]["index"]:
    temp_c[bm_c[0]["y"][i],bm_c[0]["x"][i]] = (bm_c[0]["totalblackout"][i] * 5 / 60)

# plt.pcolor(temp)
# plt.colorbar()
viridis = cm.get_cmap('brg', 256)
newcolors = viridis(np.linspace(1, 0.5, 256))
white = np.array([0, 0, 0, 0])
newcolors[:1, :] = white
newcmp = ListedColormap(newcolors)

figure, ((ax1,ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
plt.suptitle("Blackout time heatmap (Hours)", fontsize=30)

sns.heatmap(temp_o, cmap=newcmp, ax= ax1,vmin=0, vmax=500)
cbar = ax1.collections[0].colorbar
cbar.set_ticks([0,100,200,300,400,500])

viridis = cm.get_cmap('brg', 256)
newcolors = viridis(np.linspace(1, 0.5, 256))
white = np.array([0, 0, 0, 0])
newcolors[:1, :] = white
newcmp = ListedColormap(newcolors)


sns.heatmap(temp_m, cmap=newcmp, ax= ax2,vmin=0, vmax=500)
cbar = ax2.collections[0].colorbar
cbar.set_ticks([0,100,200,300,400,500])

viridis = cm.get_cmap('brg', 256)
newcolors = viridis(np.linspace(1, 0.5, 256))
white = np.array([0, 0, 0, 0])
newcolors[:1, :] = white
newcmp = ListedColormap(newcolors)


sns.heatmap(temp_s, cmap=newcmp, ax= ax3,vmin=0, vmax=500)
cbar = ax3.collections[0].colorbar
cbar.set_ticks([0,100,200,300,400,500])

viridis = cm.get_cmap('brg', 256)
newcolors = viridis(np.linspace(1, 0.5, 256))
white = np.array([0, 0, 0, 0])
newcolors[:1, :] = white
newcmp = ListedColormap(newcolors)

sns.heatmap(temp_c, cmap=newcmp, ax= ax4,vmin=0, vmax=500)
cbar = ax4.collections[0].colorbar
cbar.set_ticks([0,100,200,300,400,500])

for_yticks = []

for i in range(0,xn+10,10):
    for_yticks.append(i)

# plt.yticks([i for i in range(0,xn+10,10)],for_yticks)

for_xticks = []
for i in range(0,xn+10,10):
    if i == 0:
        for_xticks.append("")
    else:
        for_xticks.append(i)

# plt.xticks([i for i in range(0,xn+10,10)], for_xtick)

# plt.xlabel('x field size', labelpad=10)
# plt.ylabel('y field size', labelpad=10)

ax1.set(title="LBDD", yticks=[i for i in range(0,xn+10,10)], yticklabels=for_yticks, xticks=[i for i in range(0,xn+10,10)],xticklabels=for_xticks)
ax2.set(title="Proposed scheme", yticks=[i for i in range(0,xn+10,10)],yticklabels=for_yticks, xticks=[i for i in range(0,xn+10,10)],xticklabels=for_xticks)
ax3.set(title="Single Line shift", yticks=[i for i in range(0,xn+10,10)],yticklabels=for_yticks, xticks=[i for i in range(0,xn+10,10)],xticklabels=for_xticks)
ax4.set(title="LARCMS",yticks=[i for i in range(0,xn+10,10)],yticklabels=for_yticks, xticks=[i for i in range(0,xn+10,10)],xticklabels=for_xticks)

plt.savefig('BLACKOUT_M1.png',bbox_inches='tight')
plt.savefig('BLACKOUT_M1.pdf',bbox_inches='tight')

plt.show()
