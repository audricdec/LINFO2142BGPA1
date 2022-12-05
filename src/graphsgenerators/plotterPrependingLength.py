import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MaxNLocator

ipversion = '6'

df = pd.read_csv('src/output/prepending_length_ipv'+ipversion+'_rrc00_2022_2022.csv')
#ipv4 data
if ipversion == '4':
    pre_row = [2, 3, 1, 4, 5, 7, 8, 9, 6, 10, 14, 15, 11, 19, 12, 18, 20, 16, 13, 30, 24, 21, 254, 49, 25, 17, 50]
    pre_column = [463388, 397647, 740586, 194653, 138382, 36502, 25430, 26385, 57082, 22599, 5883, 5624, 9396, 192, 1967, 55, 467, 559, 2031, 9, 221, 11, 3, 34, 53, 39, 20]
else: 
    pre_row = [1, 3, 2, 4, 9, 6, 5, 7, 8, 10, 11, 15, 24, 14, 13, 16, 12]
    pre_column = [72023, 26730, 30039, 11347, 1349, 2639, 7161, 2143, 1285, 306, 1296, 568, 11, 7, 581, 80, 124]
#ipv6 data
row = pre_row[:10]
column = pre_column[:10]
column[9] = column[9] + sum(pre_column[10:])
plt.figure(figsize=(10,8))
plt.style.use('seaborn')
plt.title('Distribution of IPV'+ipversion+' RIB entries containing prepending done by stub ASes by length',fontsize = 18)
plt.xticks(range(2, max(row)+1),fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('Number of IPV'+ipversion+' RIB entries containing prepending',fontsize = 18)
plt.xlabel('Length of prepending',fontsize = 18)
plt.bar(row,column)
plt.legend()
for x,y in zip(row,column):

    label = "{:}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 fontsize=15,
                 ha='center') # horizontal alignment can be left, right or center
plt.savefig('src/graphs/prependinglengthIPV'+ipversion+'_2002_2022.png',dpi = 100,format='png')
plt.show()
