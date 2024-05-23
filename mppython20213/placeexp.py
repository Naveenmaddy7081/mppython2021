from tkinter import *
root=Tk()

def add():
    a=first.get()
    #print(a)
    b=second.get()
    #print(b)
    c=a+b
    #print("Add=",c)
    result1.set(c)
label1=Label(root,text="Enter First Number",bg="black",fg="white",
             font=("Comic Sans Ms",15))
label1.place(x=50,y=50)

first=IntVar()
txt=Entry(root,font=("Comic Sans Ms",15),bd="13",textvariable=first)
txt.place(x=300,y=50)

label2=Label(root,text="Enter Second Number",bg="black",fg="white",
             font=("Comic Sans Ms",15))
label2.place(x=50,y=150)

second=IntVar()
txt1=Entry(root,font=("Comic Sans Ms",15),bd="13",textvariable=second)
txt1.place(x=300,y=150)

btn=Button(root,text="Add",bg="Red",fg="yellow",
             font=("Comic Sans Ms",15),command=add)
btn.place(x=250,y=250)

result1=IntVar()
result=Entry(root,font=("Comic Sans Ms",15),bd="13",textvariable=result1)
result.place(x=250,y=325)
root.geometry("600x500+250+150")
root.mainloop()