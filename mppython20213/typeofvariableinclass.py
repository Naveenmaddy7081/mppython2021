'''
type of variable:
  1. class variable or static variable
  2. instance variable -- variable declared inside function
'''

class Car:
    wheel=4 # class variable
    def __init__(self):
        print("This is car")
        self.milage=25    #instance variable
        self.company_name="Maruti"   #instance variable

c1=Car()  # automatically call __init
c2=Car()
c3=Car()
Car.wheel=8    # we need class name--class variable
c2.milage=55  # we need object --instance variable
c2.company_name='Tata'
print(c1.milage,c1.company_name,c1.wheel)
print(c2.milage,c2.company_name,c2.wheel)