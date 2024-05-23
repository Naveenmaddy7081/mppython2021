from tkinter import *
from tkinter.ttk import Combobox
root=Tk()
def combo_get():
    print(c.get())
l=['CS','EC','IT','CIVIL Engineering']
#l=list(range(1,32))
c=Combobox(root,values=l,height=3,width=20)
c.set("Select Your Branch")
c.pack()
btn=Button(root,text="get Combo box data",command=combo_get)
btn.pack()
root.geometry("400x400+120+120")
root.mainloop()