# display content on a window using grid system.

from tkinter import *


root = Tk()

label1 = Label(root, text="hello world")
label2 = Label(root,text="My name is Patrick")

label1.grid(row =0,column=0)
label2.grid(row =1,column=0)
root.mainloop()