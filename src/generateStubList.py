#!  /usr/bin/env python3

import json

f_data = open("src/data/asns.jsonl", "r")
f_output1 = open("src/data/stubAS.txt", "w")
f_output2 = open("src/data/stubASProvider.txt", "w")
line_count = 0

for line in f_data:
    current_as = json.loads(line)
    as_number = current_as['asn']

    if current_as['asnDegree']['customer'] == 0:
        f_output1.write(f'{as_number}\n')
        as_provider = current_as['asnDegree']['provider']

        if as_provider >= 2:
            f_output2.write(f'{as_number},{as_provider}\n')
    
    line_count += 1

    if (line_count % 10000) == 0:
        print(f'{line_count} asn have been processed')

f_data.close()
f_output1.close()
f_output2.close()


