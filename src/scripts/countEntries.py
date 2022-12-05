#!/usr/bin/env python3
import pybgpstream
import csv
import time 

start = time.time()
#Parameters
start_year = 2002
end_year = 2022
day_time_string_1 = "-05-15 07:00:00"
day_time_string_2 = "-05-15 09:00:00"
collector = "rrc00"
recordType = "ribs"
ipversion = "4"

# + 15-May-2002 10:32 IPV4: 2002,638475,38226 IPV6 : 2002, 0, 0

#Loading stub AS based on https://asrank.caida.org/
f_data = open("src/data/stubAS.txt", "r")
stub_as = set()

for as_stub in f_data:
    stub_as.add(as_stub.rstrip("\n"))

f_data.close()

f_output = open("src/output/count_entries_"+"ipv"+ipversion+"_"+collector+"_"+str(start_year)+"_"+str(end_year)+".csv","w")
writer = csv.writer(f_output)
header = ['year', 'route_count', 'prepend_count']
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
    entries_count = 0
    route_count = 0 
    route_prepend = 0

    for elem in stream:
        as_path = elem.fields["as-path"].split(" ")
        as_number = as_path[-1]
        entries_count += 1

        if as_number in stub_as:
            route_count += 1
        
            if len(as_path) > 1 and as_path[-2] == as_number:
                    route_prepend += 1
                
        if (entries_count % 100000) == 0 :
            print(f'{entries_count} entries have been processed')

    results[str(year)] ={"Total routes": route_count, "Total prepend": route_prepend}
    writer.writerow([year, route_count, route_prepend])


    print(f'{route_count} route entries have been processed')
    print(f'{route_prepend} routes contain prepending in their AS path')

end = time.time()
print(results)
timestamp = end-start
print(f'{timestamp} s needed to compute count entries')
f_output.close()