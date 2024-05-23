h=int(input("enter the marks of hindi"))
e=int(input("enter the marks of english"))
m=int(input("enter the marks of math"))
s=int(input("enter the marks of science"))
a=int(input("enter the marks of art"))
total_obt_marks=h+e+m+s+a
print("Total marks obtained=",total_obt_marks)

per=(total_obt_marks*100)/500
print("Percentage=",per)

if per<33:
    print("You are Fail")
elif per>=33 and per<45:
    print("You are Passed Third division")
elif per>=45 and per<60:
    print("You are Passed second division")
elif per>=60:
    print("You are Passed First division")