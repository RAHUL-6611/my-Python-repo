import numpy as np
import pandas as pd

# run this in jupter

dict1 = {"name": ['main', 'tum', 'voh'],
            "marks": [43, 57, 86],
            "city": ['pune', 'mumbai', 'lokhandwala', ]}

df = pd.DataFrame(dict1)
df

df.to_csv('friends.csv')     # containing all files of df

df.to_csv('def.csv', index=False)      # without index

df.head(2)  # shows only 2 rows from top
df.tail(2)  # shows only 2 rows from bottom

df.describe()    # gives you all stats

rr = pd.read_csv('abuda.csv')
rr['city'][0] = 'poona'
rr

rr.index = ['pehla', 'dushra', 'teeshra', 'choutha']
rr