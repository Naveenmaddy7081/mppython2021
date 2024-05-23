from array import *

marks=array('i',[]) # to create an empty array
n=int(input("How many students marks u want to store"))
print("No of students=",n)

for i in range(n):
    x=int(input("Enter the marks of student"))
    marks.append(x)

print(marks)

search=int(input("Enter the marks of student u want to find"))

loc=0
for j in marks:
    if j==search:
        print("Item found at location=",loc+1)
        break
    loc=loc+1
else:
    print("item not found")


print(marks.index(search))