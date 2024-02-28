# Slicing Arrays

""" Slicing in python means taking elements from one given index to another given index.
    We pass slice instead of index like this: [start:end].We can also define the step, like this: [start:end:step].
"""
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
# Slice elements from index 1 to index 5 from the following array:
print(arr[1:5])
# Slice elements from index 4 to the end of the array:
print(arr[4:])
# Slice elements from the beginning to index 4 (not included):
print(arr[:4])

#Negative Slicing

#Use the minus operator to refer to an index from the end:
#Slice from the index 3 from the end to index 1 from the end:
print(arr[-3:-1])
print(arr[:-1])
print(arr[-7:])

#Return every other element from the entire array:
print(arr[::2])

#Slicing 2-D Arrays

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])