# Test file for pybgpstream.py
#!/usr/bin/env python3
import pybgpstream

stream = pybgpstream.BGPStream(
    from_time="2022-08-31 07:50:00", until_time="2022-08-31 08:10:00",
    collectors=["rrc12"],
    record_type="ribs",
)
for elem in stream:
    ases = elem.fields["as-path"].split(" ")
    aslist = []
    count = 0
    if len(ases) > 1:
        for idx, ahess in enumerate(ases):
            if idx < len(ases)-1:
                if ahess==ases[idx+1]:
                    aslist.append(ahess)
                    count+=1
    if count > 0:
        print("--------AS LIST FROM "+ elem.fields["prefix"] +"--------")
        print("Prepending length :" + str(count))
        print(ases)
