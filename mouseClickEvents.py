from tkinter import *
root =Tk()
def rightClick(event):
    print("RIght click")
def leftClick(event):
    print("Left click")
def middleClick(event):
    print("Middle button")

frame=Frame(root,width=300,height=300)
frame.bind("<Button-1>",leftClick)
frame.bind("<Button-2>",middleClick)
frame.bind("<Button-3>",rightClick)
frame.pack()
root.mainloop()


# pyinstaller --onefile -w --icon=iconPath name.py     for turning python file to exe