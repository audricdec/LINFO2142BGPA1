import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter

df = pd.read_csv('src/output/prepend_proportion_route-views.eqix_2002_2022.csv')
row = df['year']
column = df['prepend_count'] / df['route_count']

print(df)
print(column)

df2 = pd.read_csv('src/output/prepend_proportion_rrc00_2000_2022.csv')
row2 = df2['year']
column2 = df2['prepend_count'] / df2['route_count']
print(df2)
print(column2)

# dfPropLength = pd.read_csv('src/output/prepend_proportion_rrc00_2000_2000.csv')
# row3 = list(dfPropLength['prepend_lengths'][0])
# column3 = list(dfPropLength['prepend_counts'][0])
# print(dfPropLength)
# print(row3)
# print(column3)

# def smooth(y, box_pts):
#     box = np.ones(box_pts)/box_pts
#     y_smooth = np.convolve(y, box, mode='same')
#     return y_smooth

plt.figure(figsize=(10,8))
plt.style.use('seaborn-whitegrid')
plt.title('Proportion of STUB ASes doing prepending between 2002 and 2022',fontsize = 16)
plt.xlabel('Years',fontsize = 12)
plt.ylabel('Proportion of prepending',fontsize = 12)
plt.plot(row,savgol_filter(column,15,5),label = 'route-views.eqix', marker='o')
plt.plot(row2,savgol_filter(column2,15,5),label = 'rrc00', marker='o')
plt.legend()
plt.savefig('prependingSmooth.png',dpi = 100,format='png')
plt.show()

# plt.figure(figsize=(10,8))
# plt.style.use('seaborn')
# plt.title('STUB ASes doing prepending Length vs Count',fontsize = 16)
# plt.bar(row3, column3)
# #plt.xticks(range(1, max(row3)+1))
# plt.xlabel('Length',fontsize = 12)
# plt.ylabel('Count',fontsize = 12)
# #plt.plot(row3,column3,label = 'route-views.eqix', marker='o')
# plt.legend()
# #plt.savefig('prepending2000LC.png',dpi = 100,format='png')
# plt.show()

#df.plot(kind='line', x='year', y= 'prepend_count')
# years = np.arange(2009,2022+1)
# p2009 = 118119 / 1463944
# p2010 = 310882 / 3602743
# p2011 = 393006 / 4052269
# p2012 = 497032 / 5099788
# p2013 = 670866 / 6576419
# p2014 = 718419 / 7262000
# p2015 = 655609 /6555708
# p2016 = 771321/ 7526639
# p2017 = 848164 / 8237780
# p2018 = 1098317 / 10594045
# p2019 = 1172528 / 10788005
# p2020 = 1538480 / 13381370
# p2021 = 1999019 / 18118692
# p2022 = 1922340 / 17890276
# prep = [p2009, p2010, p2011, p2012, p2013, p2014, p2015, p2016, p2017, p2018, p2019, p2020, p2021, p2022]
# plt.plot(years, prep)
# plt.show()