import pandas as pd
import matplotlib.pyplot as plt

df = [{'Line Number': 11, 'Report Hour': 6, 'Kits Completed': 34}, {'Line Number': 11, 'Report Hour': 7, 'Kits Completed': 55}, {'Line Number': 12, 'Report Hour': 6, 'Kits Completed': 67}, {'Line Number': 12, 'Report Hour': 7, 'Kits Completed': 56}, {'Line Number': 14, 'Report Hour': 6, 'Kits Completed': 0}, {'Line Number': 14, 'Report Hour': 7, 'Kits Completed': 0}, {'Line Number': 15, 'Report Hour': 6, 'Kits Completed': 123}, {'Line Number': 15, 'Report Hour': 7, 'Kits Completed': 97}]
df = pd.DataFrame(df)

table = df.pivot(index='Report Hour', columns='Line Number', values = 'Kits Completed')
table.plot.bar()
plt.show()