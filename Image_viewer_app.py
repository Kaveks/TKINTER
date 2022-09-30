
from tkinter import *
# Import older version of pillow PIL to use image files

from PIL import ImageTk,Image

Image_viewer = Tk()
Image_viewer.title("IMAGES IN TK")
Image_viewer.geometry("700x550")
#icon
Image_viewer.iconbitmap('ICON/icon.ico')
 
#images

img1=ImageTk.PhotoImage(Image.open('C:Images/Blue Dun.jpg'))
img2=ImageTk.PhotoImage(Image.open('C:Images/Black Gnat.jpg'))
img3=ImageTk.PhotoImage(Image.open('C:Images/Blue Wing Olive.jpg'))
img4=ImageTk.PhotoImage(Image.open('C:Images/ComparaDun.jpg'))
img5=ImageTk.PhotoImage(Image.open('C:Images/Disco Midge.jpg'))
img6=ImageTk.PhotoImage(Image.open('C:Images/Elk Caddis.jpg'))

# list the images on a Python list
image_list = [img1, img2, img3, img4, img5, img6]


#display the 1st image=img1
img_label = Label(image=img1)
img_label.grid(row=0,column=0 ,columnspan=3)

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
    b_forward.grid(row =1,column=2)
    b_backward.grid(row =1,column=0)
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
    b_forward.grid(row =1,column=2)
    b_backward.grid(row =1,column=0)
    return

# buttons
b_forward=Button(Image_viewer,text=">>" ,bg = "green",fg="black",command=lambda: forward(2))
b_quit = Button(Image_viewer,text='Quit',bg="red",command=Image_viewer.quit)
b_backward = Button(Image_viewer,text="<<",fg="black",bg="green",command =lambda: backward(6))

#display
b_forward.grid(row =1,column=2)
b_quit.grid(row =1,column=3)
b_backward.grid(row =1,column=0)


Image_viewer.mainloop()