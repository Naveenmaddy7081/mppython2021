from tkinter import *
from tkinter import simpledialog
root=Tk()
root.config(bg='yellow')
def input_data():
    sum=0
    for i in range(5):
        s=simpledialog.askinteger("Enter Marks of Students","Enter Marks")
        sum=sum+s
    print(sum)

btn=Button(root,text="getData",command=input_data)
btn.pack()
root.geometry("400x400+120+120")
root.mainloop()