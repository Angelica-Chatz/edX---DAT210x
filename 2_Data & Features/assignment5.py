import pandas as pd
import numpy as np

np.set_printoptions(suppress=True)

# TODO:
# Load up the dataset, setting correct header labels.

df=pd.read_csv('census.data', index_col=0,header=None)


df.dtypes

df.columns=['education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification']

df.dtypes

# TODO:
# Use basic pandas commands to look through the dataset... get a
# feel for it before proceeding! Do the data-types of each column
# reflect the values you see when you look through the data using
# a text editor / spread sheet program? If you see 'object' where
# you expect to see 'int32' / 'float64', that is a good indicator
# that there is probably a string or missing value in a column.
# use `your_data_frame['your_column'].unique()` to see the unique
# values of each column and identify the rogue values. If these
# should be represented as nans, you can convert them using
# na_values when loading the dataframe.

df['capital-gain'].unique()

df2=pd.read_csv('census.data', index_col=0,na_values=['?'],header=None)

df2.columns=['education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification']

df2.dtypes

# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any ordinal and nominal
# types using the methods discussed in the chapter.
#
# Be careful! Some features can be represented as either categorical
# or continuous (numerical). If you ever get confused, think to yourself
# what makes more sense generally---to represent such features with a
# continuous numeric type... or a series of categories?

df2 = pd.get_dummies(df2,columns=['sex'])

ordered_edu=['Preschool','1st-4th','5th-6th','7th-8th','9th','10th','11th','12th',' HS-grad','Prof-school','Assoc-acdm','Assoc-voc','Some-college','Bachelors','Masters','Doctorate']

df2.education=df.education.astype("category",ordered=True,categories=ordered_edu).cat.codes

# TODO:
# Print out your dataframe

print(df)