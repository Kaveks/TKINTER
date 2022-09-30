# create a simple calculator to implement the  label,entry and grid concepts
from tkinter import *


calc_window = Tk()
calc_window.geometry("600x700")# customized window size
calc_window.title("Simple Calculator")#window tittle

# change tkinter icon
calc_window.iconbitmap("C:/Users/DELL/Documents/PROGRAMMING/GitHub/TKINTER/ICON/calc.ico")
entry_origin =Entry(calc_window, width=60,borderwidth=10)
entry_origin.grid(row=0,column=0,padx=50,pady=30,columnspan=3)

#define entry buttons command execution
def click_button(n):# n is any number entered
    First_entry =entry_origin.get()# get whichever entry
    entry_origin.delete(0,END)# delete entry previously existed since the entire process is a loop
    entry_origin.insert(0,str(First_entry)+str(n))# insert two entries converted to strings for effective concatenation

    return


# define operations button command functionality
def button_clear():
    entry_origin.delete(0,END)
    
    return



def button_add():
    n1= entry_origin.get()
    # make n1  and operation global so as it can be used anywhere
    global n1_global
    global operation
    
    operation ="addition" 
    n1_global = int(n1) 
    entry_origin.delete(0,END)
    
    return


def button_minus():
    n1= entry_origin.get()
    # make n1  and operation global so as it can be used anywhere
    global n1_global
    global operation
    
    operation ="subtraction" 
    n1_global = int(n1) 
    entry_origin.delete(0,END)
    
    return




def button_multiply():
    n1= entry_origin.get()
    # make n1  and operation global so as it can be used anywhere
    global n1_global
    global operation
    
    operation ="multiplication" 
    n1_global = int(n1) 
    entry_origin.delete(0,END)

    return


def button_divide():
    n1= entry_origin.get()
    # make n1  and operation global so as it can be used anywhere
    global n1_global
    global operation
    
    operation ="division" 
    n1_global = int(n1) 
    entry_origin.delete(0,END)

    return


def button_square_root():
    n1= entry_origin.get()
    # make n1  and operation global so as it can be used anywhere
    global n1_global
    global operation
    
    operation ="square root" 
    n1_global = int(n1) 
    entry_origin.delete(0,END)

    return

    


def button_mod():
    n1= entry_origin.get()
    # make n1  and operation global so as it can be used anywhere
    global n1_global
    global operation
    
    operation ="modulus" 
    n1_global = int(n1) 
    entry_origin.delete(0,END)
    return

def button_exp():
    n1= entry_origin.get()
    # make n1  and operation global so as it can be used anywhere
    global n1_global
    global operation
    
    operation ="exponential" 
    n1_global = int(n1) 
    entry_origin.delete(0,END)
    return




def button_equal():
    n2= entry_origin.get()
    entry_origin.delete(0,END)
    
    from math import sqrt
    if operation == "addition":
        entry_origin.insert(0,n1_global+ int(n2))  # type: ignore
    
    
    elif operation == "subtraction":
        entry_origin.insert(0,n1_global - int(n2))  # type: ignore
 
    
    elif operation == "multiplication":
        entry_origin.insert(0,n1_global * int(n2))  # type: ignore
        
  
    
    
    elif operation == "division":
        entry_origin.insert(0,n1_global / int(n2))  # type: ignore
    
    elif operation == "modulus":
        entry_origin.insert(0,n1_global % int(n2))  # type: ignore
    
    
    elif operation == "exponential":
        entry_origin.insert(0,n1_global ** int(n2))  # type: ignore
    
    

    elif operation == "square root":
        from math import sqrt
        entry_origin.insert(0,sqrt(n1_global)) # type: ignore

    else:
        pass

 

# def buttons
b1=Button(calc_window, text ="1", padx=40, pady=20,command=lambda: click_button(1))
b2=Button(calc_window, text ="2", padx=40, pady=20,command=lambda: click_button(2))
b3=Button(calc_window, text ="3", padx=40, pady=20,command=lambda: click_button(3))
b4=Button(calc_window, text ="4", padx=40, pady=20,command=lambda: click_button(4))
b5=Button(calc_window, text ="5", padx=40, pady=20,command=lambda: click_button(5))
b6=Button(calc_window, text ="6", padx=40, pady=20,command=lambda: click_button(6))
b7=Button(calc_window, text ="7", padx=40, pady=20,command=lambda: click_button(7))
b8=Button(calc_window, text ="8", padx=40, pady=20,command=lambda: click_button(8))
b9=Button(calc_window, text ="9", padx=40, pady=20,command=lambda: click_button(9))
b0=Button(calc_window, text ="0", padx=40, pady=20,command=lambda: click_button(0))


b_add=Button(calc_window, text ="+", padx=40, pady=20,command=button_add)
b_minus=Button(calc_window, text ="-", padx=40, pady=20,command=button_minus)
b_divide=Button(calc_window, text ="/", padx=42, pady=20,command=button_divide)
b_multiply=Button(calc_window, text ="x", padx=42, pady=20,command=button_multiply)
b_equal=Button(calc_window, text ="=", padx=45, pady=20,command=button_equal)
b_clear=Button(calc_window, text ="Del", padx=40, pady=20,command= button_clear)
b_modulus=Button(calc_window, text ="mod", padx=40, pady=20,command=button_mod)
b_exponential = Button(calc_window, text ="exp", padx=45,pady=20,command=button_exp)
b_sqrt=Button(calc_window, text ="sqrt",padx=40,pady=20,command=button_square_root)



# display buttons
b1.grid(row =4, column=0)
b2.grid(row =4, column=1)
b3.grid(row =4, column=2)


b4.grid(row =3, column=0)
b5.grid(row =3, column=1)
b6.grid(row =3, column=2)



b7.grid(row =2, column=0)
b8.grid(row =2, column=1)
b9.grid(row =2, column=2)


b0.grid(row =5, column=0)
b_add.grid(row =5, column=1)
b_minus.grid(row =5, column=2)


b_divide.grid(row =6, column=0)
b_multiply.grid(row =6, column=1)
b_clear.grid(row =6, column=2)


b_equal.grid(row =7, column=2,)


b_modulus.grid(row =1, column=0)
b_exponential.grid(row =1, column=1)
b_sqrt.grid(row=1 ,column=2)




calc_window.mainloop()