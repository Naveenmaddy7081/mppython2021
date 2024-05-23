'''
factorial of 5= 1*2*3*4*5
                5*4*3*2*1
fibbonacci series 1,2,3,5,8....
'''
n=int(input("enter any number for which u want factorial"))
i=1
f=1
while i<=n:
    f=f*i
    i=i+1
print("Factorial=",f)