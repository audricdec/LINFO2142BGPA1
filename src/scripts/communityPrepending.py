#!/usr/bin/env python3
import pybgpstream
import csv
import time 

start = time.time()
#Parameters
start_year = 2022
end_year = 2022
day_time_string_1 = "-05-15 07:00:00"
day_time_string_2 = "-05-15 09:00:00"
collector = "rrc00"
recordType = "ribs"
ipversion = "4"

#NTT
target_communities = {'2914:411', '2914:412', '2914:413', '2914:421', '2914:422', '2914:423'}
target_as = "2914"
as_name = "ntt"

#Cogent
#target_communities = {'174:3001', '174:3002', '174:3003'}
#target_as = "174"
#as_name = "cogent"

f_output = open("src/output/community_prepending_"+as_name+"_"+"ipv"+ipversion+"_"+collector+"_"+str(start_year)+"_"+str(end_year)+".csv","w")
writer = csv.writer(f_output)
header = ['year', 'community_count', 'correct_prepend_count']
writer.writerow(header)
results = {}

for year in range(start_year, end_year+1):
    stream = pybgpstream.BGPStream(
            from_time=str(year)+day_time_string_1, until_time=str(year)+day_time_string_2,
            collectors=[collector],
            record_type=recordType,
            filter = "ipversion "+ipversion
        )

    entries_count = 0
    target_found = 0
    correct_target_found = 0

    for elem in stream:
        entries_count += 1

        if "communities" in elem.fields:
            communities = elem.fields["communities"]
            intersec = target_communities.intersection(communities)

            if len(intersec) > 0:
                #print("\n")
                #print('---------------------')
                #print('There was a hit !')
                #print(communities)
                #print(elem.fields["prefix"])
                #print(elem.fields["as-path"])
                #print("\n")
                target_found += 1
                as_path = elem.fields["as-path"].split(" ")

                if target_as in as_path:
                    correct_target_found += 1
                    print("\n")
                    print('---------------------')
                    print('There was a hit !')
                    print(communities)
                    print(elem.fields["prefix"])
                    print(elem.fields["as-path"])
                    print("\n")

        if (entries_count % 100000) == 0 :
            print(f'{entries_count} entries have been processed')

    results[str(year)] ={"Total communities found": target_found, "Total correct prepend": correct_target_found}
    writer.writerow([year, target_found, correct_target_found])

print(results)
f_output.close()