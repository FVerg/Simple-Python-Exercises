# In this lecture we are going to cover the indexing and slicing of dataframes in
# Pandas. It is recommended to use Jupyter Notebook for a better data view.

import pandas

df1 = pandas.read_csv("http://pythonhow.com/supermarkets.csv")


# To extract informations from the dataframes we need to use a coordinate-like
# system. Let's suppose we want to extract the country of Bready Shop
# (Print the dataframe to understand what I'm talking about). We want to SLICE
# the data frame. To do this we can do different things.

# LABEL INDEXING
# The dataframe has index and column labels. We can access to portions of data
# by using those labels.
# To do that, we need to select an index for the rows, not the default online

df1 = df1.set_index("Address")

# Just for completeness: we can set the index of a DataFrame without using the
# previous syntax, but using another parameter of set_index, which "tells" the
# function to overwrite the previous dataframe.

# df1.set_index("Address", inplace=True)

print (df1)

# Now, in order to access to a portion of a DataFrame, we can use the loc method.
# It takes two parameters, one indexing the row, one indexing the column.

print(df1.loc["735 Dolores St":"332 Hill St","Country":"ID"])

# This way, we selected a range of tuples (From the one with address 735 Dolores St
# to the one with address 332 Hill St), considering the attributes from Country to ID
# Using loc, the specified indexes get included in the slice.

# It is possible to access single cells too

print (df1.loc["735 Dolores St","Country"])

# We can access to all the countries by doing:

df1.loc[:,"Country"]

# And convert it to a list:

l = list(df1.loc[:,"Country"])

print (l)

# This is not the common way to access data.

# INDEX INDEXING

# This way, we are addressing to tuples by using their index numbers, both for columns
# and for rows. This approach is upper bound exclusive, so the first index specified (1)
# will be included, but the last one (3) will not. That's different from the previous approach.

print (df1.iloc[1:3,1:3])

# To get the same result as before we must do:

print (df1.iloc[1:4,1:4])


# IX INDEXING

# That is another approach to access data in DataFrames.
# It allows to use a combination of indexes and labels in order to extract some data.

print (df1.i[3,"Name"])

# ix can be used for both index and label indexing.

# In order to DELETE something from a DataFrame, we can do:

print(df1.drop ("City",1))

# The parameter 1 indicates we are going to delete a column

print (df1.drop("332 Hill St", 0))

# The parameter 1 indicates we are going to delete a row

# We can combine indexing and data drop:

print (df1.drop(df1.index[0:3],0))

print (df1.drop(df1.columns[0:3],1)
