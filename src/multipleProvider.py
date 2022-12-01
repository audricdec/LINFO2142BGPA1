#!/usr/bin/env python3
import pybgpstream
import csv

start_year = 2002
end_year = 2022
day_time_string_1 = "-08-31 07:00:00"
day_time_string_2 = "-08-31 09:00:00"
collector = "rrc00"
recordType = "ribs"

f = open("output/multiple_provider_" +collector+"_"+str(start_year)+"_"+str(end_year)+".csv","w")
writer = csv.writer(f)
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

    as_list = {}
    entries_count = 0

    for elem in stream:
        entries_count += 1
        as_path = elem.fields["as-path"].split(" ")

        if len(as_path) > 1:
            as_number = as_path[-1]
                
            #We add the AS to the list if it's the 1st time we encounter it
            if as_number not in as_list:
                as_list[as_number] = {'provider': set(), 'prepend': False}

            #We check for prpending
            if as_path[-2] == as_number:
                as_list[as_number]['prepend'] = True


            i = len(as_path)-2
            provider_found = False

            #We look for the provider
            while i >= 0 and not provider_found:
                if as_path[i] != as_number:
                    provider_found = True
                    as_list[as_number]['provider'].add(as_path[i])

                i -= 1
        
        if (entries_count % 100000) == 0 :
            print(f'{entries_count} entries have been processed')

    as_count = 0
    as_prepend_count = 0

    for as_number, as_info in as_list.items():
        if len(as_info['provider']) >= 2:
            as_count += 1

            if as_info['prepend']:
                as_prepend_count += 1

    writer.writerow([year, as_count, as_prepend_count])
    results[str(year)] ={"Total AS": as_count, "Total AS prepend": as_prepend_count}

    print(f'{as_count} AS with at least 2 providers have been found')
    print(f'{as_prepend_count} AS among them use prepending')

print(results)
f.close()

