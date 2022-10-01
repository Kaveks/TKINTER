
from tkinter import *
# Import older version of pillow PIL to use image files

from PIL import ImageTk,Image

Image_viewer = Tk()
Image_viewer.title("IMAGES IN TK")
Image_viewer.geometry("750x600")
#icon
Image_viewer.iconbitmap('ICON/icon.ico')
app_frame=LabelFrame(Image_viewer,borderwidth=10, relief=SUNKEN,width=640,height=460,padx=20,pady=20)

app_frame.place(anchor='center', relx=0.5, rely=0.5,bordermode=OUTSIDE)
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
img_label = Label(app_frame,image=img1)
img_label.grid(row=1,column=0 ,columnspan=3)

# status bar label
status =Label(app_frame,text ="Image 1 of"+str(len(image_list)),bg= "teal",bd=3,relief=SUNKEN,anchor=E)


#define buttons functionality

def forward(Image_Number):
    global img_label
    global b_forward
    global b_backward
    
    img_label.grid_forget()# forget previous image whe we click forward
    img_label=Label(app_frame,image=image_list[Image_Number-1])#Image_Number-1 since we gave forward(2)
    # 1st image =img1=index(0), next=img2 =index(1) which is Image_Number-1=1
    b_forward=Button(app_frame,text=">>" ,bg = "green",fg="black",command=lambda: forward(Image_Number+1))
    b_backward = Button(app_frame,text="<<",fg="black",bg="green",command =lambda: backward(Image_Number-1))  
    
    
    if Image_Number==6:
        b_forward=Button(app_frame,text=">>" ,bg = "green",fg="black",state=DISABLED)
    
    
    img_label.grid(row=1,column=0 ,columnspan=3)
    b_forward.grid(row =2,column=1)
    b_backward.grid(row =2,column=0)
    
    # Update status bar when clicking forward
    status =Label(app_frame,text ="Image " + str(Image_Number) + "of" +str(len(image_list)),bg= "teal",bd=3,relief=SUNKEN,anchor=E)
    status.grid(row=3, column=0,columnspan=3,sticky=W+E)
    return


def backward(Image_Number):
    global img_label
    global b_forward
    global b_backward
    
    img_label.grid_forget()# forget previous image when we click backward
    img_label=Label(app_frame,image=image_list[Image_Number-1])#Image_Number-1 since we gave forward(2)
    # 1st image =img1=index(0), next=img2 =index(1) which is Image_Number-1=1
    b_forward=Button(app_frame,text=">>" ,bg = "green",fg="black",command=lambda: forward(Image_Number+1))
    b_backward = Button(app_frame,text="<<",fg="black",bg="green",command =lambda: backward(Image_Number-1))  
    
    
    if Image_Number==1:
        b_backward=Button(app_frame,text=">>" ,bg = "green",fg="black",state=DISABLED)
    
    
    img_label.grid(row=1,column=0 ,columnspan=3)
    b_forward.grid(row =2,column=1)
    b_backward.grid(row =2,column=0)
    
    # update status bar
    status =Label(app_frame,text ="Image " + str(Image_Number) + "of" +str(len(image_list)),bg= "teal",bd=3,relief=SUNKEN,anchor=E)
    status.grid(row=3, column=0,columnspan=3,sticky=W+E)
    return

# buttons
b_forward=Button(app_frame,text=">>" ,bg = "green",fg="black",command=lambda: forward(2))
b_quit = Button(app_frame,text='Quit',bg="red",command=Image_viewer.quit)
b_backward = Button(app_frame,text="<<",fg="black",bg="green",command =lambda: backward(6))

#display
b_forward.grid(row =2,column=1)
b_quit.grid(row =2,column=2)
b_backward.grid(row =2,column=0)


# display status bar
status.grid(row=3, column=0,columnspan=3,sticky=W+E)
# display frame
app_frame.grid( row=0,column=0,columnspan=3,padx=10,pady=10,)


Image_viewer.mainloop()