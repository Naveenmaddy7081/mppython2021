from tkinter import *
root=Tk()
def open_window():
    top=Toplevel(root)
    top.title("Child Window")
    btn_destroy = Button(top, text="close", command=top.destroy)
    btn_destroy.pack()
    top.geometry("400x400+150+150")
root.title("Main Window")
btn=Button(root,text="open new window",command=open_window)
btn.pack()
btn_close=Button(root,text="Quit",command=quit)
btn_close.pack()
root.geometry("400x400+150+150")
root.mainloop()