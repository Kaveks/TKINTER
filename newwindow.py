from tkinter import *

# Import older version of pillow PIL to use image files

from PIL import ImageTk,Image
from tkinter import filedialog

# create the main window
window1 = Tk()
window1.title("The origin window")
#icon
window1.iconbitmap('ICON/icon.ico')
 
 
#create a new window in the main window

def new():
    global img1
    window2=Toplevel()
    window2.title("new window")
    #open a folder using filedialog.askopenfilename
    window2.filename=filedialog.askopenfilename(initialdir="LEARN_TKINTER/Images",title="select a file",filetypes=(("png files","*.png"),("all files","*.*")))  # type: ignore
    # open a file in this case png or all files
    img1=ImageTk.PhotoImage(Image.open(window2.filename))  # type: ignore
    img_label = Label(window2,image=img1)
    img_label.pack()
    button2=Button(window2,text="close window",command=window2.destroy)
    button2.pack()


button1= Button(window1,text="new window",command=new)
button1.pack()


window1.mainloop()