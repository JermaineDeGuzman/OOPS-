import tkinter as tk
from vehicle import Car, Van, Motorcycle
from tkinter import *
from drivers import Booking
from random import randint

def ranrider():
    riders=["Maria Santos ", " Jose Ruiz", "Ana Cruz ", "Pedro Reyes",  "Ava Fyang", "Ben Garcia ", "Sofia Lim" 
, "Miguel dela Cruz"]

    riders_set=set(riders)
    unique_riders=list(riders_set)
    rando= randint(0,7)

    my_rider1= Label(root, text=unique_riders[rando], font=("Lexend Zetta", 11), bg="#ffffff", fg="#001657")
    my_rider1.pack()
    my_rider1.place(x=124, y=237)

    unique_riders=list(riders_set)
    rando= randint(0,7)
    my_rider2= Label(root, text=unique_riders[rando], font=("Lexend Zetta", 11), bg="#ffffff", fg="#001657")
    my_rider2.pack()
    my_rider2.place(x=444, y=189)
    
    unique_riders=list(riders_set)
    rando= randint(0,7)
    my_rider3= Label(root, text=unique_riders[rando], font=("Lexend Zetta", 11), bg="#ffffff", fg="#001657")
   
    my_rider3.pack()
    my_rider3.place(x=762, y=237)


def ranlis():
    plates=["ABC-1234", "XYZ-5678", "PQR-9012", "LMN-3456", "EFG-7890", "UVW-1122", "JKL-3344", " RST-5566"]

    plates_set=set(plates)
    unique_plates=list(plates_set)
    rando= randint(0,7)

    my_plate1= Label(root, text=unique_plates[rando], font=("Lexend Zetta", 11), bg="#ffffff", fg="#001657")
    my_plate1.pack()
    my_plate1.place(x=156, y=283)

    unique_plates=list(plates_set)
    rando= randint(0,7)
    my_plate2= Label(root, text=unique_plates[rando], font=("Lexend Zetta", 11), bg="#ffffff", fg="#001657")
    my_plate2.pack()
    my_plate2.place(x=455, y=240)
    
    unique_plates=list(plates_set)
    rando= randint(0,7)
    my_plate3= Label(root, text=unique_plates[rando], font=("Lexend Zetta", 11), bg="#ffffff", fg="#001657")
   
    my_plate3.pack()
    my_plate3.place(x=794, y=283)




root= Tk()
root.title("Choose your Driver:")
root.geometry("1000x600")
root.config(background="#001657")

R1=PhotoImage(file="Receipt.png")
Receipt1= Label(image=R1, bg="#001657")
Receipt2= Label(image=R1, bg="#001657")
Receipt3= Label(image=R1, bg="#001657")

Receipt1.pack()
Receipt2.pack()
Receipt3.pack()
Receipt1.place(x=12, y=85)
Receipt2.place(x=328, y=40)
Receipt3.place(x=647, y=85)

C1=PhotoImage(file="Choose.png")
C2=PhotoImage(file="Findr.png")
Choose1= Button(root, image=C1, command= root.quit, borderwidth=0, bg="#ffffff", activebackground="#ffffff")
Choose2= Button(root, image=C1, command= root.quit, borderwidth=0, bg="#ffffff", activebackground="#ffffff")
Choose3= Button(root, image=C1, command= root.quit, borderwidth=0, bg="#ffffff", activebackground="#ffffff")
Find1= Button(root, image=C2, command= lambda:[ranrider(), ranlis()], borderwidth=0, bg="#001657", activebackground="#001657")
Choose1.pack()
Choose2.pack()
Choose3.pack()
Find1.pack()


Choose1.place(x=123, y=423)
Choose2.place(x=439, y=387)
Choose3.place(x=758, y=423)
Find1.place(x=401, y=517)


labels = [
    ("Name:", 237, 61),  
    ("Vehicle:", 260, 61),
    ("Plate No:", 283, 61),
    ("Total Cost:", 305, 61),
    ("Name:", 189, 380),  
    ("Vehicle:", 215, 380),
    ("Plate No:", 241, 380),
    ("Total Cost:", 263, 380),
    ("Name:", 237, 696),   
    ("Vehicle:", 260, 696),
    ("Plate No:", 283, 696),
    ("Total Cost:", 305, 696),
]

# Loop through the list of label texts, positions, and x coordinates
for text, y, x in labels:  
    label = tk.Label(root, text=text, font=("Lexend Zetta", 11), bg="#ffffff", fg="#001657")  # Create label
    label.place(x=x, y=y)


root.mainloop()