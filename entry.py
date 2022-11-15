from tkinter import *
def click_me():
    # s=entry.get()
    # print(s)
    # if s=="sukhmeet":
    #     print("Success!")
    # else:
    #     print("Failure")
    s1=s.get()
    print(s1)

root=Tk()

s=StringVar()

entry=Entry(root,textvariable=s)
s.set("Welcome")

entry.pack()

b=Button(root,text="Click",command=click_me)
b.pack()

root.geometry("300x300+120+120")
root.mainloop()