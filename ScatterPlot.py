# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 21:30:12 2015

@author: xz
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
matplotlib.style.use('ggplot')

# Load up the Seeds Dataset into a Dataframe
df = pd.read_csv('Datasets/wheat.data')

# Create a slice of your dataframe (call it s1)
# that only includes the 'area' and 'perimeter' features
s1 = df[['area', 'perimeter']]

# Create another slice of your dataframe (call it s2)
# that only includes the 'groove' and 'asymmetry' features
s2 = df[['groove', 'asymmetry']]

# Create a histogram plot using the first slice,
# and another histogram plot using the second slice.
# Set alpha = 0.75
s1.plot.hist(alpha = 0.75)
s2.plot.hist(alpha = 0.75)
plt.show()

# Load up the Seeds Dataset into a Dataframe
df2 = pd.read_csv('Datasets/wheat.data')

# Create a 2d scatter plot that graphs the
# area and perimeter features
df2.plot.scatter(x = 'area', y = 'perimeter')

# Create a 2d scatter plot that graphs the
# groove and asymmetry features
df2.plot.scatter(x = 'groove', y = 'asymmetry')

# Create a 2d scatter plot that graphs the
# compactness and width features
df2.plot.scatter(x = 'compactness', y = 'width')

# Check out the optional display parameter marker with values of
# either '^', '.', or 'o'.
df2.plot.scatter(x = 'compactness', y = 'width', marker = '.')
df2.plot.scatter(x = 'compactness', y = 'width', marker = '^')
df2.plot.scatter(x = 'compactness', y = 'width', marker = 'o')
plt.show()



