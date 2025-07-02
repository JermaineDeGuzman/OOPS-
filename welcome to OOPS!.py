import tkinter as tk
from tkinter import *
from tkinter import ttk
from main2 import RideBookingApp 

def open_booking_app():
    new_window = tk.Toplevel(root)
    RideBookingApp(new_window)  
root = tk.Tk()
root.title("Welcome to OOPS!")
root.geometry("1000x600")
root.config(background="#001657")

book_btn=PhotoImage(file="Button.png")
oops_lg=PhotoImage(file="logo.png")
logo= Label(image=oops_lg, bg="#001657")
logo.pack()
logo.place(x=11, y=30)

book_button = Button(root, image=book_btn, command=open_booking_app, borderwidth=0, bg="#001657", activebackground="#001657")
book_button.pack()
book_button.place(x=321, y=350)

root.mainloop()