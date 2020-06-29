import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 25
plt.rcParams['figure.figsize'] = (12,9)

color_dict = ['#0000FF','#FF0000']

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

df800_o1 = open_file('OLP800_10_1.csv',"index","blackout","sink")
df1000_o1 = open_file('OLP1000_10_1.csv',"index","blackout","sink")
df1200_o1 = open_file('OLP1200_10_1.csv',"index","blackout","sink")

df800_o2 = open_file('OLP800_10_2.csv',"index","blackout","sink")
df1000_o2 = open_file('OLP1000_10_2.csv',"index","blackout","sink")
df1200_o2 = open_file('OLP1200_10_2.csv',"index","blackout","sink")

df800_o3 = open_file('OLP800_10_3.csv',"index","blackout","sink")
df1000_o3 = open_file('OLP1000_10_3.csv',"index","blackout","sink")
df1200_o3 = open_file('OLP1200_10_3.csv',"index","blackout","sink")

df800_o4 = open_file('OLP800_10_4.csv',"index","blackout","sink")
df1000_o4 = open_file('OLP1000_10_4.csv',"index","blackout","sink")
df1200_o4 = open_file('OLP1200_10_4.csv',"index","blackout","sink")

df800_o5 = open_file('OLP800_10_5.csv',"index","blackout","sink")
df1000_o5 = open_file('OLP1000_10_5.csv',"index","blackout","sink")
df1200_o5 = open_file('OLP1200_10_5.csv',"index","blackout","sink")

df_o = [df800_o1, df800_o2, df800_o3, df800_o4, df800_o5, df1000_o1,df1000_o2,df1000_o3, df1000_o4, df1000_o5, df1200_o1,df1200_o2,df1200_o3, df1200_o4, df1200_o5]

df800_m1 = open_file('MLP800_10_1.csv',"index","blackout","sink")
df1000_m1 = open_file('MLP1000_10_1.csv',"index","blackout","sink")
df1200_m1 = open_file('MLP1200_10_1.csv',"index","blackout","sink")

df800_m2 = open_file('MLP800_10_2.csv',"index","blackout","sink")
df1000_m2 = open_file('MLP1000_10_2.csv',"index","blackout","sink")
df1200_m2 = open_file('MLP1200_10_2.csv',"index","blackout","sink")

df800_m3 = open_file('MLP800_10_3.csv',"index","blackout","sink")
df1000_m3 = open_file('MLP1000_10_3.csv',"index","blackout","sink")
df1200_m3 = open_file('MLP1200_10_3.csv',"index","blackout","sink")

df800_m4 = open_file('MLP800_10_4.csv',"index","blackout","sink")
df1000_m4 = open_file('MLP1000_10_4.csv',"index","blackout","sink")
df1200_m4 = open_file('MLP1200_10_4.csv',"index","blackout","sink")

df800_m5 = open_file('MLP800_10_5.csv',"index","blackout","sink")
df1000_m5 = open_file('MLP1000_10_5.csv',"index","blackout","sink")
df1200_m5 = open_file('MLP1200_10_5.csv',"index","blackout","sink")
df_m = [df800_m1, df800_m2, df800_m3, df800_m4, df800_m5, df1000_m2,df1000_m2,df1000_m2, df1000_m4, df1000_m5, df1200_m1,df1200_m2,df1200_m3, df1200_m4,df1200_m5]



