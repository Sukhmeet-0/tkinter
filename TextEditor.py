from tkinter import *
from tkinter import filedialog
class textEditor:
    def open_file(self):
        openreturn=filedialog.askopenfile(initialdir="/",title="Select file to open",filetypes=(("text files",".txt"),("all files",".*")))
        if openreturn!=None:
            self.textarea.delete(1.0,END)
            for i in openreturn:
                self.textarea.insert(END,i)



    def __init__(self,master):
        self.master=master
        master.title("TextPad")
        self.textarea = Text(wrap=WORD)
        self.textarea.pack(fill=BOTH,expand=1) 
        
        self.mainmenu=Menu()
        self.master.config(menu=self.mainmenu)
        
        self.filemenu=Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="File",menu=self.filemenu)
        self.filemenu.add_command(label="Open",command=self.open_file)

        self.editmenu=Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="Edit",menu=self.editmenu)


root=Tk()

te=textEditor(root)

root.geometry("700x700+300+120")
root.mainloop()