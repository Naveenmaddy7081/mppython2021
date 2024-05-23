from tkinter import *
root=Tk()

label1=Label(root,text=" Enter First Number ",bg="black",fg="white",
             font=("Comic Sans Ms",15))
label1.grid(row=0,column=0)
first=IntVar()
txt=Entry(root,font=("Comic Sans Ms",15),textvariable=first)
txt.grid(row=0,column=1)

label2=Label(root,text="Enter Second Number",bg="black",fg="white",
             font=("Comic Sans Ms",15))
label2.grid(row=1,column=0)
second=IntVar()
txt1=Entry(root,font=("Comic Sans Ms",15),textvariable=second)
txt1.grid(row=1,column=1)

btn=Button(root,text="Add",bg="Red",fg="yellow",
             font=("Comic Sans Ms",15))
btn.grid(row=2,columnspan=2)

second=IntVar()
txt1=Entry(root,font=("Comic Sans Ms",15),textvariable=second)
txt1.grid(row=1,column=1)
#root.geometry("600x500+250+150")
root.mainloop()