import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import numpy as np

import inputData as id

# matplotlib 폰트설정
# fontprop = fm.FontProperties(fname="Times New Roman 400.ttf")

X = [800,1000,1200]

# ys, xs, patches = plt.hist(X, bins=3, range=(800,1400), weights=OLP_b, histtype='bar',rwidth=0.8)
# print(ys, xs, patches)
# plt.xticks([(xs[i]+xs[i+1])/2 for i in range(0, len(xs)-1)],
#            ["{}".format(xs[i]) for i in range(0, len(xs)-1)])
# plt.xlabel('전체 노드 수', fontproperties=fontprop, labelpad=10)
# plt.ylabel('전체 블랙 아웃 시간', fontproperties=fontprop, labelpad=10)


# df_o_total = []
# for i in id.df_o:
#     df_o_total.append(id.total_data(i,'blackout'))
# df_o = [np.mean(np.array(df_o_total[0:5])),np.mean(np.array(df_o_total[5:10])),np.mean(np.array(df_o_total[10:15]))]
#
# df_m_total = []
# for i in id.df_m:
#     df_m_total.append(id.total_data(i,'blackout'))
# df_m = [np.mean(np.array(df_m_total[0:5])),np.mean(np.array(df_m_total[5:10])),np.mean(np.array(df_m_total[10:15]))]
#
# B_data = np.array([[df_o[0] * 10 / 60,df_m[0] * 10 / 60],
#                   [df_o[1] * 10 / 60, df_m[1] * 10 / 60],
#                   [df_o[2] * 10 / 60, df_m[2] * 10 / 60]])
#
# diffrence_800 = abs(B_data[0][0] - B_data[0][1]) / B_data[0][0] * 100
# diffrence_1000 = abs(B_data[1][0] - B_data[1][1]) / B_data[1][0] * 100
# diffrence_1200 = abs(B_data[2][0] - B_data[2][1]) / B_data[2][0] * 100
# print(diffrence_800)
# print(diffrence_1000)
# print(diffrence_1200)
#
# df_B = pd.DataFrame(data=B_data ,index=[format(i,",") for i in X], columns=('LBDD','Proposed scheme'))
#
# fig1 = df_B.plot(kind='bar',color=[id.color_dict[0],id.color_dict[1]], edgecolor="black")
#
# plt.xlabel('Number of nodes', labelpad=10)
# plt.xticks(rotation=360)
# plt.ylabel('Total blackout time (Hours)', labelpad=10)
# plt.yticks([0,5000,10000,15000,20000,25000,30000,35000],[format(i,",") for i in [0,5000,10000,15000,20000,25000,30000,35000]])
#
# plt.subplots_adjust(left=0.15)
# # fig.set_size_inches(forward=True)
# ax = plt.gca()
# ax.tick_params(which='major', direction='in', length = 7)
# plt.savefig('totalblackout.png',bbox_inches='tight')
# plt.show()

# df_o_total = []
# for i in id.df_o:
#     df_o_total.append(id.total_data(i,'sink'))
# df_o = [np.mean(np.array(df_o_total[0:5])),np.mean(np.array(df_o_total[5:10])),np.mean(np.array(df_o_total[10:15]))]



# df_m_total = []
# for i in id.df_m:
#     df_m_total.append(id.total_data(i,'sink'))
# df_m = [np.mean(np.array(df_m_total[0:5])),np.mean(np.array(df_m_total[5:10])),np.mean(np.array(df_m_total[10:15]))]

df_o_total = []
for i in id.df_o:
    df_o_total.append(id.total_data(i,'blackout'))
df_o = [np.mean(np.array(df_o_total[0:5])),np.mean(np.array(df_o_total[5:10])),np.mean(np.array(df_o_total[10:15]))]

df_m_total = []
for i in id.df_m:
    df_m_total.append(id.total_data(i,'blackout'))
df_m = [np.mean(np.array(df_m_total[0:5])),np.mean(np.array(df_m_total[5:10])),np.mean(np.array(df_m_total[10:15]))]

df_s_total = []
for i in id.df_s:
    df_s_total.append(id.total_data(i,'blackout'))
df_s = [np.mean(np.array(df_s_total[0:5])),np.mean(np.array(df_s_total[5:10])),np.mean(np.array(df_s_total[10:15]))]

df_c_total = []
for i in id.df_c:
    df_c_total.append(id.total_data(i,'blackout'))
df_c = [np.mean(np.array(df_c_total[0:5])),np.mean(np.array(df_c_total[5:10])),np.mean(np.array(df_c_total[10:15]))]

B_data = np.array([[df_o[0] * 5 / 60,df_s[0] * 5 / 60, df_c[0] * 5 / 60,df_m[0] * 5 / 60],
                  [df_o[1] * 5 / 60,df_s[1] * 5 / 60, df_c[1] * 5 / 60,df_m[1] * 5 / 60],
                  [df_o[2] * 5 / 60,df_s[2] * 5 / 60, df_c[2] * 5 / 60,df_m[2] * 5 / 60]])

print(B_data)
# diffrence_800 = abs(S_data[0][0] - S_data[0][1]) / S_data[0][0] * 100
# diffrence_1000 = abs(S_data[1][0] - S_data[1][1]) / S_data[1][0] * 100
# diffrence_1200 = abs(S_data[2][0] - S_data[2][1]) / S_data[2][0] * 100
# print(diffrence_800)
# print(diffrence_1000)
# print(diffrence_1200)

# df_S = pd.DataFrame(data=S_data, index=('LBDD','Line Shift', 'LARCMS', 'Proposed scheme'), index=range(0,1))
df_B = pd.DataFrame(data=B_data,index=[format(800),format(1000),format(1200)], columns=('LBDD','Single Line shift', 'LARCMS','Proposed scheme'))

fig2 = df_B.plot(kind='bar',color=[id.color_dict[0],id.color_dict[1],id.color_dict[2],id.color_dict[3]], edgecolor="black")

# fig2 = df_S.plot(kind='bar',color=[id.color_dict[0],id.color_dict[1]], edgecolor="black")
plt.xlabel('Number of nodes', labelpad=10)
plt.ylabel('Total blackout time (Hours)', labelpad=10)
plt.xticks(rotation=360)
plt.yticks([i for i in np.arange(0,max(map(max, B_data))+5000, 50000)],[i if i < 10000 else format(i,",") for i in np.arange(0,int(max(map(max, B_data))+5000), 50000)])

plt.subplots_adjust(left=0.15)

ax = plt.gca()
ax.tick_params(which='major', direction='in', length = 7)
plt.savefig('totalblackoutdata.png',bbox_inches='tight')
plt.savefig('totalblackoutdata.pdf',bbox_inches='tight')
plt.show()


