from numpy import *
a=array([
    [1,3,5],
    [3,5,7],
    [4,6,8]
])
print(a)
b=array([
    [1,22,5],
    [3,7,7],
    [45,6,8],

])

print(b)

#print(a+b)

'''
2*3 r c
3*2 r c

2*2

'''

c=dot(a,b)
print(c)

d=a@b
print(d)

print(a.transpose())
print(diagonal(a))
print(a.min())
print(a.max())
