# Creating 0-D Array in Numpy

import numpy as np
arr = np.array(20)
print("0-D Array:-> ", arr)
# We can check which type of array so for this we can use Variable Name with dot(.) and ndim.
print("Dimention:- ", arr.ndim)

# Creating 1-D Array in Numpy
# we can also use Tuple for creating Array in Numpy

arr = np.array((1, 2, 3, 4, 5))
print("1-D Array:-> ", arr)
print("Dimention:- ", arr.ndim)


# Creating 2-D Array in Numpy

arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("2-D Array:-> ", arr1)
print("Dimention:- ", arr1.ndim)

arr2 = np.array(((1, 2, 3, 4), (4, 5, 7, 8)))
print("2-D Array:-> ", arr2)
print("Dimention:- ", arr2.ndim)


# Creating 3-D Array in Numpy

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("3-D Array:-> ", arr)
print("Dimention:- ", arr.ndim)

# We can Create Higher Dimensional Arrays like An array can have any number of dimensions. 
# When the array is created, you can define the number of dimensions by using the ndmin argument.

arr = np.array([1, 2, 3], ndmin = 5)
print(arr)
print("Number of Dimention in this Array:- ", arr.ndim)