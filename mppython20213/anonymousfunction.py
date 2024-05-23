# function without name is called anomymous function
# to make a anonymous function
# function should have only one expression but it can take any number
#of argument

'''
def add(a,b):
    c=a+b
    print(c)
add(4,5)
'''

def add(a,b):
    return a+b  # this function has only one expression
print(add(6,7))


ankit=lambda a,b:a+b  # anomymous function

result=ankit(55,45)
print(result)

d=ankit(4,5)
print(d)

mul=lambda a,b:a*b
g=mul(4,6)
print(g)