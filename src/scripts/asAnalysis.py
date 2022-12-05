#!/usr/bin/env python3
import pybgpstream
import csv

#Parameter
start_year = 2022
end_year = 2022
day_time_string_1 = "-08-31 07:00:00"
day_time_string_2 = "-08-31 09:00:00"
collector = "rrc00"
recordType = "ribs"
as_to_analyse = '21433'

f_output = open("src/output/as_analysis_"+as_to_analyse+"_"+collector+"_"+str(start_year)+"_"+str(end_year)+".csv","w")
writer = csv.writer(f_output)
header = ['year', 'prefix_2_count', 'prepend_2_count']
writer.writerow(header)

for year in range(start_year, end_year+1):

    print(f'Processing rib from {year}')

    stream = pybgpstream.BGPStream(
        from_time=str(year)+day_time_string_1, until_time=str(year)+day_time_string_2,
        collectors=[collector],
        record_type=recordType
    )
    entries_count = 0
    entries_with_prepending = 0
    prefix_with_prepending = 0
    prefix_list = {}
    peer_list = set()

    for elem in stream:
        as_path = elem.fields["as-path"].split(" ")
        entries_count += 1

        if(as_path[-1] == as_to_analyse):
            
            prefix = elem.fields["prefix"]
            peer = None
            prepending = False

            if prefix not in prefix_list:
                prefix_list[prefix] = {}

            if len(as_path) > 1:

                if as_path[-2] == as_to_analyse:
                    prepending = True
                    entries_with_prepending += 1

                i = len(as_path)-2
                while i >= 0 and peer is None:

                    if as_path[i] != as_to_analyse:
                        peer = as_path[i]
                        peer_list.add(peer)

                        if peer not in prefix_list[prefix]:
                            prefix_list[prefix][peer] = prepending

                            if prepending:
                                prefix_with_prepending += 1
                        
                    i -= 1

        if (entries_count % 100000) == 0:
            print(f'{entries_count} entries have been processed')
    
    peer_count = len(peer_list)
    print(year)
    print(f'{peer_count} peers detected')
    print(peer_list)
    print(f'{entries_with_prepending} entries with prepending detected')
    print(f'{prefix_with_prepending} prefix-peer pair with prepending detected')

    prefix_2_count = 0
    prepending_2_count = 0
    for prefix, peer_info in prefix_list.items():
        
        if len(peer_info) >= 2:
            prefix_2_count += 1
            prepend_info = list(peer_info.values())
            i = 0
            prepend_found = False

            while i < len(prepend_info) and prepend_found is False:

                if prepend_info[i] is True:
                    prepend_found = True
                    prepending_2_count += 1
                
                i += 1
    
    writer.writerow([year, prefix_2_count, prepending_2_count])

f_output.close()