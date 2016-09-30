# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 20:10:33 2015

@author: xz
"""
import pandas as pd

# PART I
# Load up the 'tutorial.csv' dataset
df = pd.read_csv('Datasets/tutorial.csv')    

# Print the results of the .describe() method
print df.describe()

# Figure out which indexing method you need to
# use in order to index your dataframe with: [2:4,'col3']
# And print the results
print df.loc[2:4, 'col3']


# PART II
# Load up the dataset
# Ensuring you set the appropriate header column names
df3 = pd.read_csv('Datasets/servo.data', header = None)

# Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
df3.columns = ['motor', 'screw', 'pgain', 'vgain', 'class']
dfv = df3[df3.vgain == 4]
print dfv.count()

# Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
dfms = df3[(df3.motor == 'E') & (df3.screw == 'E')]
print dfms.count()

# Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
dfp = df3[df3.pgain == 4]
print dfp.vgain.mean()


# PART III Data Manipulating
# Load up the table, and extract the dataset
# out of it. 
url = 'http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015'
df4 = pd.read_html(url)[0]

# Rename the columns so that they match the
# column definitions provided
df4.columns = ['RK', 'PLAYER', 'TEAM', 'GP', 'G', 'A', 'PTS', '+/-', 'PIM', 'PTS/G', 'SOG', 'PCT', 'GWG', 'G', 'A', 'G', 'A']

# Get rid of any row that has at least 4 NANs in it
df4 = df4.dropna(axis = 0, thresh = 4)

# At this point, look through dataset by printing
# it. There probably still are some erroneous rows in there.
df4 = df4[df4.RK != 'RK']
# Get rid of the 'RK' column
df4 = df4.drop(labels = ['RK'], axis = 1)

# Ensure there are no holes in the index by resetting
# it. By the way, don't store the original index
df4 = df4.reset_index(drop = True)

# Check the data type of all columns, and ensure those
# that should be numeric are numeric
print df4.dtypes
df4.GP = pd.to_numeric(df4.GP, errors = 'coerce')
df4.iloc[:, 3] = pd.to_numeric(df4.iloc[:, 3], errors = 'coerce')
df4.iloc[:, 4] = pd.to_numeric(df4.iloc[:, 4], errors = 'coerce')
df4.PTS = pd.to_numeric(df4.PTS, errors = 'coerce')
df4['+/-'] = pd.to_numeric(df4['+/-'], errors = 'coerce')
df4.PIM = pd.to_numeric(df4.PIM, errors = 'coerce')
df4['PTS/G'] = pd.to_numeric(df4['PTS/G'], errors = 'coerce')
df4.SOG = pd.to_numeric(df4.SOG, errors = 'coerce')
df4.PCT = pd.to_numeric(df4.PCT, errors = 'coerce')
df4.GWG = pd.to_numeric(df4.GWG, errors = 'coerce')
df4.iloc[:, -4] = pd.to_numeric(df4.iloc[:, -4], errors = 'coerce')
df4.iloc[:, -3] = pd.to_numeric(df4.iloc[:, -3], errors = 'coerce')
df4.G = pd.to_numeric(df4.G, errors = 'coerce')
df4.A = pd.to_numeric(df4.A, errors = 'coerce')

# dataset ready to go
print df4.PCT.unique()
print df4.PCT.value_counts()
df4.loc[15:16, 'GP']