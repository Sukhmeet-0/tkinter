from tkinter import *
root=Tk()
f=Frame(root)
s=Scrollbar(f)
s.pack(side=RIGHT,fill=Y)

l=Listbox(f,yscrollcommand=s.set)
l.pack(side=LEFT)
for i in range(1,100):
    l.insert(END,"List "+str(i))
s.config(command=l.yview)
f.pack()
root.geometry("300x300+300+300")
root.mainloop()