# In this application we are going to create a web map: a map accessible on
# a website.

# To create this map you'll need an external library, called Folium
# You can download it by typing in the cmd "pip install folium"

# Almost everything in Folium spins around a so called map object

import folium
import pandas
import numpy

# Folium will automatically detect and translate your Python code into
# Javascript and HTML, in order to use it on the web.
# A Folium map needs some parameters:
# - Location: Latitude and Longitude of the map (list)
# - Width: Width of the map (in percentage or pixel)
# - Height: Height of the map (in percentage or pixel)
# - Tiles: Represent the background of the map ('OpenStreetMap' is the default value)
# [...]

map = folium.Map(location=[43, 13])

# I used Italy coordinates

# We created a map, and we need to save it in a HTML file

map.save("Output/Map1.html")

# We can try different kind of maps by changing the tiles parameter

map = folium.Map(location=[43, 13], tiles="Mapbox Bright")

map.save("Output/Map2.html")

# We want now to add points to the map.
# To do that we need to add a Folium Marker to the Map

map = folium.Map(location=[43, 13], tiles="Mapbox Bright")

# The object we want to add to a map must be between the creation and the
# saving of the map.

# The objects we are talking about, like markers, are children of the map.

# The Marker object has parameters:
# - Location: Where the marker has to be placed
# - Popup: What the marker has to show when pressed
# - Icon: The icon plugin used to render the marker

map.add_child(folium.Marker(location=[40.823250, 14.210104], popup="Home", icon = folium.Icon(color='red')))

map.save("Output/Map3.html")

# To do a better organization we can use feature groups, which allow us to
# separate the objects in the map by collecting them into different groups.

map = folium.Map(location=[43, 13], tiles="Mapbox Bright")

fg = folium.FeatureGroup (name ="My map")

fg.add_child(folium.Marker(location=[40.823250, 14.210104], popup="Home", icon = folium.Icon(color='red')))

map.add_child(fg)

# This helps to keep the code and the map more organized, when we are going to add to
# it more layers and more complex objects.

map.save("Output/Map3.html")

# To add multiple markers we can apply the add_child method multiple times
# or we can use the for loop.

map = folium.Map(location=[43, 13], tiles="Mapbox Bright")

fg = folium.FeatureGroup (name ="My markers")

for coordinates,names in zip([[40.823250, 14.210104], [45.062305, 7.662385]],["Home","Politecnico"]):
    fg.add_child(folium.Marker(location=coordinates, popup=names, icon = folium.Icon(color='red')))

# If you are in trouble trying to understand this for loop statement, get back to
# Lesson "12_Foor_Loop"

map.add_child(fg)

# This helps to keep the code and the map more organized, when we are going to add to
# it more layers and more complex objects.

map.save("Output/Map4.html")

# Now we want the coordinates of multiple markers to be automatically
# extracted from a txt file, which you can find in the Resources folder.

# To do this you'll need the Pandas library.
# pip install pandas

input_data = pandas.read_csv("./Resources/Volcanoes.txt")

print (input_data)

# We now need to iterate over the dataframe input_data
# We want to create two lists:
# 1: Containing the column of Latitude
# 2: Containing the column of Longitude

lat = list(input_data["LAT"])
lon = list(input_data["LON"])
elev = list (input_data["ELEV"])

print (lat)
print (lon)

# We want to create one marker for each couple (lat, lon) contained in those 2 lists
map = folium.Map(location=[43, 13], tiles="Mapbox Bright")

fg = folium.FeatureGroup (name ="My markers")

# Again if you are unconfortable with this loop statement take a look to the
# lesson "12_For_Loop"

for latitude, longitude, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location = [latitude,longitude], popup = str(el)+" m", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Output/Map5.html")

# We want now to add smarter features to the map.
# We could, for example, change the color of the different markers
# according to the height of the volcano related to it.
# GREEN: From 0 to 1000m
# ORANGE: From 1000 to 2000m
# RED: More than 2000m

map = folium.Map(location=[43, 13], tiles="Mapbox Bright")

fg = folium.FeatureGroup (name ="My markers")

for latitude, longitude, el in zip(lat, lon, elev):
    if el < 1000:
        fg.add_child(folium.Marker(location = [latitude,longitude], popup = str(el)+" m", icon=folium.Icon(color='green')))
    elif el > 1000 and el < 2000:
        fg.add_child(folium.Marker(location = [latitude,longitude], popup = str(el)+" m", icon=folium.Icon(color='orange')))
    else:
        fg.add_child(folium.Marker(location = [latitude,longitude], popup = str(el)+" m", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Output/Map6.html")

# We can also do this by using a function:
# Input: Elevation
# Output: Color depending on the Elevation

def calculate_color(elevation):
    if elevation < 1000:
        return "green"
    elif elevation < 2000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[43, 13], tiles="Mapbox Bright")

fg = folium.FeatureGroup (name ="My markers")

for latitude, longitude, el in zip(lat, lon, elev):
    color = calculate_color(el)
    fg.add_child(folium.Marker(location = [latitude,longitude], popup = str(el)+" m", icon=folium.Icon(color=color)))

map.add_child(fg)

map.save("Output/Map7.html")
