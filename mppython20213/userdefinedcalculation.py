f=int(input("Enter the first number"))
s=int(input("Enter the Second number"))
print("Enter A for add S for Sub")
user_input=input("enter your Choice")[0]
print(user_input)
#print(user_input[0])

if user_input=='a' or user_input=='A':
    print("Add=",f+s)
elif user_input=='s' or user_input=='S':
    print("Sub=",f-s)
else:
    print("Bhai Zyada hosiyar mat bano jo bola wahi karo")

