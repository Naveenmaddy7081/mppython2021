from tkinter import *
from tkinter import colorchooser
root=Tk()
def color_chooser():
    c=colorchooser.askcolor()
    print(c)
    print(c[0])
    print(c[1])
    root.config(bg=c[1])
root.title("Color chooser")
root.wm_iconbitmap('note.ico')
btn=Button(root,text="Color Chooser",command=color_chooser)
btn.pack()
root.geometry("400x400+120+120")
root.mainloop()
