#!/usr/bin/env python3
import pybgpstream
import csv

# 17800000 have been processed IPV4 & IPV6 "2022-08-31 07:50:00", until_time="2022-08-31 08:10:00"
# 18100000 have been processed "2021-08-31 07:50:00", until_time="2021-08-31 08:10:00"

start_year = 2000
end_year = 2022
day_time_string_1 = "-08-31 07:00:00"
day_time_string_2 = "-08-31 18:00:00"
collector = "rrc00"
recordType = "ribs"

f = open("/Users/audricdeckers/Desktop/LINFO2142 - Computer Networks/LINFO2142BGPA1/src/output/prepend_proportion_" \
+collector+"_"+str(start_year)+"_"+str(end_year)+".csv","w")
writer = csv.writer(f)
header = ['year', 'route_count', 'prepend_count']
writer.writerow(header)
results = {}

for year in range(start_year, end_year+1):

    print(f'Processing rib from {year}')

    stream = pybgpstream.BGPStream(
        from_time=str(year)+day_time_string_1, until_time=str(year)+day_time_string_2,
        collectors=[collector],
        record_type=recordType,
        filter="aspath _36040$"
    )
    route_count = 0 
    route_prepend = 0

    for elem in stream:
        as_path = elem.fields["as-path"].split(" ")
        route_count += 1
        
        if len(as_path) > 1:

            if(as_path[-2] == as_path[-1]): # check prepending done by the stub AS
                route_prepend += 1
                
        if (route_count % 100000) == 0 :
            print(f'{route_count} entries have been processed')

    results[str(year)] ={"Total routes": route_count, "Total prepend": route_prepend}
    writer.writerow([year, route_count, route_prepend])


    print(f'{route_count} route entries have been processed')
    print(f'{route_prepend} routes contain prepending in their AS path')

print(results)
f.close()