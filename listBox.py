from tkinter import *
def print_me():
    ci=l.curselection()
    for i in ci:
        print(l.get(i))
def delete_me():
    ci=l.curselection()
    for i in ci:
        print(l.delete(i))
root =Tk()
# l=Listbox(root,width=10,height=10,selectmode=BROWSE)
# l=Listbox(root,width=10,height=10,selectmode=SINGLE)
# l=Listbox(root,width=10,height=10,selectmode=MULTIPLE)
l=Listbox(root,width=10,height=10,selectmode=EXTENDED)
l.insert(1,"c++")
l.insert(2,"Python")
l.insert(3,"Java")
l.pack()
b=Button(root,text="Click",command=print_me)
b.pack()
bb=Button(root,text="Delete",command=delete_me)
bb.pack()
root.geometry("400x400+120+120")
root.mainloop()