from numpy import *
arr=array([1,2,3,4,5,6])
print(arr)
arr2=arr*5
print(arr2)
arr3=array([2,5,3,4,7,8])
print(arr+arr3)

sum1=0
for i in arr3:
    sum1=sum1+i
    #print(i)
print("Sum of Marks=",sum1)

print(sum(arr3))
print(max(arr3))

