#library
import csv
import pandas
import numpy as np
import json
from collections import Counter

#import data
with open('data pipeline.json') as json_file:
    data = json.load(json_file)

a=data['Drug']
journauxByDrug=[]
for i in a:
    journauxForOneDrug=[]
    for j in (i['mentionPubMed']):
        if j[2] not in journauxForOneDrug:
            journauxForOneDrug.append(j[2])
    for j in (i['publicationScientifique']):
        if j[2] not in journauxForOneDrug:
            journauxForOneDrug.append(j[2])
    journauxByDrug+=journauxForOneDrug

#class by number of itération
print ((Counter(journauxByDrug)).most_common()[0][0])
