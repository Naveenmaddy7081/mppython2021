'''i=63
while i<=630:
    print(i," ",end="")
    i=i+63
'''
'''
2*1=2
2*2=4
2*3=6
2*4=8
...
2*10=20
here 2 is the no input by user
and 1,2,3...10 
'''
n=int(input("Enter the number for which u want table"))
i=1
while i<=10:
    t=n*i
    print(n,"*",i,"=",t)
    i=i+1