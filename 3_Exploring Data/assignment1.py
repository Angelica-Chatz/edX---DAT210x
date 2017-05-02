import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'

df = pd.read_csv('wheat.data')

df.dtypes

df.describe()

# TODO: Create a slice of your dataframe (call it s1)
# that only includes the 'area' and 'perimeter' features

s1 = df.ix[:,1:3]

#
# TODO: Create another slice of your dataframe (call it s2)
# that only includes the 'groove' and 'asymmetry' features

s2 = df.ix[:,6:8]


#
# TODO: Create a histogram plot using the first slice,
# and another histogram plot using the second slice.
# Be sure to set alpha=0.75

s1.graph = s1.plot.hist(alpha=0.75)

s2.graph = s2.plot.hist(alpha=0.75)

# Display the graphs:
s1.graph = s1.plot.hist(alpha=0.75)

s2.graph = s2.plot.hist(alpha=0.75)
plt.show()

