# create an entry on the window with a button to execute a command
from tkinter import *


root =Tk()

entry1 = Entry(root,width=50,borderwidth=10)#create entry
entry1.pack()#display entry


# create a function to execute a command on a button click
def entryfunc():
    name =entry1.get()# get whatever entry in entry1 variable
    greetings = f"hello!  {name}"# concatenate using string formatter
    label1 = Label(root ,text=greetings)# create label to display entry content up on clicks
    label1.pack()# display label
    return

button_entry1=Button(root,text = "run",padx=5,pady=2,fg ="red",bg="blue",command=entryfunc )# create a button
button_entry1.pack()#display entry
root.mainloop()