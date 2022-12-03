#!/usr/bin/env python3
import pybgpstream
import csv

#Parameters
start_year = 2022
end_year = 2022
day_time_string_1 = "-08-31 07:00:00"
day_time_string_2 = "-08-31 09:00:00"
collector = "rrc00"
recordType = "ribs"

#Loading stub AS that have at least 2 providers
f_data = open("src/data/stubASProvider.txt", "r")
stub_as_provider = set()

for as_stub in f_data:
    as_number = as_stub.split(",")[0]
    stub_as_provider.add(as_number)

f_data.close()

f_output = open("src/output/multiple_provider_" +collector+"_"+str(start_year)+"_"+str(end_year)+".csv","w")
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
    )

    as_list = set()
    as_prepend_list = set()
    entries_count = 0

    for elem in stream:
        entries_count += 1
        as_path = elem.fields["as-path"].split(" ")
        as_number = as_path[-1]

        if as_number in stub_as_provider:
            as_list.add(as_number)

            if len(as_path) > 1 and as_path[-2] == as_number:
                as_prepend_list.add(as_number)
                
        
        if (entries_count % 100000) == 0 :
            print(f'{entries_count} entries have been processed')

    as_count = len(as_list)
    as_prepend_count = len(as_prepend_list)

    writer.writerow([year, as_count, as_prepend_count])
    results[str(year)] ={"Total AS": as_count, "Total AS prepend": as_prepend_count}

    print(f'{as_count} AS with at least 2 providers have been found')
    print(f'{as_prepend_count} AS among them use prepending')

f_output.close()
print(results)


