from tkinter import *
from tkinter import messagebox
def cm(event=""):
    messagebox.showinfo("trying","something important")
root=Tk()
root.bind('<Control-c>',cm)
b=Button(root,text="call me",command=cm)
b.pack()
root.geometry("300x300")
root.mainloop()