from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import messagebox
import base64
import os
from turtle import Screen

def decrypt():
    password=code.get()
    
    if password=="1671":
        screen2=Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("300x200")
        screen2.configure(bg="#6bd1ed")

        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

       
        text2=Text(screen2,font="Rpbote 10",bg="#c6ebf5",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=20,y=60,width=200,height=100)

        text2.insert(END,decrypt)

    elif password=="":
        messagebox.showerror("encryption","Enter password")
        
    elif password !="1671":
        messagebox.showerror("encryption","Wrong password")
        


def encrypt():
    password=code.get()

    if password=="1671":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("300x200")
        screen1.configure(bg="#3d3d3c")

        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        
        text2=Text(screen1,font="Rpbote 10",bg="#4f4f4d",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=20,y=60,width=200,height=100)

        text2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("encryption","Enter password")
        
    elif password !="1671":
        messagebox.showerror("encryption","Wrong password")
        

    
        

def main_screen():

    global screen
    global code
    global text1

    
    
    screen=Tk()
    screen.geometry("400x450")  
    screen.title("SecretApp")
    
    image_icon = PhotoImage(file="ic.png")
    screen.iconphoto(False,image_icon)

    def reset():
        code.set("")
        text1.delete(1.0,END)

        
    
    Label(text="Enter your Secret Message",fg="black",font=("calbri",13)).place(x=20,y=20)
    text1=Text(font="Robote 15",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=20,y=60,width=350,height=150)

    Label(text="Enter secret key for encryption and decryption",fg="black",font=("calibri",12)).place(x=20,y=220)
    
    code=StringVar()
    Entry(textvariable=code,width=23,bd=0,font=("arial",20),show="*").place(x=20,y=250)

    Button(text="ENCRYPT",height='2',width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=20,y=290)
    Button(text="DECRYPT",height='2',width=23,bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200,y=290)
    Button(text="RESET",height='2',width=30,bg="#1089ff",fg="white",bd=0,command=reset).place(x=100,y=340)    
    
    screen.mainloop()

main_screen()  
