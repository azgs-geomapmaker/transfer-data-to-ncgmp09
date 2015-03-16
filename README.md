### transfer-data-to-ncgmp09
========================

python script directory for loading data into ncgmp09 schema with field map

scripts used to transfer geologic map data from azgs schema to ncgmp schema

in these scripts, not all fields that are in ncgmp09 schema are accounted for, please refer to NCGMP documentation: http://ngmdb.usgs.gov/Info/standards/NCGMP09/


open each individual script to set environment and data parameters 

In execute-mixed.py change:

  - env.workspace= "C:\\user\\username\\documents\\azgs\\mixed"

Also change inFC and outFC in every script:

  - InFC= "C:\\Users\\ <user name> \\Documents\\azgs\\mixed\\"
  - outFC= "C:\\Users\\ <user name> \\Documents\\ncgmp\\mixed\\"


**Folder Setup**

create two folders ncgmp and azgs
 - inside azgs folder
    - add two folders (mixed and pre-ncgmp)
 - inside ncgmp folder
    - add two folders (mixed and azgs)
 


