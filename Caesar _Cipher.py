import tkinter as tk
import tkinter.font as tkfont
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

root = tk.Tk()

pic = PhotoImage(file = "C:\\Users\\zerod\\Documents\\Python Projects\\cesarcipher\\new.png")
root.iconphoto(False,pic)
root.title("Text Encryptor-Decryptor")
#dimensions of the window
root.geometry("450x450") # width x height
#resizing of the window.
root.resizable(width=FALSE, height=FALSE)
canvas = tk.Canvas(root,height = 450, width=450, bg="#0066ff")
filename = PhotoImage(file = "C:\\Users\\zerod\\Documents\\Python Projects\\cesarcipher\\newonee.png")
background_label = Label(root, image=filename)
background_label.place(x=-1, y=0, relwidth=1, relheight=1)
canvas.pack()
# font features for boxes 
bold_font = tkfont.Font(family="Helvetica",size=9,weight="bold")


# Box1 starting box
Box1 = tk.Label(root,text= "Enter Text Below",width=15,bg="#0066ff")
# Adding  font features to the boxes
Box1.config(font=bold_font)
# Placing the label in the canvas
canvas.create_window(222,25,window=Box1)

# Text Area for user text
user_text = tk.Entry(root)
canvas.create_window(225,55,window=user_text,width = 250,height = 25)

# Box2 2nd 
Box2=tk.Label(root,text="Choose an Operation",width=20,bg="#0066ff")
Box2.config(font=bold_font)
canvas.create_window(225,215,window=Box2)

# Box3 3rd 
Box3 = tk.Label(root,text= "Key Between 1-25",width=15,bg="#0066ff")
Box3.config(font=bold_font)
canvas.create_window(222,85,window=Box3)

# Text Area for the value of key

key_text = tk.Entry(root)
canvas.create_window(225,120,window=key_text,width = 25,height = 30)


# Integer varaiable
v = tk.IntVar()
# Code Logic Starts from here 
def choice():
  # Retrieve the value of the radio button
    x = v.get()
    if(x==1):
        cipher_message()
    elif(x==2):
        decipher_message()


# Main encryption Logic
def cipher_message():
    message = user_text.get()
    char = " "
    encrypted_message = ""
    shift = int(key_text.get())
    for i in range(len(message)):
        char = message[i]
        if char == " ":
            encrypted_message += " "
        elif not char.isalpha():
            print("Only write Alphabets  in the message no numbers or special charaters are allowed")
            break
        elif (char.isupper() ):
            encrypted_message += chr((ord(char) + shift-65) % 26 + 65)
        else:
            encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)

# encrypted Text EAns     
    EAns = tk.Text(root, height = 1, width= 40)
    EAns.insert(tk.END,str(encrypted_message))
    EAns.config(font=bold_font,state=DISABLED)
    canvas.create_window(220,400,window=EAns)

# Main decryption Logic
def decipher_message():
    message = user_text.get()
    char = " "
    decypher_message = ""
    shift = int(key_text.get())
    for i in range(len(message)):
        char = message[i]
        if char == " ":
            decypher_message += " "
        elif not char.isalpha() :
            print("Only write Alphabets  in the message no numbers or special charaters are allowed")
            break
        elif (char.isupper() ):
            decypher_message += chr((ord(char) - shift-65) % 26 + 65)
        else:
            decypher_message += chr((ord(char) - shift - 97) % 26 + 97)
# Decrypted Text DAns
    # DAns=tk.Entry(root,text=decrypted_message,width=20,bg="light yellow")
    DAns = tk.Text(root, height = 1, width= 40)
    DAns.insert(tk.END,str(decypher_message))
    DAns.config(font=bold_font,state=DISABLED)
    canvas.create_window(220,400,window=DAns)

#Button1 for Encryption 
Button1=tk.Radiobutton(root, text="Encryption",padx = 20, variable=v, value=1,command=choice,bg="light yellow")
Button1.config(font=bold_font)
canvas.create_window(75,250,window=Button1)

#Button2 for Decryption
Button2=tk.Radiobutton(root, text="Decryption",padx = 20, variable=v, value=2,command=choice,bg="light yellow")
Button2.config(font=bold_font)
canvas.create_window(375,250,window=Button2)

# Box4 4th 
Box4 =tk.Label(root,text="Converted Text ",width=20,bg="yellow")
Box4.config(font=bold_font)
canvas.create_window(220,350,window=Box4)

# Box5 5th information Block
Box5 =tk.Label(root,text="Only write Alphabets, no numbers or special charaters are allowed ",width=20,bg="yellow")
Box5.config(font=bold_font)
canvas.create_window(220,430,window=Box5,width = 460,)

# End of canvas 
root.mainloop()