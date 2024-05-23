def msg():
    print("Good Morning")

def add(x,y):
    print(x+y)

def sub(c,d):
    print(c-d)

print(__name__)  #special variable which is already defined

if __name__=='__main__':
    def speak():
        print("This is original file")
    speak()
'''sub(50,5)
add(4,6)
msg()
'''