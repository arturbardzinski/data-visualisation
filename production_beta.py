import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json

df = pd.read_csv("matrix.csv", sep=",")
#df = df.set_index("Report Date")
df = df[['Line Number', 'Report Hour', 'Kits Completed']]
line11 = df[df['Line Number'] == 11]
line12 = df[df['Line Number'] == 12]
line15 = df[df['Line Number'] == 15]

line_number = df['Line Number']
report_hour = df['Report Hour']
kits_completed = df['Kits Completed']

"""Zamienia dane na lista w liście"""
df = df.to_dict('records')

df = pd.DataFrame(df)
table = df.pivot(index='Report Hour', columns='Line Number', values = 'Kits Completed')
table.plot.bar()
plt.show()


#lists = df.values
#print(df[df['Kits Completed'] != 0])
#plt.plot(lists)
#plt.pie(line_number, report_hour)
#plt.show()
