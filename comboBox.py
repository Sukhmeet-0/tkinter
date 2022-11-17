from tkinter import *
from tkinter.ttk import Combobox
def d():
    v=c.get()
    print(v)
root =Tk()
ls=["apple","banana","mango"]
c=Combobox(root,values=ls,height=1,width=15,state="readonly")

c.set("Select")
c.pack()
b=Button(root,text="CLick",command=d)
b.pack()
root.geometry("400x400+120+120")
root.mainloop()