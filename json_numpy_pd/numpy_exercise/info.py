# NumPy is used to work with arrays. The array object in NumPy is called ndarray.

import numpy as np 
print(np.__version__)

# 0-D Arrays
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
# Create a 0-D array with value 42

arr = np.array(42)
print(arr) # result = 42


# 1-D Arrays
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
# Create a 1-D array containing the values 1,2,3,4,5:

arr1 = np.array([1,2,3,4,5])
print(arr1)


# 2-D Arrays
# An array that has 1-D arrays as its elements is called a 2-D array.
# These are often used to represent matrix or 2nd order tensors.
# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:

arr2 = np.array([[1,2,3], [4,5,6]])
print(arr2)


# 3-D arrays
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.

arr3 = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
print(arr3)

## Check Number of Dimensions? ##
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

print(f'arr 0 has: {arr.ndim} Dimensions')
print(f'arr 1 has: {arr1.ndim} Dimensions')
print(f'arr 2 has: {arr2.ndim} Dimensions')
print(f'arr 3 has: {arr3.ndim} Dimensions')


# An array can have any number of dimensions.
# When the array is created, you can define the number of dimensions by using the 'ndmin' argument.
# Create an array with 5 dimensions and verify that it has 5 dimensions:

arr5 = np.array([1,2,3,4], ndmin=5)
print(arr5)
print(f'arr 5 has: {arr5.ndim} Dimensions')

# To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.
# Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column

# Access the element on the first row, third column:
# result should be = 3

arrNum = np.array([ [1,2,3,4,50], # first row = index 0
                    [6,7,8,9,10]]) # second row = index 1
                   # 1,2,3,4,5 - columns
                   # 0,1,2,3,4 - indexs

print(arrNum[0, 2])

# Access the element on the second row, 5th column

arrNum2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print(arrNum2[1, -1])
# or 
print(arrNum2[1, 4])


# Access 3-D Arrays
# Access the third element of the second array of the first array:

arrNum3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# another way to look at it :
arrNum3 = np.array([
    # first array
    [[1, 2, 3], 
    # second array
    [4, 
    5, 
    # third element
    6]], 

    [[7, 8, 9], 
    [10, 11, 12]]

    ])

print(arrNum3[0,1,2])

# Slicing 2-D Arrays
arrNum4 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arrNum4[1, 1:4:2])


# From both elements, return index 2:
arrNum5 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arrNum5[0:2, 2])

# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array: 
# result = [[2,3,4],[7,8,9]]

arrNum6 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arrNum6[0:2, 1:4])

# Creating Arrays With a Defined Data Type
# We use the array() function to create arrays, 
# this function can take an optional argument: 'dtype' that allows us to define the expected data type of the array elements:

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

print('\n\n')

arrNum7 = np.array([1, 2, 3, 4], dtype='U1')
print(arrNum7)
