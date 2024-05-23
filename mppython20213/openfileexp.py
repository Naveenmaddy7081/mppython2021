from tkinter import *
from tkinter import filedialog
root=Tk()

def open_file():
    r=filedialog.askopenfile(initialdir="/",title="Open File",
                 filetype=(('All Files','*.*'),('Text File','*.txt')))
    print(r)
    for data in r:
        print(data,end="")
        txt.insert(INSERT,data)
def Save_file():
    f=filedialog.asksaveasfile(mode="w",defaultextension="*.txt")
    f.write('Welcome')
    f.close()
    print(f)
txt=Text(root)
txt.pack()
btn=Button(root,text="Open File",command=open_file)
btn.pack()
btn2=Button(root,text="Save File",command=Save_file)
btn2.pack()
root.geometry("600x600+120+120")
root.mainloop()
