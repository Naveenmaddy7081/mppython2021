from tkinter import *
root=Tk()
root.config(bg='yellow')
def list_get():
    get_data=l.curselection()
    print(get_data)
    for i in get_data:
        print(l.get(i))

def list_delete():
    r=l.curselection()
    for i in r:
        print(l.delete(i))
l=Listbox(root,selectmode=BROWSE)
l.insert(1,"CS")
l.insert(2,'EC')
l.insert(3,'CIVIL')
l.insert(4,'ME')
l.pack()
btn=Button(root,text="get Combo box data",command=list_get)
btn.pack()

btn_delete=Button(root,text="Delete list Data",command=list_delete)
btn_delete.pack()
root.geometry("400x400+120+120")
root.mainloop()