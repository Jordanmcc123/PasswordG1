from tkinter import *
from random import randint 

root = Tk()
root.title("Jordan's Strong Password Generator")
#icon for top of window from faveicon generator.
root.iconbitmap("/Users/jordanmccalla/Documents/coding_projects/password_G/favicon_io/favicon.ico")
root.geometry("500x300")

#genrating random intger to pull and convert into ascii character 
my_password = chr(randint(33,126))

def new_rand():
    #Clear the entry box 
    pw_entry.delete(0, END)

    #Get the length 
    pw_length = int(my_entry.get())

    #Variable to hold password 
    my_password = ""

    #Loop through length 
    for x in range(pw_length):
        my_password += chr(randint(33,126))
    
    #Output password to box 
    pw_entry.insert(0, my_password)

#Copy to clipboard
def copier():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
    


#label frame 
lf = LabelFrame(root, text= "Number Of Characters?")
lf.pack(pady=10)

#Create input box for number of characters 
my_entry = Entry(lf, font=("Helvetica", 20))
my_entry.pack(pady=15, padx=20)

#Creat entry box for our returned password 

pw_entry = Entry(root, text="", font=("Helvetica", 24))
pw_entry.pack(pady=20)

#Frame for buttons 

my_frame = Frame(root)
my_frame.pack(pady=20)

#Buttons

my_button = Button(my_frame, text="Create Strong Passowrd", command=new_rand)
my_button.grid(row=0, column=0, padx=20)

copy_button = Button(my_frame, text="Copy To Clipboard", command= copier)
copy_button.grid(row=0, column=1, padx=20)






root.mainloop()