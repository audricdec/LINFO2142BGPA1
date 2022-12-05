import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MaxNLocator

ipversion = '6'

df = pd.read_csv('src/output/count_entries_ipv'+ipversion+'_rrc00_2000_2022.csv')
row = df['year']
column = df['prepend_count'] / df['route_count']
print(df)
print(column)

plt.figure(figsize=(10,8))
plt.style.use('seaborn')
plt.title('Proportion of IPV'+ipversion+' RIB entries containing prepending done by stub ASes',fontsize = 18)
plt.xticks(range(2, max(row)+1,2),fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Years',fontsize = 16)
plt.ylabel('Proportion of prepending done by stub ASes',fontsize = 16)
plt.plot(row,column, marker='o')
plt.legend()
plt.savefig('src/graphs/countentriesIPV'+ipversion+'_2002_2022.png',dpi = 100,format='png')
plt.show()
