from tkinter import *
def pr():
    # r=t.get(1.0,END)
    r=t.selection_get()
    pos=t.search(r,1.0,stopindex=END)
    print(r)
    print(pos)
def c():
    t.delete(1.0,END)
root =Tk()
t=Text(root,width=50,height=10,padx=10,pady=10,wrap=WORD,bd=2,selectbackground="blue",selectforeground="green")
t.insert(INSERT,"Hello...")
t.pack()
b=Button(root,text="Print",command=pr)
b.pack()
bb=Button(root,text="Clear",command=c)
bb.pack()
root.geometry("500x500+200+200")
root.mainloop()