from tkinter import*
from tkinter import messagebox
def call_me():
    # messagebox.showinfo("success","installation complete")
    # messagebox.showerror("success","installation complete")
    # messagebox.showwarning("success","installation complete")
    # ans=messagebox.askquestion("Exit","Do you really want to exit?")
    ans=messagebox.askyesnocancel("Exit","Do you really want to exit?")
    print(ans)
    if ans:
        root.quit()

root=Tk()

b=Button(root,text="message",command=call_me)
b.pack()
root.mainloop()