# This is some Special NumPy Array Methods
print("----Zeros----")

import numpy as np
ar_zero=np.zeros(4) # np.zeros is used to create Array filled with Zero
# ar_zero1=np.zeros((3,4))  this line is used to create the dimension we want
print(ar_zero)
#print(ar_zero1)

print("-----Ones------")
ar_one=np.ones(3)
print(ar_one)

print("------Empty------")
ar_emp=np.empty(3)
print(ar_emp)

print("-------RANGE-------")
ar_rng=np.arange(3) # it is same as range function in python. like it give the output which you have taken in the function
print(ar_rng)


print("DIAGONAL")
ar_dia=np.eye(3) # eye function is used to create diagonal elements filled with 1's
print(ar_dia)
ar_dia1=np.eye(3,5)  
print(ar_dia1)

print("____LINSPACE_____")
ar_lin=np.linspace(0,20,num=5) #to print number between
print(ar_lin)

# More Special NumPy Array Methods (continuation of special_arr.py)



print("----FULL----")
ar_full = np.full((2, 3), 7)  # array of given shape filled with any value we want
print(ar_full)

print("----ZEROS_LIKE / ONES_LIKE----")
base = np.array([[1, 2, 3], [4, 5, 6]])
print(np.zeros_like(base))  # zeros with the same shape as base
print(np.ones_like(base))   # ones with the same shape as base

print("----IDENTITY----")
print(np.identity(3))  # square matrix with 1's on the diagonal (like eye, but always square)

print("----DIAG----")
print(np.diag([1, 2, 3]))  # puts the given values on the diagonal

print("----ARANGE WITH STEP----")
print(np.arange(1, 20, 3))  # start, stop (not included), step

print("----ARANGE WITH STEP----")
print(np.arange(1, 20, 3))  # start, stop (not included), step

print("----LOGSPACE----")
print(np.logspace(0, 3, num=4))  # numbers spaced evenly on a log scale: 10^0 to 10^3

print("----RANDOM----")
np.random.seed(42)  # seed makes the random numbers repeatable
print(np.random.rand(3))                # random floats between 0 and 1
print(np.random.randint(1, 10, size=5))  # random integers from 1 to 9
print(np.random.randn(3))               # random numbers from a normal distribution

print("----RESHAPE----")
ar_rs = np.arange(12).reshape(3, 4)  # change the shape without changing the data
print(ar_rs)
print(ar_rs.shape)  # (rows, columns)

print("----FLATTEN----")
print(ar_rs.flatten())  # converts any array back to 1D

print("----TILE & REPEAT----")
print(np.tile([1, 2], 3))    # repeats the whole array: [1 2 1 2 1 2]
print(np.repeat([1, 2], 3))  # repeats each element:    [1 1 1 2 2 2]

print("----SLICING----")
print(ar_rs[1, 2])      # element at row 1, column 2
print(ar_rs[:, 1])      # every row, column 1
print(ar_rs[0:2, 1:3])  # rows 0-1, columns 1-2

print("----ARRAY INFO----")
print(ar_rs.ndim)   # number of dimensions
print(ar_rs.size)   # total number of elements
print(ar_rs.dtype)  # data type of the elements

# CREATING RANDOM NUMBERS
print("Creating RANDOM NUMBERS")

#Rand()

var=np.random.rand(4)  # value  between 0 to 1
print(var)

var1=np.random.rand(2,5)
print(var1)

#Randn()
print("randn() function")
var2=np.random.randn(3)  # value close to 0. either can be negative or positive.
print(var2)