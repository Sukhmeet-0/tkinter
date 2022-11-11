from tkinter import *

root =Tk()

name=Label(root,text="Username")
pas=Label(root,text="Password")
e1=Entry(root)
e2=Entry(root)

name.grid(row=0,column=0,sticky=E)
e1.grid(row=0,column=1)
pas.grid(row=1,column=0)
e2.grid(row=1,column=1)

c=Checkbutton(root,text="Keep me logged in")
c.grid(columnspan=2)
root=mainloop()