# In this lecture we are going to cover the different ways to import
# datasets in pandas. We'll use file such as .xlsx, .csv, .json etc.

# You can find some example files in the Resources folder.

# In order to have a better data visualization, it is recommended to use
# the Jupyter Notebook: http://jupyter.org/

# For this lecture, I used jupyter notebook, but you can do the same by using
# a normal text editor, such as Atom or Notepad++.

# I'll report here the lines of code I used, and the jupyter notebook file too
# whose format is .ipynb

import pandas

df1 = pandas.read_csv("Resources/supermarkets.csv")

print (df1)

# Each file format has a header, which recognizes the column names.
# If we want to ignore that, and consider the tuple containing the column names
# equal to the others, we can do it by typing:

df1 = pandas.read_csv ("Resources/supermarkets.csv", header=None)

# Pandas will create a default header for column names

# As you may have noticed, Python automatically sets an automatic ID.
# If we want to set a custom ID, we can do by typing:

df1 = df1.set_index("ID")

# This way, Python will find for a column named "ID" and will use it as an index.
print (df1)

# If we want to know the dimension of the datasets in columns/rows:

print (df1.shape)

# In order to read a json file, we can do:

df2 = pandas.read_json("Resources/supermarkets.json")

# We can do the same for the index, as we did before:

df2 = df2.set_index("ID")

# Now, let's import an excel file (xlsx):

df3 = pandas.read_excel("Resources/supermarkets.xlsx")

# As you know, excel files can have multiple sheets.
# They are identified by the parameter sheetname, which goes from 0 to N
# with N the last sheet.

df3 = pandas.read_excel("Resources/supermarkets.xlsx", sheetname=0)

# Now, as you can see we have a txt file in the Resources folder. If we take a look
# to it, we notice that it has its data separated by commas. So, in order to import
# it in a DataFrame, we need to use the read_csv function (CSV = Comma Separated Value)

df4 = pandas.read_csv("Resources/supermarkets-commas.txt")

# Obviously, in a txt file, we can use the separator character we prefer.
# To indicate it, we can use the separator parameter:

df5 = pandas.read_csv ("Resources/supermarkets-semi-colons.txt", sep=';')

# If we do not specify the separator for a txt file whom separator character
# is different from the comma, Python won't recognize the dataset correctly.


# Pandas allows to read online files as well!
# For example, we can read a file host on a website: http://pythonhow.com/supermarkets.csv

df6 = pandas.read_csv("http://pythonhow.com/supermarkets.csv")

df7 = pandas.read_json("http://pythonhow.com/supermarkets.json")
