__author__ = 'Edmond van der Plas'
__date__ = '30-11-2013'
__version__ = '0.2.1'

import pandas as pd

import sys
from datetime import datetime


#Importeren van de csv data waarbij de filename van het csv bestand ingegeven is als argument in het starten van het python script
df = pd.read_csv(sys.argv[1], header=None, na_values='') #

df2 = df[[2, 4, 6, 8, 10]]
df2.columns=['Datum', 'Bedrag', 'Tegenrekening', 'afbij','Omschrijving']

#Indien geen tegenrekening bekend, dan - weergeven i.p.v. NaN
df2 = df2.astype(object).fillna(' ')

#Een float maken van de bedragen (als type)
df2['Bedrag'] =  df2['Bedrag'].astype(float)

df2['Datum'] =  df2['Datum'].astype(str)
df2.Datum = df2.Datum.apply(lambda d: datetime.strptime(d, '%Y%m%d'))
df2['Datum']=df2['Datum'].map(lambda x: x.strftime('%d/%m/%Y'))

#Berekening maken of bedrag positief of negatief is
df2['Bedrag2'] = df2.apply(lambda row: (row['Bedrag']
                                             if row['afbij']=='cb'
                                            else -row['Bedrag']), axis=1)

print df2.dtypes

#Kolommen selecteren voor output
df3 = df2[['Datum','Omschrijving', 'Bedrag2','Tegenrekening']]

#Datastructuur naar csv schrijven
df3.to_csv('transacties_rabo_ibank.csv', sep=',', na_rep='0', dtype=int)

print df3
