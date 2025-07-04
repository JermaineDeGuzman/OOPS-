import tkinter as tk # Imports the tkinter module for GUI development.
from tkinter import * # Imports all tkinter elements for direct use.
from tkinter import ttk # Imports the ttk module for themed widgets.
from main3 import RideBookingApp # Imports the main application class.

def open_booking_app(): # Defines a function to open the main booking application.
    new_window = tk.Toplevel(root) # Creates a new top-level window for the booking app.
    RideBookingApp(new_window) # Initializes the RideBookingApp within the new window.

root = tk.Tk() # Creates the main application window.
root.title("Welcome to OOPS!") # Sets the title of the main window.
root.geometry("1000x600") # Defines the main window's initial dimensions.
root.config(background="#001657") # Sets the background color of the main window.

book_btn=PhotoImage(file="Button.png") # Loads the image for the booking button.
oops_lg=PhotoImage(file="logo.png") # Loads the image for the application logo.
logo= Label(image=oops_lg, bg="#001657") # Creates a label widget to display the logo image with a matching background.
logo.pack() # Packs the logo label into the window.
logo.place(x=11, y=30) # Places the logo label at specific coordinates.

book_button = Button(root, image=book_btn, command=open_booking_app, borderwidth=0, bg="#001657", activebackground="#001657") # Creates a button widget that uses the loaded image, calls 'open_booking_app' when clicked, and has no border with specific background colors.
book_button.pack() # Packs the button into the window.
book_button.place(x=321, y=350) # Places the button at specific coordinates.

root.mainloop() # Starts the Tkinter event loop, keeping the window open and responsive to interactions.