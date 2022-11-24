from tkinter import *
from tkinter import filedialog
# def open_file():
#     rs=filedialog.askopenfile(initialdir="/",title="Select file",filetypes=(("text files",".txt"),("all files",".*")))
#     print(rs)
#     for  c in rs:
#         print(c)
def save_file():
    f=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if f is None:
        return
    else:
        f.write("Hello how are you?")
        f.close()
root= Tk()

b=Button(root,text="Save file",command=save_file)
b.pack()
root.geometry("300x300")
root.mainloop()
