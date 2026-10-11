import numpy as np

# 1D NumPy Array
x = np.array([1, 2, 3, 4, 5, 6])
print("NumPy 1D:", x)
print("Type:", type(x))

# 2D NumPy Array (Matrix with 2 rows and 3 columns)
y_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("\nNumPy 2D Array Shape:", y_2d.shape)
print(y_2d)

# 3D NumPy Array (Collection of 2D matrices)
y_3d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[8, 9, 10], [11, 12, 13]]
])
print("\nNumPy 3D Array Shape:", y_3d.shape)
print(y_3d)

# Python List Example
y_list = [1, 2, 3, 4, 5, 6]
print("\nPython List:", y_list)
print("Type:", type(y_list))


# NumPy Datatype

#import numpy as np
var=np.array([1,2,3,4,12,13,14,15]) # INT DATATYPE
print("Data Tpye: ", var.dtype)

var1=np.array([1.2,3.7, 4.5,7.0])  # FLOAT DATATYPE
print(var1.dtype)

str1=np.array(["a","b", "c"]) # U1 (string) DATATYPE
print(str1.dtype)

# CONVERSION FROM ONE DATATYPE TO ANOTHER DATATYPE

a=np.array([1,2,3,4],dtype=np.int8) #int64 to int8
print("DATA TYPE :", a.dtype)
print(a)

a1=np.array([1,2,3,4],dtype="f") # changing in shortcut method by using only one word
print("a1 DATA TYPE :", a1.dtype)
print(a)


b=np.array([1,2,3,4]) # changing in shortcut method by using only one word
new=np.float32(b)
new1=np.int_(new)
print(" b DATA TYPE :", b.dtype)
print(b)
print(new)
print(new1)
print("new1 Data Type:",new1.dtype)

# Direct Convert

c=np.array([1,2,3,4])
new2=c.astype(float)
print(c)
print(new2)

# **Arithmetic Operation**

var=np.array([1,2,3,4])
varadd= var + 3
print("Add:",varadd)

abc=np.array([1,2,3,4])
xyz=np.array([1,2,3,4])
varadd1=abc+xyz
print("add two array:",varadd1)


