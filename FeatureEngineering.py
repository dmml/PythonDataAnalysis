import pandas as pd
import numpy as np

# Load up the dataset, setting correct header labels
# Use basic pandas commands to look through the dataset...
# get a feel for it before proceeding!
# Find out what value the dataset creators used to
# represent "nan" and ensure it's properly encoded as np.nan

df5 = pd.read_csv('Datasets/census.data', header = None)
df5.columns = ['n', 'education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification']
df5 = df5.drop(labels = ['n'], axis = 1)

# Figure out which features should be continuous + numeric
# Conert these to the appropriate data type as needed,
# that is, float64 or int64

# Look through data and identify any potential categorical
# features. Ensure properly encode any ordinal types.
order_class = ['<=50K', '>50K']
df5.classification = df5.classification.astype("category", ordered = True,
                                              categories = order_class
                                              ).cat.codes
order_edu = ['Bachelors', 'HS-grad', '11th', 'Masters', '9th', 'Some-college',
       '7th-8th', 'Doctorate', '5th-6th', '10th', '1st-4th', 'Preschool',
       '12th']
df5.education = df5.education.astype("category", ordered = True, 
                                     categories = order_edu
                                     ).cat.codes

# Look through data and identify any potential categorical
# features. Ensure properly encode any nominal types by
# exploding them out to new, separate, boolean fatures.
df5 = pd.get_dummies(df5, columns = ['race', 'sex'])

# Print out dataframe
print df5