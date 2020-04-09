# records.py
"""formats address records and eliminates records with missing critical fields."""
import numpy as np
import pandas as pd

# record_data = np.genfromtxt(r'/Users/tylerclark/Repos/SDEV300/wk4/MOCK_DATA.csv', delimiter=',', skip_header=1,usecols=[0,1,2,3],dtype='U')

df = pd.read_csv(r'/Users/tylerclark/Repos/SDEV300/wk4/MOCK_DATA.csv', sep=',',header=None)
print(df.values)

