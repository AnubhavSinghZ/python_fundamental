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

