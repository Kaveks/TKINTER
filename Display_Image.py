
from tkinter import *
# Import older version of pillow PIL to use image files

from PIL import ImageTk,Image

root = Tk()
root.title("IMAGES IN TK")
#icon
root.iconbitmap('C:/Users/DELL/Documents/PROGRAMMING/GitHub/TKINTER/ICON/icon.ico')
 
#image
img1=ImageTk.PhotoImage(Image.open('C:/Users/DELL/Documents/PROGRAMMING/GitHub/TKINTER/Images/Blue Dun.jpg'))

img_label = Label(image=img1)
img_label.pack()



# quit button
b_quit = Button(root,text='Quit',bg="red",command=root.quit)
b_quit.pack()


root.mainloop()