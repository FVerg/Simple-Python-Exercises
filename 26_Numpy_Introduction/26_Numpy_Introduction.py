# In this lecture we are going to cover the usage of Numpy.
# Numpy is a Python library which allow us to manipulate images and videos.

# As you should already know, images are composed by pixels, and each pixel
# is painted in a certain color. Each color, for the computer, corresponds
# to a particular number, following a certain color representation (RGB, YUV).

# So: each image is composed by pixels and each pixel can be represented by a number
# Therefore, an image can be represented as a set of number

# Considering a 3X2 image. It can be represented as a list of 3 lists
# Image = [[P00, P01],[P10,P11],[P20,P21]]

# Here's how Numpy comes in handy
# If you've already installed Pandas, Numpy should be already installed

import numpy

n = numpy.arange(27)

# The arange method returns an array of evenly spaced numbers
# numpy.arange(3) = array ([0,1,2])
# The returned array is of type numpy.ndarray
# ndarray stays for n-dimensional array
# In this case n = 1

# To make it a multidimensional array we need to change its shape.
# Now, it is structured as a 1-dimensional array
# We want it to be a 2-dimensional array, so we reshape it by making it a
# 3X9 array (3 rows, 9 columns)

n.reshape(3,9)

# An image is a 2-dimensional array too! Each pixel can be identified
# by using a row index and a column index

# As you may've noticed, a numpy array is very similar to a Python list.
# Hence, it is possible to create a Numpy array from a Python list.

l = [[123,1,1,2,3],[],[]]

m = numpy.asarray(l)
