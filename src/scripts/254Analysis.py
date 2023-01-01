#!/usr/bin/env python3
import pybgpstream
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time 

start = time.time()

#Parameters
year = 2022
day_time_string_1 = "-15 07:00:00"
day_time_string_2 = "-15 09:00:00"
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
collector = "rrc00"
recordType = "ribs"
ipversion = "4"
as_to_analyse = '51196'

f = open("src/output/254Analysis"+"_ipv"+ipversion+"_"+collector+"_"+str(year)+"_"+str(year)+".csv", "w")
writer = csv.writer(f)
header = ['month', 'route_count', 'prepend_count', 'prepend_lengths', 'prepend_counts']
writer.writerow(header)
results = {}

for month in months:    

    print(f'Processing rib from {year}, {month}')

    stream = pybgpstream.BGPStream(
        from_time=str(year)+"-"+month+day_time_string_1, until_time=str(year)+"-"+month+day_time_string_2,
        collectors=[collector],
        record_type=recordType,
        filter = "ipversion "+ipversion

    )
    route_count = 0
    route_prepend = 0
    prepend_dict = {}

    for elem in stream:
        as_path = elem.fields["as-path"].split(" ")
        route_count += 1

        if as_path[-1] == as_to_analyse:
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
                    print(f'Prepending of length {prepend_length}')
                    print(as_path)
                    print(elem.fields["prefix"])
                    if  contain_prepending == True:
                        route_prepend += 1
                        prepend_dict[prepend_length] = prepend_dict.get(prepend_length,0) + 1
                        goNext = True
                    else:
                        goNext=True
                else:
                    goNext = True

        if (route_count % 10000000) == 0:
            print(f'{route_count} entries have been processed')
            
    prepend_lenghts, prepend_counts = zip(*prepend_dict.items())

    results[str(month)] ={"Total routes": route_count, "Total prepend": route_prepend}
    #fh.write(str(year)+"\n")
    #fh.write(f'Total routes: {route_count}\n')
    #fh.write(f'Total prepend: {route_prepend}\n')
    #fh.write("\n")
    writer.writerow([month, route_count, route_prepend, prepend_lenghts, prepend_counts])


    print(f'{route_count} route entries have been processed')
    print(f'{route_prepend} routes contain prepending in their AS path')

end = time.time()
print(results)
timestamp = end-start
print(f'{timestamp} s needed to compute prepending length')
f.close()