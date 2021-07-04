#library
import csv
import pandas
import numpy as np
import json

#import data
drugs = pandas.read_csv(r"drugs.csv")
clinical_trials = pandas.read_csv(r"clinical_trials.csv")
pubmed = pandas.read_csv(r"pubmed.csv")

#program
def listWhereTheWordAppearInColFromDataFrame(word,dataFrame,nomCol):
    endList=[]
    for i in range (np.size(dataFrame[nomCol])):
        if word.upper() in dataFrame[nomCol][i].upper():
            listAdd=dataFrame.loc[i][1:np.size(pubmed.loc[i])]
            endList+=[list(listAdd.values)]
    return (endList)

#main
essentiel={}
essentiel['Drug']=[]
for nomDrug in drugs["drug"]:
    ligne=[nomDrug]
    listMentionPubMed=listWhereTheWordAppearInColFromDataFrame(nomDrug,pubmed,"title")
    listInScientificTitle=listWhereTheWordAppearInColFromDataFrame(nomDrug,clinical_trials,"scientific_title")
    essentiel['Drug'].append({
        'name':nomDrug,
        'mentionPubMed':listMentionPubMed,
        'publicationScientifique':listInScientificTitle
    })

# to json
with open('data pipelineA.json', 'w') as outfile:
    json.dump(essentiel, outfile,indent=4)