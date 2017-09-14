# EX 07: Translating addresses into geographic coordinates
# The process of translating an address to a pair of coordinates is called
# geo-coding. The reverse mechanism is called reverse geo-coding

# To do this exercise you need to install the Geopy library
# https://github.com/geopy/geopy
import pandas
import geopy

df = pandas.read_csv ("http://pythonhow/supermarkets.csv")

# Geopy needs an internet connection to use its module "geocoder", the one we
# need for our purposes.

# We need to use the tool Nominatim, included in the geocoders module

from geopy.geocoders import Nominatim

# We create a Nominatim variable
nom = Nominatim (scheme='http')

n = nom.geocode("3995 23rd St, San Francisco, CA 94114")

# By using this method we receive a location, another data type
# Location(3995, 23rd Street, Noe Valley, SF,
# California, 94114, United States of America, (37.7529648, -122.4317141, 0.0))

# If the address inserted doesn't exist, nothing will be returned

# From a location data type, we can extract latitude and longitude by using
# the corresponding methods.

lat = n.latitude
lon = n.longitude

# This is the way we translate an address into coordinates.

# We want to do that by using the addresses included in the df dataframe
# First, we want to edit the "Address" column in order to contain the
# entire data we need to pass to the geocode method.

df["Address"] = df["Address"]+", "+df["City"]+", "+ df["State"] + ", " + df["Country"]

# On a Pandas DataFrame we don't need to iterate. Pandas allow to apply methods
# on all the rows of a DataFrame.

# The apply method allow us to do that. It takes as a parameter the function
# to apply on each row. The parameter the function will take will change every
# time a new row is considered.

df ["Coordinates"] = df["Address"].apply(nom.geocode)

# With this operation, we are going to create a new column called coordinates, in
# which we put the result of nom.geocode(row), for each row of the dataframe.
# The nom.geocode will get as a parameter the address, as indicated from df["Address"]

# This way we put all the informations about the location, not only the coordinates in the dataframe.
# To put the coordinates only:

df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x != None else None)

df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x != None else None)

# With these two statements we are going to apply the function latitude and longitude for each row of the
# dataframe. We are going to apply those functions on the Position object stored in df["Coordinates"]
# If for some reason, the Coordinates value is None (maybe because the position cannot be
# calculated, because of the unreal address in the dataset), the function must not be applied
# This way, we avoid getting errors due to non-present data.
