from numpy import *
arr=array([
    [1,2,3],
    [4,5,6],
    [8,7,9],
    [4,4,4]
])
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
# convert 2d array into one d array
arr2=arr.flatten()
print(arr2)
print(arr2.ndim)

arr3=arr2.reshape(3,4)
print(arr3)
print(arr3.ndim)

arr4=arr2.reshape(2,2,3)
print(arr4)
print(arr4.ndim)