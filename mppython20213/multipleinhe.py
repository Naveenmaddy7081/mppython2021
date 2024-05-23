class A:
    def a(self):
        print("Class A")

class B:
    def b(self):
        print("Class B")

class C(A,B):
    def c(self):
        print("Class C")

cobj=C()
cobj.a()
cobj.b()
cobj.c()