#!/usr/bin/env python3
import pybgpstream
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time 

start = time.time()

#Loading stub AS based on https://asrank.caida.org/
f_data = open("src/data/stubAS.txt", "r")
stub_as = set()

for as_stub in f_data:
    stub_as.add(as_stub.rstrip("\n"))

f_data.close()

#Parameter
start_year = 2022
end_year = 2022
day_time_string_1 = "-05-15 07:00:00"
day_time_string_2 = "-05-15 09:00:00"
collector = "rrc00"
recordType = "ribs"
ipversion = "4"

f = open("src/output/prepending_length_"+"ANALYSEROUTE_ipv"+ipversion+"_"+collector+"_"+str(start_year)+"_"+str(end_year)+".csv", "w")
writer = csv.writer(f)
header = ['year', 'route_count', 'prepend_count', 'prepend_lengths', 'prepend_counts']
writer.writerow(header)
results = {}

for year in range(start_year, end_year+1):

    print(f'Processing rib from {year}')

    stream = pybgpstream.BGPStream(
        from_time=str(year)+day_time_string_1, until_time=str(year)+day_time_string_2,
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

        if as_path[-1] in stub_as:
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
                    if(prepend_length > 48):
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

        if (route_count % 100000) == 0:
            print(f'{route_count} entries have been processed')
            
    prepend_lenghts, prepend_counts = zip(*prepend_dict.items())

    results[str(year)] ={"Total routes": route_count, "Total prepend": route_prepend}
    #fh.write(str(year)+"\n")
    #fh.write(f'Total routes: {route_count}\n')
    #fh.write(f'Total prepend: {route_prepend}\n')
    #fh.write("\n")
    writer.writerow([year, route_count, route_prepend, prepend_lenghts, prepend_counts])


    print(f'{route_count} route entries have been processed')
    print(f'{route_prepend} routes contain prepending in their AS path')

end = time.time()
print(results)
timestamp = end-start
print(f'{timestamp} s needed to compute prepending length')
f.close()