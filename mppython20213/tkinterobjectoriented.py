from tkinter import *
class MyWindow:
    def msg(self):
        print("Good morning")
    def __init__(self,window):
        self.button=Button(window,text="Click me",command=self.msg,
                           fg="red",bg="yellow")
        self.button.pack()

root=Tk()
window=MyWindow(root)
root.title("My Object oriented Window")
root.geometry("400x400+150+150")
root.mainloop()