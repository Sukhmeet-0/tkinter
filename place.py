from tkinter import *
root=Tk()

label=Label(root,text="Label 1")
label2=Label(root,text="Label 2")
label.place(x=10,y=10)
label2.place(x=10,y=40)
root.geometry("300x300+120+120")

root.mainloop()