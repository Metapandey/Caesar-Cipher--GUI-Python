import tkinter as tk
import tkinter.font as tkfont
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

root = tk.Tk()
pic = PhotoImage(file = "C:\\Users\\zerod\\Documents\\Python Projects\\cesarcipher\\new.png")
root.iconphoto(False,pic)
root.title("Text Encryptor-Decryptor")
# To set the dimensions of the window
root.geometry("450x450") # width x height
# To set whether we can resize the window or not.The below line doesn't allow the resizing of the window.
root.resizable(width=FALSE, height=FALSE)
canvas = tk.Canvas(root,height = 450, width=450, bg="#0066ff")
filename = PhotoImage(file = "C:\\Users\\zerod\\Documents\\Python Projects\\cesarcipher\\newonee.png")
background_label = Label(root, image=filename)
background_label.place(x=-1, y=0, relwidth=1, relheight=1)
# Attaching the canvas
canvas.pack()
bold_font = tkfont.Font(family="Helvetica",size=8,weight="bold")
# Creating a label with a text and attaching it to the root
label1 = tk.Label(root,text= "Enter the Text",width=13,bg="#0066ff")
# adding the font features to the label
label1.config(font=bold_font)
# placing the label in the canvas
canvas.create_window(225,80,window=label1)
# Text Area 
user_text = tk.Entry(root)
canvas.create_window(225,105,window=user_text,width = 200,height = 25)
label2=tk.Label(root,text="Choose an Operation",width=18,bg="#0066ff")
# adding the font features to the label
label2.config(font=bold_font)
# placing the label in the canvas
canvas.create_window(225,150,window=label2)
v = tk.IntVar()
def choice():
  # Retrieve the value of the radio button
    x = v.get()
  # Performs Encryption if the value is 1 else performs Decryption.
    # if(x==1):
    #     encryption()
    # elif(x==2):
    #     decryption()


# this the last line of my code

root.mainloop()