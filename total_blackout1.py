import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import numpy as np

# import inputData as id

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

df_o = open_file('OLP600_10_5.csv',"index","blackout","sink","canttransmit")
df_o_total = total_data(df_o,'blackout')
df_o_total_ct = total_data(df_o,"canttransmit")

df_m = open_file('MLP600_10_5.csv',"index","blackout","sink","canttransmit")
df_m_total = total_data(df_m,'blackout')
df_m_total_ct = total_data(df_m,"canttransmit")

df_s = open_file('SLP600_10_5.csv',"index","blackout","sink","canttransmit")
df_s_total = total_data(df_s,'blackout')
df_s_total_ct = total_data(df_s,"canttransmit")

df_c = open_file('CLP600_10_5.csv',"index","blackout","sink","canttransmit")
df_c_total = total_data(df_c,'blackout')
df_c_total_ct = total_data(df_c,"canttransmit")

# df_m_total = []
# for i in id.df_m:
#     df_m_total.append(id.total_data(i,'sink'))
# df_m = [np.mean(np.array(df_m_total[0:5])),np.mean(np.array(df_m_total[5:10])),np.mean(np.array(df_m_total[10:15]))]

S_data = np.array([df_o_total* 5 / 60 , df_s_total* 5 / 60, df_c_total* 5 / 60, df_m_total* 5 / 60])
# S_data_ct = np.array([df_o_total_ct* 5 / 60 , df_s_total_ct* 5 / 60, df_c_total_ct* 5 / 60, df_m_total_ct* 5 / 60])
# diffrence_800 = abs(S_data[0][0] - S_data[0][1]) / S_data[0][0] * 100
# diffrence_1000 = abs(S_data[1][0] - S_data[1][1]) / S_data[1][0] * 100
# diffrence_1200 = abs(S_data[2][0] - S_data[2][1]) / S_data[2][0] * 100
# print(diffrence_800)
# print(diffrence_1000)
# print(diffrence_1200)

data = {'blackout': S_data,
        # 'canttransmit': S_data_ct,
        'index' : ['LBDD','Line Shift', 'LARCMS', 'Proposed scheme']}
print(data)
# df_S = pd.DataFrame(data=S_data, index=('LBDD','Line Shift', 'LARCMS', 'Proposed scheme'), index=range(0,1))
df_S = pd.DataFrame(data=S_data, index=('LBDD','Line Shift', 'LARCMS', 'Proposed scheme'))
# df_S_ct = pd.DataFrame(data=S_data_ct, index=('LBDD','Line Shift', 'LARCMS', 'Proposed scheme'))
# fig2 = df_S.plot(kind='bar',color=[id.color_dict[0],id.color_dict[1]], edgecolor="black")

p1 = plt.bar(data['index'], data['blackout'], color='b')
# p2 = plt.bar(data['index'], data['canttransmit'], color='r', bottom=data['blackout'])
# plt.legend((p1[0],p2[0]),('blackout','canttransmit'))
# df_S.plot(kind='bar', stacked=True,legend=False)
# df_S_ct.plot(kind='bar', stacked=True,legend=False, bottom=data.canttransmit)

plt.xlabel('Number of nodes', labelpad=10)
# plt.ylabel('Amount of gathered data at the sink (MB)', labelpad=10)
plt.xticks(rotation=360)
plt.ylabel('Total blackout time (Hours)', labelpad=10)
# plt.yticks([0,5000,10000,15000,20000,25000,30000,35000],[format(i,",") for i in [0,5000,10000,15000,20000,25000,30000,35000]])

plt.subplots_adjust(left=0.15)

ax = plt.gca()
ax.tick_params(which='major', direction='in', length = 7)
plt.savefig('totalblackoutdata.png',bbox_inches='tight')
plt.savefig('totalblackoutdata.pdf',bbox_inches='tight')
plt.show()


