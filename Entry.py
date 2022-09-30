# create an entry on the window with a button to execute a command
from tkinter import *


root =Tk()

entry1 = Entry(root,width=50,borderwidth=10)#create entry
entry1.pack()#display entry


button_entry1=Button(root,text = "run",padx=5,pady=2,fg ="red",bg="blue", )# create a button
button_entry1.pack()#display entry
root.mainloop()