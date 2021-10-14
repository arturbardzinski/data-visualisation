import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("matrix.csv", sep=",")
df = df.set_index("Report Date")
df = df[['Line Number', 'Report Hour', 'Kits Completed']]

line_number = df['Line Number']
report_hour = df['Report Hour']
kits_completed = df['Kits Completed']

#line_11 = [kits_completed.sum(axis=1) if line_number == 11]
for line in line_number:
    if line_number == '11':
        print(line_number)
#print(df[df['Kits Completed'] != 0])

#plt.pie(line_number, report_hour)
#plt.show()
# df.iloc[1] can display specific hour, line and kits

# user choice line and hour
