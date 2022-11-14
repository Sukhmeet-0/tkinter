from tkinter import *
root =Tk()
def doNothind():
    print("i Wont")
mainMenu=Menu(root)
root.config(menu=mainMenu)


fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label='File',menu=fileMenu)


editMenu=Menu(mainMenu)
mainMenu.add_cascade(label='Edit',menu=editMenu)


saveMenu=Menu(mainMenu)
mainMenu.add_cascade(label='save',menu=saveMenu)


closeMenu=Menu(mainMenu)
mainMenu.add_cascade(label='close',menu=closeMenu)



fileMenu.add_command(label="New Project",command=doNothind)
fileMenu.add_separator()
fileMenu.add_command(label="Open Project",command=doNothind)
fileMenu.add_separator()
fileMenu.add_command(label="Save Project",command=doNothind)
fileMenu.add_separator()
fileMenu.add_command(label="Close Project",command=doNothind)
fileMenu.add_separator()

saveMenu=Menu(fileMenu)
fileMenu.add_cascade(label="save",menu=saveMenu)
saveMenu.add_command(label="Save as",command=doNothind)
root.mainloop()