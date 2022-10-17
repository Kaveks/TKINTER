from tkinter import *


win=Tk()
win.title("Radio Buttons")
win.iconbitmap("ICON/icon.ico")
win.geometry("400x600")


frame=LabelFrame(win,borderwidth=5,padx=20,pady=20,height=600,width=400)
frame.place(anchor='center', relx=0.5, rely=0.5,bordermode=OUTSIDE)
# define tkinter variable
lang =StringVar()

# set the default choice in the radio buttons
lang.set("None selected")


# define a tuple of tuples of radio choices
programming_lang=(
    ("Python","Python"),
    ("Java","Java"),
    ("C++","C++"),
    ("C#","C#"),
    ("C","C"),
    ("R","R-Programming"),
    ("None selected","None selected"),
)

# iterate in the tuple of tuples,note options and language iterables which
# are the two value strings of the tuple eg ("Python","Python")
for Options,language in programming_lang:
    Radiobutton(frame,text=Options,variable=lang,value=language).pack(anchor=W)

# button functionality when clicked val=lang.get()in the button command
def clicked(val):
    R_label=Label(frame,text=val)
    R_label.pack(anchor=W)

# create a label of a radio choice and display on the left hand
R_label=Label(frame,text=lang.get())
R_label.pack(anchor=W)

#create button and display on the left hand
click_button=Button(frame ,fg="white",bg="blue",borderwidth=10,text="Select",command=lambda:clicked(lang.get())).pack(anchor=W)

# display frame 
frame.grid(row=0,column=0,padx=10,pady=10,columnspan=1)


win.mainloop()