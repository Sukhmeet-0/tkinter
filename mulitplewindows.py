from tkinter import *
def open_window():
    top=Toplevel()

root=Tk()

b=Button(root,text="open window",command=open_window)
b.pack()

root.mainloop()