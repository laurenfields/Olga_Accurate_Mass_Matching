# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
import pandas as pd

instrument_output_path = r"C:\Users\Olga\Desktop\Mass_Matching\instrument_output.csv"
mass_values_path = r"C:\Users\Olga\Desktop\Mass_Matching\mass_values.csv"
sample_name = 'Amino_acid_mix2' #no spaces or special characters, first character cannot be a number
output_directory = r"C:\Users\Olga\Desktop\Mass_Matching"
difference = 0.1
tags = ['m/z','d3','d6','d9','d12']
#####don't edit beyond here####
print('Analysis initiated')
instrument_output = pd.read_csv(instrument_output_path)
mass_values = pd.read_csv(mass_values_path)


query = instrument_output['m/z'].values.tolist()

tag = []
instrumentout = []
massout = []
for a in tags:
    values_lookup = mass_values[a].values.tolist()

    for b in query:
        for c in values_lookup:
                tag.append(a)
                instrumentout.append(b)
                massout.append(c)

results_store = pd.DataFrame()
results_store['Tag'] = tag
results_store['Instrument output m/z'] = instrumentout
results_store['Mass m/z'] = massout
results_store['difference'] = abs(results_store['Instrument output m/z'] - results_store['Mass m/z'])
results_store = results_store[results_store['difference'] <= difference]
results_store = results_store.drop_duplicates()

merge = results_store.merge(instrument_output, left_on='Instrument output m/z', right_on='m/z')

output_path = output_directory + '\\' + sample_name + '.csv'

with open(output_path,'w',newline='') as filec:
        writerc = csv.writer(filec)
        merge.to_csv(filec,index=False)
print('Analysis Complete')