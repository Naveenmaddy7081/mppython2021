'''
An array is collection of similar data type.

'''
import time
#import array
#import array as m
from array import *
a=array('f',[1,2,3,4,5,6,8.7])
print(a)
print(a.typecode)
print(a.buffer_info())
#a.reverse()
print(a)
print(len(a))
#print(a[0])

for i in range(len(a)):
    print(a[i])


j=0
while j<len(a):
    print(a[j])
    j=j+1

for k in a:
    print(a)
    time.sleep(1)

d=array('u',['a','b','c','d'])
print(d)