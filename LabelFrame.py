from tkinter import *

root =Tk()

l=LabelFrame(root,text="Input",padx=20,pady=20)
l.pack()

entry=Entry(l)
entry.pack()
root.geometry("400x400+200+200")
root.mainloop()