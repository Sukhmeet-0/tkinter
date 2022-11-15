from tkinter import *
root=Tk()

r1=Radiobutton(root,text="Male",value=1)
r2=Radiobutton(root,text="Female",value=2)

r1.pack()
r2.pack()

root.geometry("300x300+120+120")
root.mainloop()