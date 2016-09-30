# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 21:39:02 2016

@author: xz
"""
# PART I
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

# Look pretty...
matplotlib.style.use('ggplot')

# Load up the Seeds Dataset into a Dataframe
df3 = pd.read_csv('Datasets/wheat.data')

fig = plt.figure()
# Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the area,
# perimeter and asymmetry features. Use the
# optional display parameter c = 'red'
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('area')
ax.set_ylabel('perimeter')
ax.set_zlabel('asymmetry')
ax.scatter(df3.area, df3.perimeter, df3.asymmetry, c = 'red')

fig = plt.figure()
# Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the width,
# groove and length features. Use the
# optional display parameter c='green'
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('width')
ax.set_ylabel('groove')
ax.set_zlabel('length')
ax.scatter(df3.width, df3.groove, df3.length, c = 'green')

plt.show()

####################################################################
# PART II
from pandas.tools.plotting import parallel_coordinates

# Load up the Seeds Dataset into a Dataframe
df = pd.read_csv('Datasets/wheat.data')

# Drop the 'id', 'area', and 'perimeter' feature
df = df.drop(labels = ['id', 'area', 'perimeter'], axis = 1)

# Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Set the optional
# display parameter alpha to 0.4
plt.figure()
parallel_coordinates(df, 'wheat_type', alpha = 0.4)
plt.show()

####################################################################
# PART III
from pandas.tools.plotting import andrews_curves
# Look pretty...
matplotlib.style.use('ggplot')

# Load up the Seeds Dataset into a Dataframe
df = pd.read_csv('Datasets/wheat.data')

# Drop the 'id', 'area', and 'perimeter' feature
df = df.drop(labels = ['id', 'area', 'perimeter'], axis = 1)
df = df.drop(labels = ['id'], axis = 1)

# PLOT Andrew's Curves
plt.figure()
andrews_curves(df, 'wheat_type')
plt.show()

####################################################################
# PART IV
# Load up the Seeds Dataset into a Dataframe
df = pd.read_csv('Datasets/wheat.data')

# Drop the 'id' feature
df = df.drop(labels = ['id'], axis = 1)

# Compute the correlation matrix
df.corr()

# Graph the correlation matrix using imshow or matshow
plt.imshow(df.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(df.columns))]
plt.xticks(tick_marks, df.columns, rotation='vertical')
plt.yticks(tick_marks, df.columns)

plt.show()
