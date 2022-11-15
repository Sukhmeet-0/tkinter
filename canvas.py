from tkinter import *

root=Tk()

can=Canvas(root,width=200,height=200,bg='white')
can.pack()

#line
line=can.create_line(0,0,200,200)
line=can.create_line(200,0,0,200,fill="red")

#arc
arc=can.create_arc(100,100,200,200,extent=120)

#image
# img=PhotoImage(file="C:\\Users\\sukhm\\OneDrive\\Documents\\mr.png")
# can.create_image(0,0,image=img,anchor=NW)
# root.geometry("400x400+120+120")

#rectangle
rect=can.create_rectangle(10,10,100,100,fill="yellow")

#oval
ov=can.create_oval(10,10,100,100,fill="red",outline="blue")

#polygon
points=[10,10,100,150,150,180,10,10]
can.create_polygon(points,fill="green",outline="Red",width=4)

root.title("Canvas")
root.mainloop()