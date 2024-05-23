from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.config(bg='yellow')
exit_image=ImageTk.PhotoImage(Image.open('images/3.png'))
btn3=Button(root,text="Exit",image=exit_image,
           command=quit)
btn3.pack()
root.resizable(0,0)
root.geometry("400x400+300+150")
root.mainloop()