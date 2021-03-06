__author__ = 'Edmond van der Plas'
__date__ = '07-12-2013'
__version__ = '0.3.2'
__account_type__ = 'Spaarrekening'


import pandas as pd

import sys
from datetime import datetime


#Importeren van de csv data waarbij de filename van het csv bestand ingegeven is als argument in het starten van het python script
df = pd.read_csv(sys.argv[1], header=None, na_values='') #

df2 = df[[2, 3, 4, 10, 11]]
df2.columns=['Date', 'afbij', 'Amount', 'Payee', 'Memo']

#Indien geen Payee bekend, dan whitespace weergeven i.p.v. NaN
df2 = df2.astype(object).fillna(' ')

#Een float maken van de Amount (als type)
df2['Amount'] =  df2['Amount'].astype(float)

#Date als string voor omzetten naar datetime64 in 2e regel
#In derde regel wordt de formattering van de Date voor Ibank toegepast, namelijk dd/mm/yyyy
df2['Date'] =  df2['Date'].astype(str)
df2.Date = df2.Date.apply(lambda d: datetime.strptime(d, '%Y%m%d'))
df2['Date']=df2['Date'].map(lambda x: x.strftime('%d/%m/%Y'))

#Berekening maken of Amount positief of negatief is
df2['Amount2'] = df2.apply(lambda row: (row['Amount']
                                             if row['afbij']=='C'
                                            else -row['Amount']), axis=1)

#df2['Amount2'].replace(',','').replace('.',',').astype(float)

#Kolommen selecteren voor output
df3 = df2[['Date','Memo', 'Amount2','Payee']]

#Datastructuur naar csv schrijven
df3.to_csv('transacties_rabo_ibank.csv', sep=',', na_rep='0', dtype=int)

print df3
