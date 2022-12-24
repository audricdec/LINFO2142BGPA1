# LINFO2142 - Computer networks : configuration and management : BGPA1 project
**Detection of traffic engineering for stub ASes in BGP routes**\
*Authors : Emile Giot & Audric Deckers*

## Architecture of the project
``` text
src/
├── asrank/             << Contains python scripts to generate jsonl and txt files in data folder  
├── README.md           << Documentation of the project
├── data/               << Contains all the data used in the project
├── graphs/             << Contains all the graphs from the graphsgenerators scripts
├── graphsgenerator/    << Contains all python scripts to generate graphs
├── output/             << Contains all csv files computed by the scripts
└── scripts/
    ├── asAnalysis.py      
    ├── countEntries.py 
    ├── granularityAnalysis.py 
    ├── multipleProvider.py   
    └── prependingLength.py
```

## How to use our scripts 
Each of our scripts are executable and our results are reproducible. This can be done using the following generic command, at the root of the project:
```bash
python3 src/scripts/scriptname.py
```