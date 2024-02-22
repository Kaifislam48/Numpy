# Access Array Elements by help Indexing.
""" Array indexing is the same as accessing an array element.
    You can access an array element by referring to its index number.
    The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 and so on. 
"""

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

print("Positive Indexing:-- ")
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])

# We can also use right to left indexing from -1 to n-1
print("Negative Indexing:-- ")
print(arr[-1])
print(arr[-2])
print(arr[-3])
print(arr[-4])
print(arr[-5])

# We can Add two element of Array by the help of Indexing
arr = np.array([1, 2, 3, 4])
print("Add two element by index: ", (arr[2] + arr[3]))


# Access 2-D Arrays. To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])
print("3rd element of 2nd row: ", arr[1, 2])

# Access 3-D Arrays. To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])