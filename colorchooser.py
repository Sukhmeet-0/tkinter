from tkinter import *
from tkinter import colorchooser
def c():
    clr=colorchooser.askcolor(title="Select color")
    print(clr)
    root.configure(background=clr[-1])
root=Tk()

b=Button(root,text="Colors",command=c)
b.pack()
root.geometry("300x300")
root.mainloop()