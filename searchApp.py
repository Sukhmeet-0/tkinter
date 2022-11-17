from tkinter import *
import wikipedia

def get_me():
    
    ta.delete(1.0,END)
    ev = entry.get()
    try:
        tav = wikipedia.summary(ev)
    except:
        print("Check your input or internet connection!!")
    ta.insert(INSERT,tav)

root =Tk()
root.title("Search App")


f1=Frame(root)
entry=Entry(f1)
entry.pack()
b=Button(f1,text="Search",command=get_me)
b.pack()
f1.pack(side=TOP)

f2=Frame(root)
scroll=Scrollbar(f2)
scroll.pack(side=RIGHT,fill=Y)
ta=Text(f2,width=50,height=20,yscrollcommand=scroll.set,wrap=WORD)
ta.pack()
scroll.config(command=ta.yview)
f2.pack()

root.geometry("500x500+250+250")
root.mainloop()