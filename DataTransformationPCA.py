# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 23:31:00 2015

@author: xz
"""
# PART I
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import datetime

from mpl_toolkits.mplot3d import Axes3D
from plyfile import PlyData, PlyElement

# Every 100 data samples, we save 1. If things run too
# slow, try increasing this number. If things run too fast,
# try decreasing it... =)
reduce_factor = 100

# Look pretty...
matplotlib.style.use('ggplot')

# Load up the scanned armadillo
plyfile = PlyData.read('Datasets/stanford_armadillo.ply')
armadillo = pd.DataFrame({
  'x':plyfile['vertex']['z'][::reduce_factor],
  'y':plyfile['vertex']['x'][::reduce_factor],
  'z':plyfile['vertex']['y'][::reduce_factor]
})

# Function for importing the libraries required for PCA.
# Then, train PCA on the armadillo dataframe. Finally,
# drop one dimension (reduce it down to 2D) and project the
# armadillo down to the 2D principal component feature space.
#
# (This projection is actually stored in a NumPy NDArray and
# not a Pandas dataframe, which is something Pandas does automatically. =)
def do_PCA(armadillo):
  from sklearn.decomposition import PCA
  pca = PCA(n_components =  2)
  pca.fit(armadillo)
  PCA(copy=True, n_components=2, whiten=False)
  df = pca.transform(armadillo)
  return df

# Write code to import the libraries required for
# RandomizedPCA. Then, train RandomizedPCA on the armadillo
# dataframe. Finally, drop one dimension (reduce it down to 2D)
# and project the armadillo down to the 2D principal component
# feature space.
def do_RandomizedPCA(armadillo):
  from sklearn.decomposition import RandomizedPCA
  rpca = RandomizedPCA(n_components = 2)
  rpca.fit(armadillo)
  RandomizedPCA(copy = True, n_components = 2, whiten = False)
  rdf = rpca.transform(armadillo)
  return rdf
  
# Render the Original Armadillo
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Armadillo 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.scatter(armadillo.x, armadillo.y, armadillo.z, c='green', marker='.', alpha=0.75)

# Render the newly transformed PCA armadillo!
t1 = datetime.datetime.now()
pca = do_PCA(armadillo)
time_delta = datetime.datetime.now() - t1
if not pca is None:
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.set_title('PCA, build time: ' + str(time_delta))
  ax.scatter(pca[:,0], pca[:,1], c='blue', marker='.', alpha=0.75)

# Render the newly transformed RandomizedPCA armadillo!
t1 = datetime.datetime.now()
rpca = do_RandomizedPCA(armadillo)
time_delta = datetime.datetime.now() - t1
if not rpca is None:
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.set_title('RandomizedPCA, build time: ' + str(time_delta))
  ax.scatter(rpca[:,0], rpca[:,1], c='red', marker='.', alpha=0.75)

plt.show()


###############################################################################
# PART II
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import pca_helper as helper #helper module not upload on github

# Look pretty...
matplotlib.style.use('ggplot')

# Do * NOT * alter this line, until instructed!
scaleFeatures = True

# Load up the dataset and remove any and all
# Rows that have a nan.
df = pd.read_csv('Datasets/kidney_disease.csv')
df = df.drop(labels = ['id', 'classification', 'rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane'], 
             axis = 1)
df = df.dropna(axis = 0)
df = df.reset_index(drop = True)

# Create some color coded labels; the actual label feature
# will be removed prior to executing PCA, since it's unsupervised.
# Only labeling by color so it can see the effects of PCA
# labels = ['red' if i=='ckd' else 'green' for i in df.classification]

# Use an indexer to select only the following columns:
#       ['bgr','wc','rc']

# Print out and check the dataframe's dtypes. It probably
# want to call 'exit()' after print it out so it can stop the
# program's execution.
#
# It can either take a look at the dataset webpage in the attribute info
# section: https://archive.ics.uci.edu/ml/datasets/Chronic_Kidney_Disease
# or actually peek through the dataframe by printing a few rows.
print df.dtypes
df.pcv = pd.to_numeric(df.pcv, errors = 'coerce')
df.wc = pd.to_numeric(df.wc, errors = 'coerce')
df.rc = pd.to_numeric(df.rc, errors = 'coerce')

# PCA Operates based on variance. The variable with the greatest
# variance will dominate. Go ahead and peek into the data using a
# command that will check the variance of every feature in the dataset.
# Print out the results. Also print out the results of running .describe
# on the dataset.
if scaleFeatures: df = helper.scaleFeatures(df)

# Run PCA on dataset and reduce it to 2 components
# The results of transformation are saved in 'T'.
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
pca.fit(df)
T = pca.transform(df)

# Plot the transformed data as a scatter plot. The transforming
# data will result in a NumPy NDArray.  Either use MatPlotLib
# to graph it directly, or convert it to DataFrame and have pandas
# do it.
ax = helper.drawVectors(T, pca.components_, df.columns.values, plt, scaleFeatures)
T = pd.DataFrame(T)
T.columns = ['component1', 'component2']
T.plot.scatter(x = 'component1', y = 'component2', marker='o', c = labels, alpha=0.75, ax=ax)

plt.show()



