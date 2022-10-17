from tkinter import *
from tkinter import messagebox


win=Tk()
win.title("message")
win.iconbitmap("ICON/icon.ico")
win.geometry("400x600")


# there are several messages byb tkinter as follows:
#1 showinfo
#2 showwarning
#3 showerror
#4 askquestion
#5 askokcancel
#6 askyesno  all implemented as follows.

def inf():
    messagebox.showinfo("Information","Hello World")
    
    return

Button(win,text="Info",command =inf,borderwidth=5).grid(row=0,column=0)



def warn():
    messagebox.showwarning("Warning","This is dangerous")
    
    return
Button(win,text="Warn",borderwidth=5,command =warn).grid(row=1,column=0)

def err():
    messagebox.showerror("error","This is an error")
    
    return
Button(win,text="Error",borderwidth=5,command =err).grid(row=2,column=0)

def quiz():
    messagebox.askquestion("ask"," Is your name patrick?")
    response=messagebox.askquestion("ask","Is Your name patrick")
    if response=='yes':
        Label(win,text="You clicked yes!").grid(row=3,column=1)
    else:
        Label(win,text="You clicked no!!").grid(row=3,column=1)
    return
Button(win,text="question",borderwidth=5,command =quiz).grid(row=3,column=0)

def ask():
    response=messagebox.askokcancel("ask","I am through")
    if response==1:
        Label(win,text="You clicked yes!").grid(row=4,column=1)
    else:
        Label(win,text="You clicked no!!").grid(row=4,column=1)
    
    return
Button(win,text="ok /cancel",borderwidth=5,command =ask).grid(row=4,column=0)


def yesorno():
    response=messagebox.askyesno("ask","Is it yes or no")
    if response==1:
        Label(win,text="You clicked yes!").grid(row=5,column=1)
    else:
        Label(win,text="You clicked no!!").grid(row=5,column=1)
    
    
    return
Button(win,text="yes/no",borderwidth=5,command =yesorno).grid(row=5,column=0)



win.mainloop()