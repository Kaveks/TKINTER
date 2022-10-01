
from tkinter import *
# Import older version of pillow PIL to use image files

from PIL import ImageTk,Image

Image_viewer = Tk()
Image_viewer.title("IMAGES IN TK")
Image_viewer.geometry("670x575")
#icon
Image_viewer.iconbitmap('ICON/icon.ico')
 
#images

img1=ImageTk.PhotoImage(Image.open('Images/Blue Dun.jpg'))
img2=ImageTk.PhotoImage(Image.open('Images/Black Gnat.jpg'))
img3=ImageTk.PhotoImage(Image.open('Images/Blue Wing Olive.jpg'))
img4=ImageTk.PhotoImage(Image.open('Images/ComparaDun.jpg'))
img5=ImageTk.PhotoImage(Image.open('Images/Disco Midge.jpg'))
img6=ImageTk.PhotoImage(Image.open('Images/Elk Caddis.jpg'))

# list the images on a Python list
image_list = [img1, img2, img3, img4, img5, img6]


#display the 1st image=img1
img_label = Label(image=img1)
img_label.grid(row=0,column=0 ,columnspan=3)

# status bar label
status =Label(Image_viewer,text ="Image 1 of"+str(len(image_list)),bg= "blue",bd=3,relief=SUNKEN,anchor=E)


#define buttons functionality

def forward(Image_Number):
    global img_label
    global b_forward
    global b_backward
    
    img_label.grid_forget()# forget previous image whe we click forward
    img_label=Label(image=image_list[Image_Number-1])#Image_Number-1 since we gave forward(2)
    # 1st image =img1=index(0), next=img2 =index(1) which is Image_Number-1=1
    b_forward=Button(Image_viewer,text=">>" ,bg = "green",fg="black",command=lambda: forward(Image_Number+1))
    b_backward = Button(Image_viewer,text="<<",fg="black",bg="green",command =lambda: backward(Image_Number-1))  
    
    
    if Image_Number==6:
        b_forward=Button(Image_viewer,text=">>" ,bg = "green",fg="black",state=DISABLED)
    
    
    img_label.grid(row=0,column=0 ,columnspan=3)
    b_forward.grid(row =1,column=1)
    b_backward.grid(row =1,column=0)
    
    # Update status bar when clicking forward
    status =Label(Image_viewer,text ="Image " + str(Image_Number) + "of" +str(len(image_list)),bg= "blue",bd=3,relief=SUNKEN,anchor=E)
    status.grid(row=2, column=0,columnspan=3,sticky=W+E)
    return


def backward(Image_Number):
    global img_label
    global b_forward
    global b_backward
    
    img_label.grid_forget()# forget previous image when we click backward
    img_label=Label(image=image_list[Image_Number-1])#Image_Number-1 since we gave forward(2)
    # 1st image =img1=index(0), next=img2 =index(1) which is Image_Number-1=1
    b_forward=Button(Image_viewer,text=">>" ,bg = "green",fg="black",command=lambda: forward(Image_Number+1))
    b_backward = Button(Image_viewer,text="<<",fg="black",bg="green",command =lambda: backward(Image_Number-1))  
    
    
    if Image_Number==1:
        b_backward=Button(Image_viewer,text=">>" ,bg = "green",fg="black",state=DISABLED)
    
    
    img_label.grid(row=0,column=0 ,columnspan=3)
    b_forward.grid(row =1,column=1)
    b_backward.grid(row =1,column=0)
    
    # update status bar
    status =Label(Image_viewer,text ="Image " + str(Image_Number) + "of" +str(len(image_list)),bg= "blue",bd=3,relief=SUNKEN,anchor=E)
    status.grid(row=2, column=0,columnspan=3,sticky=W+E)
    return

# buttons
b_forward=Button(Image_viewer,text=">>" ,bg = "green",fg="black",command=lambda: forward(2))
b_quit = Button(Image_viewer,text='Quit',bg="red",command=Image_viewer.quit)
b_backward = Button(Image_viewer,text="<<",fg="black",bg="green",command =lambda: backward(6))

#display
b_forward.grid(row =1,column=1)
b_quit.grid(row =1,column=2)
b_backward.grid(row =1,column=0)


# display status bar
status.grid(row=2, column=0,columnspan=3,sticky=W+E)


Image_viewer.mainloop()