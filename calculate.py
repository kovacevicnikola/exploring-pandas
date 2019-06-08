import numpy as np
import pandas as pd

def header(msg):
    print('-'*50)
    print(msg)
    print('-'*50)
    print()

header('read belgrade weather data into dataframe')
filename = 'bgd_data.txt'
df = pd.read_csv(filename)

header('calculate avg temp')
df['avg_temp'] = (df.temp_low + df.temp_high) / 2
header('avg temp in belgrade for the past month')
print(df.avg_temp.mean())
header('write avg temp to file')
df.to_csv('avgtemp.csv')

