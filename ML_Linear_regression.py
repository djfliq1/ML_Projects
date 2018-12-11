import numpy as np
import pandas as pd
import quandl

# stock prices linear regression
# Get your data
df = quandl.get('WIKI/GOOGL')
# Get only the data you want. The list is by headers
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
# (a-b)/b*100. Cleaning the data a little
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
# Factors we want to actually see
df= df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

print(df.head())