from tkinter import *
def click_me():
    print(spin1.get())
root =Tk()

spin1=Spinbox(root,from_=0,to=5)
spin1.pack()

b=Button(root,text="Print",command=click_me)
b.pack()

root.mainloop()