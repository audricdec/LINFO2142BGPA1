#!/usr/bin/env python3
#Test file for pybgpstream.py

import pybgpstream

stream = pybgpstream.BGPStream(
    from_time="2015-08-31 07:50:00", until_time="2016-08-31 08:10:00",
    collectors=["rrc21"],
    record_type="ribs",
    #filter="aspath _36040$"
    #filter="aspath _63293$"
)
#filter='path "_18144_"',
for elem in stream:
    #print(elem.fields["prefix"])
    #print(elem.fields["as-path"].split(" "))
    ases = elem.fields["as-path"].split(" ")
    aslist = []
    count = 0
    if len(ases) > 1:
        if(ases[-2]==ases[-1]):
            aslist.append(ases[-1])
            count+=1
        # for idx, ahess in enumerate(ases):
        #     if idx < len(ases)-1:
        #         if ahess==ases[idx+1]:
        #             aslist.append(ahess)
        #             count+=1
    if count > 0:
        print("--------AS LIST FROM "+ elem.fields["prefix"] +"--------")
        print("Prepending length :" + str(count))
        print(ases)

