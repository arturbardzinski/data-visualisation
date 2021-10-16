import pandas as pd

data = [
    {"Line Number": 11, "Report Hour": 6, "Kits Completed": 34},
    {"Line Number": 11, "Report Hour": 7, "Kits Completed": 55},
    {"Line Number": 12, "Report Hour": 6, "Kits Completed": 67},
    {"Line Number": 12, "Report Hour": 7, "Kits Completed": 56},
    {"Line Number": 14, "Report Hour": 6, "Kits Completed": 0},
    {"Line Number": 14, "Report Hour": 7, "Kits Completed": 0},
    {"Line Number": 15, "Report Hour": 6, "Kits Completed": 123},
    {"Line Number": 15, "Report Hour": 7, "Kits Completed": 97},
]

df = pd.DataFrame.from_records(data)

grouped_by_hour = (
    df.groupby("Report Hour", as_index=False).sum().drop(columns="Line Number")
)

chart = grouped_by_hour.plot.bar(x="Report Hour", y="Kits Completed", rot=0)
chart.figure.savefig('chart.png')
chart.figure.show()

print(grouped_by_hour)

input("Press a key to close the chart")

