#!/usr/bin/env python3
import pybgpstream
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 17800000 have been processed IPV4 & IPV6 "2022-08-31 07:50:00", until_time="2022-08-31 08:10:00"
# 18100000 have been processed "2021-08-31 07:50:00", until_time="2021-08-31 08:10:00"

start_year = 2000
end_year = 2022
day_time_string_1 = "-08-31 07:00:00"
day_time_string_2 = "-08-31 09:00:00"
collector = "rrc00"
recordType = "ribs"

f = open("/Users/audricdeckers/Desktop/LINFO2142 - Computer Networks/LINFO2142BGPA1/src/output/YT_prepend_proportion_"
+ collector+"_"+str(start_year)+"_"+str(end_year)+".csv", "w")
writer = csv.writer(f)
header = ['year', 'route_count', 'prepend_count', 'prepend_lengths', 'prepend_counts']
writer.writerow(header)
results = {}

for year in range(start_year, end_year+1):

    print(f'Processing rib from {year}')

    stream = pybgpstream.BGPStream(
        from_time=str(year)+day_time_string_1, until_time=str(year)+day_time_string_2,
        collectors=[collector],
        record_type=recordType
    )
    route_count = 0
    route_prepend = 0
    prepend_dict = {}

    for elem in stream:
        as_path = elem.fields["as-path"].split(" ")
        route_count += 1
        i = 1
        prepend_length = 0
        contain_prepending = False
        goNext = False
        while goNext == False:
            if len(as_path) > i:
                j = i
                while as_path[-j - 1] == as_path[-j]:  # check prepending done by the stub AS
                    contain_prepending = True
                    prepend_length += 1
                    j += 1 
                i+=1
                if  contain_prepending == True:
                    route_prepend += 1
                    prepend_dict[prepend_length] = prepend_dict.get(prepend_length,0) + 1
                    goNext = True
                else:
                    goNext=True
            else:
                goNext = True

        if (route_count % 100000) == 0:
            print(f'{route_count} entries have been processed')
            
    prepend_lenghts, prepend_counts = zip(*prepend_dict.items())

    plt.figure(figsize=(10,8))
    plt.style.use('seaborn')
    plt.title('Length of STUB ASes doing prepending per number doing prepending',fontsize = 16)
    plt.bar(prepend_lenghts, prepend_counts)
    plt.xticks(range(1, max(prepend_lenghts)+1))
    plt.xlabel('Prepending length',fontsize = 12)
    plt.ylabel('Number of STUB ASes doing prepending',fontsize = 12)
    #plt.plot(row3,column3,label = 'route-views.eqix', marker='o')
    plt.legend()
    plt.savefig('prepending1month.png',dpi = 100,format='png')
    plt.show()

    results[str(year)] ={"Total routes": route_count, "Total prepend": route_prepend}
    #fh.write(str(year)+"\n")
    #fh.write(f'Total routes: {route_count}\n')
    #fh.write(f'Total prepend: {route_prepend}\n')
    #fh.write("\n")
    writer.writerow([year, route_count, route_prepend, prepend_lenghts, prepend_counts])


    print(f'{route_count} route entries have been processed')
    print(f'{route_prepend} routes contain prepending in their AS path')

print(results)
f.close()