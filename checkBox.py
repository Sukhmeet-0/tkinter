from tkinter import *

def d():
    print(i.get())

    
root=Tk()

# i=IntVar()
i=StringVar()
c=Checkbutton(root,text="item 1",variable=i,onvalue="checked",offvalue="unchecked")
c.pack()

b=Button(root,text="Click me",command=d)
b.pack()

root.geometry("300x300+120+120")
root.mainloop()