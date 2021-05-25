#!/usr/bin/env python3

import numpy as np

''' single array or vector ''' 
a = np.array([1,2,3])
print('1D array:')
print(a)
print()

''' bidimensional array '''
b = np.array([(1,2,3),(4,5,6)])
print('2D array:')
print(b)
print()

''' array filled with ones '''
ones = np.ones((3, 4))
print(ones)
print()

''' array filled with zeros '''
zeros = np.zeros((3, 4))
print(zeros)
print()

''' array filled with random values '''
random = np.random.random((3, 4))
print(random)
print()

''' empty array '''
empty = np.empty((3, 4))
print(empty)
print()

''' array filled with a specific value '''
full = np.full((3, 4), 25)
print(full)
print()

''' array filled with values with interval values in a range '''
intervals = np.arange(10, 50, 5)
print(intervals)
print()

''' array filled with a specific amount of values in a range '''
fivevaluesbetweentenandfifty = np.linspace(10, 50, 5)
print(fivevaluesbetweentenandfifty)
print()

''' array filled with identity matrix or diagonal values equals 1'''
identity = np.eye(5, 5)
print(identity)
print()

''' array filled with identity matrix or diagonal values equals 1'''
identity2 = np.identity(5)
print(identity2)
print()

''' matrix dimensions function ndim'''
print(identity2.ndim)
print()

''' matrix data type function dtype'''
print(identity2.dtype)
print()

''' matrix size function size'''
print(identity2.size)
print()

''' matrix shape function shape '''
print(identity2.ndim)
print()

''' changing shape to a matrix with reshape function '''
reshapematrix = np.array([(1,2,3),(4,5,6)])
reshapematrix = reshapematrix.reshape(3,2)
print(reshapematrix)
print()

''' taking a specific column values from a matrix '''
reshapematrix = np.array([(1,2,3),(4,5,6)])
print(reshapematrix[0:,2])
print()

''' min value of a vector or matrix '''
reshapematrix = np.array([(1,2,3),(4,5,6)])
print(reshapematrix.min())
print()

''' max value of a vector or matrix '''
reshapematrix = np.array([(1,2,3),(4,5,6)])
print(reshapematrix.max())
print()

''' sum of all values of a vector or matrix '''
reshapematrix = np.array([(1,2,3),(4,5,6)])
print(reshapematrix.sum())
print()

''' square root for every value of a vector or matrix '''
reshapematrix = np.array([(1,2,3),(4,5,6)])
print(np.sqrt(reshapematrix))
print()

''' standard desviation for every value of a vector or matrix '''
reshapematrix = np.array([(1,2,3),(4,5,6)])
print(np.std(reshapematrix))
print()

''' sum of two matrices '''
a = np.array([(1,2,3),(4,5,6)])
b = np.array([(1,2,3),(4,5,6)])
print(a + b)
print()

''' substraction of two matrices '''
a = np.array([(1,2,3),(4,5,6)])
b = np.array([(1,2,3),(4,5,6)])
print(a - b)
print()

''' multiplication of two matrices '''
a = np.array([(1,2,3),(4,5,6)])
b = np.array([(1,2,3),(4,5,6)])
print(a * b)
print()

''' division of two matrices '''
a = np.array([(1,2,3),(4,5,6)])
b = np.array([(1,2,3),(4,5,6)])
print(a / b)
print()


