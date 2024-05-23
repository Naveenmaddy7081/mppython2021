y=20 # global variable
x=50 # global
def msg():
    x=10  # x is local variable
    global z # this z is global variable
    z=10 # declare local but behaves as global
    print("X inside  function=",x)
    print("Y inside function=",y)
    # if i want to access global varibale with the same name
    d=globals()['x']
    print("d=x=",d)
msg()
print("Y=",y)
print("x=",x)
print("Z =",z)