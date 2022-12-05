import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Loading stub AS that have at least 2 providers
f_data = open("src/data/stubASProvider.txt", "r")
provider_dict = {}

for as_stub in f_data:
    nb_provider = int(as_stub.split(",")[1])
    if nb_provider == 69:
        print(as_stub.split(",")[0])
    # if(nb_provider) < 10:
    provider_dict[nb_provider] = provider_dict.get(nb_provider,0) + 1
    # else: 
    #     provider_dict[10] = provider_dict.get(10,0) + 1

f_data.close()

provider_dict[1] = 101026 - 33830
row, column = zip(*provider_dict.items())

print(row, column)

# plt.figure(figsize=(10,8))
# plt.style.use('seaborn')
# plt.xticks(range(1, max(row)+1),fontsize=15)
# plt.yticks(fontsize=15)
# plt.title('Number of providers for stub ASes in 2022',fontsize = 18)
# plt.xlabel('Number of providers',fontsize = 18)
# plt.ylabel('Number of stub ASes',fontsize = 18)
# plt.bar(row,column)
# plt.legend()
# for x,y in zip(row,column):

#     label = "{:}".format(y)

#     plt.annotate(label, # this is the text
#                  (x,y), # these are the coordinates to position the label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  fontsize=15,
#                  ha='center') # horizontal alignment can be left, right or center
# plt.savefig('src/graphs/providersStubASes2022.png',dpi = 100,format='png')
# plt.show()
