def add(x,y,z):
    c=x+y+z
    print("Add=",c)

add(2,5,8)

def variablesum(a,*b):
    #print(a)
    #print(b,type(b))
    c=a
    for i in b:
        c=c+i
    print(c)
variablesum(1,2,3,4)

def variablesum1(*b):
    #print(a)
    #print(b,type(b))
    c=0
    for i in b:
        c=c+i
    print(c)
variablesum1(1,2,3,4)