from tkinter import *
from tkinter import simpledialog
def get_me():
    s=simpledialog.askstring("Input String","please enter your name: ")
    print(s)
root =Tk()
b=Button(root,text="Poppup", command=get_me)
b.pack()
root.mainloop()