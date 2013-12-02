__author__ = 'Edmond van der Plas'
__date__ = '01-12-2013'
__version__ = '0.2.1'

import pandas as pd

import sys
from datetime import datetime


#Importeren van de csv data waarbij de filename van het csv bestand ingegeven is als argument in het starten van het python script
df = pd.read_csv(sys.argv[1], header=None, na_values='') #

df2 = df[[2, 4, 6, 8, 10]]
df2.columns=['Date', 'Amount', 'Payee', 'afbij','Memo']

#Indien geen Payee bekend, dan - weergeven i.p.v. NaN
df2 = df2.astype(object).fillna(' ')

#Een float maken van de Amounten (als type)
df2['Amount'] =  df2['Amount'].astype(float)

#Date als string voor omzetten naar datetime64 in 2e regel
#In derde regel wordt de formattering van de Date voor Ibank toegepast, namelijk dd/mm/yyyy
df2['Date'] =  df2['Date'].astype(str)
df2.Date = df2.Date.apply(lambda d: datetime.strptime(d, '%Y%m%d'))
df2['Date']=df2['Date'].map(lambda x: x.strftime('%d/%m/%Y'))

#Berekening maken of Amount positief of negatief is
df2['Amount2'] = df2.apply(lambda row: (row['Amount']
                                             if row['afbij']=='cb'
                                            else -row['Amount']), axis=1)

#Kolommen selecteren voor output
df3 = df2[['Date','Memo', 'Amount2','Payee']]

#Datastructuur naar csv schrijven
df3.to_csv('transacties_rabo_ibank.csv', sep=',', na_rep='0', dtype=int)

print df3
