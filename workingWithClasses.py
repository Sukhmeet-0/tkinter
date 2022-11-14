from tkinter import *
class myButtons:
    def __init__(self,master):
        self.printButton=Button(master,text="Print",command=self.printMessage)
        self.printButton.pack(side=LEFT)
        self.quit=Button(master,text="Quit",command=master.quit)
        self.quit.pack(side=LEFT)
    def printMessage(self):
        print("Printing message")

root =Tk()

b=myButtons(root)
root.mainloop()