import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MaxNLocator

ipversion = '6'

df = pd.read_csv('src/output/single_provider_ipv'+ipversion+'_rrc00_2002_2022.csv')
row = df['year']
column = df['prepend_count'] / df['as_count']
print(df)
print(column)

plt.figure(figsize=(10,8))
plt.style.use('seaborn')
plt.title('Proportion of stub ASes with a single provider doing prepending in IPV'+ipversion+'',fontsize = 18)
plt.xticks(range(2, max(row)+1,2),fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Years',fontsize = 18)
plt.ylabel('Proportion of stub ASes doing prepending',fontsize = 18)
plt.plot(row,column, marker='o')
plt.legend()
plt.savefig('src/graphs/singleproviderIPV'+ipversion+'_2002_2022.png',dpi = 100,format='png')
plt.show()
