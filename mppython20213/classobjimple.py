class Student:
    def student_info(self):
        print("Ram",55)

# how to create object of class
s=Student()
print(type(s))
Student.student_info(s)
# but this fuction can be accessed as
s.student_info()
a=5
print(type(a))
