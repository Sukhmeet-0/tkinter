from tkinter import *

root =Tk()
def call_me(event):
    print("I am called")

# button=Button(root,text="Click me",command=call_me)
button=Button(root,text="Click me")
button.bind("<Button-1>",call_me)
button.pack()
root.mainloop()