#!  /usr/bin/env python3
__author__ = "Bradley Huffaker"
__email__ = "<bradley@caida.org>"
# This software is Copyright (C) 2020 The Regents of the University of
# California. All Rights Reserved. Permission to copy, modify, and
# distribute this software and its documentation for educational, research
# and non-profit purposes, without fee, and without a written agreement is
# hereby granted, provided that the above copyright notice, this paragraph
# and the following three paragraphs appear in all copies. Permission to
# make commercial use of this software may be obtained by contacting:
#
# Office of Innovation and Commercialization
#
# 9500 Gilman Drive, Mail Code 0910
#
# University of California
#
# La Jolla, CA 92093-0910
#
# (858) 534-5815
#
# invent@ucsd.edu
#
# This software program and documentation are copyrighted by The Regents of
# the University of California. The software program and documentation are
# supplied â€œas isâ€, without any accompanying services from The Regents. The
# Regents does not warrant that the operation of the program will be
# uninterrupted or error-free. The end-user understands that the program
# was developed for research purposes and is advised not to rely
# exclusively on the program for any reason.
#
# IN NO EVENT SHALL THE UNIVERSITY OF CALIFORNIA BE LIABLE TO ANY PARTY FOR
# DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES,
# INCLUDING LOST PR OFITS, ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS
# DOCUMENTATION, EVEN IF THE UNIVERSITY OF CALIFORNIA HAS BEEN ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE. THE UNIVERSITY OF CALIFORNIA SPECIFICALLY
# DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE
# SOFTWARE PROVIDED HEREUNDER IS ON AN â€œAS ISâ€ BASIS, AND THE UNIVERSITY OF
# CALIFORNIA HAS NO OBLIGATIONS TO PROVIDE MAINTENANCE, SUPPORT, UPDATES,
# ENHANCEMENTS, OR MODIFICATIONS.
#
import json
import requests
import pybgpstream

URL = "https://api.asrank.caida.org/v2/graphql"
decoder = json.JSONDecoder()
encoder = json.JSONEncoder()

def AsnQuery(asn): 
    return """{
        asn(asn:"%i") {
            cone {
                numberAsns
                numberPrefixes
                numberAddresses
            }
            asnDegree {
                provider
                peer
                customer
                total
                transit
                sibling
            }
        }
    }""" % (asn)

year = 2022
day_time_string_1 = "-08-31 07:00:00"
day_time_string_2 = "-08-31 09:00:00"
collector = "rrc00"
recordType = "ribs"

print(f'Processing rib from {year}')

stream = pybgpstream.BGPStream(
    from_time=str(year)+day_time_string_1, until_time=str(year)+day_time_string_2,
    collectors=[collector],
    record_type=recordType,
)

as_list = set()
entries_count = 0

for elem in stream:
    entries_count += 1
    as_path = elem.fields["as-path"].split(" ")

    if len(as_path) > 1:
        if as_path[-1][0]!='{': 
            as_list.add(int(as_path[-1]))
    
    if (entries_count % 100000) == 0 :
        print(f'{entries_count} entries have been processed')

f1 = open("src/data/stubAS.txt","w")
f2 = open("src/data/stubASProvider.txt","w")

print(str(len(as_list))+" AS have been found")
as_count = 0

for as_number in as_list:
    as_count += 1
    query = AsnQuery(as_number)
    request = requests.post(URL,json={'query':query})
    print(as_number)
    
    if request.status_code == 200:
        datas = request.json()
        if datas['data']['asn']['asnDegree']['customer'] == 0: # Check if ASN isSTUB
            f1.write(f'{as_number}\n')
            nb_provider = datas['data']['asn']['asnDegree']['provider']
            if nb_provider > 1:
                f2.write(f'{as_number},{nb_provider}\n')
    
    else:
        print("Query failed to run returned code of %d " % (request.status_code))

    if (as_count % 1000) == 0 :
        print(f'{as_count} entries have been processed')

f1.close()
f2.close()
