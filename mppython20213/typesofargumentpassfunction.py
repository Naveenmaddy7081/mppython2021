'''
Types of actual argument to function
1. positional argument
2. keyword argument
3. default argument
4. variable length argument (*)
5. keyword variable length argument
'''
#1. positional
def person(name,age):
    print("Name=",name)
    age=age+10
    print("Age=",age)

person('Ashwani',38)
#person(55,'rohit')
#2. keyword argument
person(name='ram',age=35)
#a=500
#b='ttt'
#person(age=a,name=b)
person(age=18,name='vishal')

#3. default argument
def getpersondata(name,age=18):  #default argument age=18
    print("Name=", name)
    print("Age=", age)

getpersondata(name='sapana')
getpersondata(name='bandana',age=15)