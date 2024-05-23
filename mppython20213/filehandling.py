f=open('ram.txt',"r")
print(f)

# to read the contents of file

for data in f:
    print(data,end="")

'''f1=open('Mohan.txt','a')
print(f1)
msg=input("Enter the text u want to write in a file")

f1.write(msg)
'''
f4=open('myturtle.gif','wb')
f3=open('turtle.gif','rb')
for data in f3:
    print(data)
    f4.write(data)