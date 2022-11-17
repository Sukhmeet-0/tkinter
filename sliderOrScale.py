from tkinter import *

root =Tk()

s=Scale(root,from_=0,to=100,orient=HORIZONTAL,length=300,width=10,sliderlength=50)
s.set(50)
s.pack(side=LEFT,fill=Y)
print(s.get())

root.geometry("300x300+120+120")
root.mainloop()