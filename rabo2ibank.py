__author__ = 'Edmond van der Plas'
__date__ = '16-11-2013'
__version__ = '0.2'

import pandas as pd

import sys

#Importeren van de csv data waarbij de filename van het csv bestand ingegeven is als argument in het starten van het python script
df = pd.read_csv(sys.argv[1], header=None) #

df2 = df[[2, 4, 6, 8, 10]]
df2.columns=['Datum', 'Bedrag', 'Tegenrekening', 'afbij','Omschrijving']

#Als scheidingsteken voor decimalen een punt instellen ipv een comma en daarna een float maken van de bedragen (als type)

df2['Bedrag'] =  df2['Bedrag'].astype(float)

#Berekening maken of bedrag positief of negatief is
df2['Bedrag2'] = df2.apply(lambda row: (row['Bedrag']
                                             if row['afbij']=='cb'
                                            else -row['Bedrag']), axis=1)

#Kolommen selecteren voor output
df3 = df2[['Datum','Omschrijving', 'Bedrag2','Tegenrekening']]

#Datastructuur naar csv schrijven
df3.to_csv('test_result.csv', sep=',', na_rep='0', dtype=int)

print df3
