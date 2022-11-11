from tkinter import *

root =Tk()
one =Label(root,text="One",bg="red")
two =Label(root,text="two",bg="green")
three =Label(root,text="three",bg="blue")

one.pack(fill=X)
two.pack(fill=X)
three.pack(side=LEFT,fill=Y)

root.mainloop()