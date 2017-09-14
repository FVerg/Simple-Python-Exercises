# In this lecture we are going to cover the adding and updating data in a
# Dataframe. It is recommended to use Jupyter Notebook.

import pandas

df = pandas.read_json("http://pythonhow/supermarkets.json")

df = df.set_index("Address")

# First of all, we want to add a new column.
# Let's suppose we want to add a column "Continent", which has North America
# for each row of the dataframe.

print (df.shape)

# This prints the dimension of the dataframe in (#Rows, #Columns)

print (df.shape[0])

# This prints only the first element of the result given by shape
# So, it returns the number of rows
# df.shape[1] returns the number of columns

print (df.shape[0]*["North America"])

# This way we are going to multiply the number of rows (in this case 5)
# times a list with only an element. The result of this operation will be
# a new list containing the same element replicated 5 times.
# In this case : ["North America", ... , "North America"]

# We want this list to be the data for each of the rows of the dataframe,
# corresponding to the attribute (column) "Continent" we are going to create

df["Continent"] = df.shape[0]*["North America"]

# This way we are creating a new column, "Continent" and we are replicating
# the data North America for each row of the dataframe.

# To modify a column we can just do:

df["Continent"] = df["Country"] +", " + "North America"

# This way we are editing all the data of the column continent by replacing
# the previous data with the value of the corresponding Country and ", North America"

# To add a new row we have to do different things

df_t = df.T

# THe method T is going to transpose the original dataframe. So, the new one,
# df_t will have the same data as the original dataframe df, but with rows and
# columns reversed. It is the same as the transposition in algebra.
# Now, we can use the same syntax we used before for editing columns.

df_t["My Address"] = ["My city", "My country", "10", "7", "My shop", "My state", "My continent"]

# This way we are creating a new column, with the data specified by the list.
# Now we have to transpose back the dataframe, in order to let it be structured
# as the original one

df = df_t.T

# To modify a row you simply need to point to the one you want to modify

df_t["332 Hill St"] = ["My city", "My country", "10", "7", "My shop", "My state", "My continent"]

# And then transpose back the dataframe

df = df_t.T
