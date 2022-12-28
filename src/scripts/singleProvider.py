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
ipversion = "6"
# + 15-May-2002 10:32 IPV4: 2002,5820,915 IPV6 : 2002, 0, 0

#Loading stub AS that at least 2 providers
f_data = open("src/data/stubASProvider.txt", "r")
stub_as_provider = set()

for as_stub in f_data:
    as_number = as_stub.split(",")[0]
    stub_as_provider.add(as_number)

f_data.close()

f_data_all = open("src/data/stubAS.txt", "r")
stub_as_single_provider = set()

#Computing stub AS that have a single provider
for as_stub in f_data_all:
    if as_stub.rstrip("\n") not in stub_as_provider:
        stub_as_single_provider.add(as_stub.rstrip("\n"))

f_data_all.close()

print(len(stub_as_single_provider))

f_output = open("src/output/single_provider_"+"ipv"+ipversion+"_"+collector+"_"+str(start_year)+"_"+str(end_year)+".csv","w")
writer = csv.writer(f_output)
header = ['year', 'as_count', 'prepend_count']
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

    as_list = set()
    as_prepend_list = set()
    entries_count = 0

    for elem in stream:
        entries_count += 1
        as_path = elem.fields["as-path"].split(" ")
        as_number = as_path[-1]

        if as_number in stub_as_single_provider:
            as_list.add(as_number)

            if len(as_path) > 1 and as_path[-2] == as_number:
                as_prepend_list.add(as_number)
                
        
        if (entries_count % 100000) == 0 :
            print(f'{entries_count} entries have been processed')

    as_count = len(as_list)
    as_prepend_count = len(as_prepend_list)

    writer.writerow([year, as_count, as_prepend_count])
    results[str(year)] ={"Total AS": as_count, "Total AS prepend": as_prepend_count}

    print(f'{as_count} AS with single provider have been found')
    print(f'{as_prepend_count} AS among them use prepending')

f_output.close()
end = time.time()
print(results)
timestamp = end-start
print(f'{timestamp} s needed to compute single provider')


