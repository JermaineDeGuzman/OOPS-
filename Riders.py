import tkinter as tk
from random import randint
import os

def show_riders_window(parent, vehicle_type=None, cost=None, user_name="Guest", booking_id="N/A"):
    # Create a new window for choosing a driver
    root = tk.Toplevel(parent)
    root.title("Choose your Driver:")
    root.geometry("1000x600")
    root.config(background="#001657")  # Set background color

    # Lists to hold rider and plate labels
    rider_labels = []
    plate_labels = []
    # Data structure to hold rider information
    rider_data = [{"name": "", "plate": ""} for _ in range(3)]

    # Load images for the UI
    R1 = tk.PhotoImage(file="Receipt.png")
    C1 = tk.PhotoImage(file="Choose.png")
    C2 = tk.PhotoImage(file="Findr.png")
    root.R1, root.C1, root.C2 = R1, C1, C2

    # Define positions for UI elements
    positions = [
        {"receipt": (12, 85), "choose": (123, 423), "rider": (124, 237), "plate": (156, 283), "labels": [(237, 61), (260, 61), (283, 61), (305, 61)]},
        {"receipt": (328, 40), "choose": (439, 387), "rider": (444, 189), "plate": (455, 240), "labels": [(189, 380), (215, 380), (241, 380), (263, 380)]},
        {"receipt": (647, 85), "choose": (758, 423), "rider": (762, 237), "plate": (794, 283), "labels": [(237, 696), (260, 696), (283, 696), (305, 696)]}
    ]

    # Function to show the ticket window
    def show_ticket(index):
        root.destroy()  # Close the current window
        win = tk.Toplevel(parent)  # Create a new window for the ticket
        win.title("Your Ticket")
        win.geometry("360x600")
        win.resizable(False, False)  # Prevent resizing
        win.config(bg="#001657")  # Set background color

        # Center the ticket window on the screen
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry(f"{width}x{height}+{x}+{y}")

        # Load and display the ticket image
        ticket_img = tk.PhotoImage(file="Receipt.png")
        win.ticket_img = ticket_img
        tk.Label(win, image=ticket_img, bg="#001657").place(x=0, y=0, relwidth=1, relheight=1)

        # Thank you message
        tk.Label(win, text="Thank you for riding with us!", font=("Arial", 11, "bold"),
                  fg="#001657").place(relx=0.5, y=220, anchor="center")

        # Display ride details
        info = [
            ("Rider's Name:", rider_data[index]['name']),
            ("Vehicle:", vehicle_type),
            ("Plate No:", rider_data[index]['plate']),
            ("Total Cost:", f"₱{cost:.2f}")
        ]
        y_start = 240
        for label, value in info:
            tk.Label(win, text=label, font=("Arial", 10), bg="white", fg="#001657").place(x=50, y=y_start)
            tk.Label(win, text=value, font=("Arial", 10, "bold"), bg="white", fg="#001657").place(x=150, y=y_start)
            y_start += 30  # Increment y position for the next label

        # Buttons for rebooking and exiting
        def rebook():
            win.destroy()  # Close the ticket window
            os.system("python main3.py")  # Restart the main program

        tk.Button(win, text="Rebook", font=("Arial", 10), bg="#001657", fg="white", width=20,
                  command=rebook).place(relx=0.5, y=380, anchor="center")
        tk.Button(win, text="Exit", font=("Arial", 10), bg="#001657", fg="white", width=20,
                  command=win.quit).place(relx=0.5, y=420, anchor="center")

    # Function to randomly assign rider names
    def ranrider():
        names = list(set([
            "Maria Santos", "Jose Ruiz", "Ana Cruz", "Pedro Reyes",
            "Ava Fyang", "Ben Garcia", "Sofia Lim", "Miguel dela Cruz"
        ]))
        for i in range(3):
            name = names[randint(0, len(names) - 1)]  # Select a random name
            rider_data[i]["name"] = name
            rider_labels[i].config(text=name)  # Update the label with the name

    # Function to randomly assign vehicle plates
    def ranlis():
        plates = list(set([
            "ABC-1234", "XYZ-5678", "PQR-9012", "LMN-3456",
            "EFG-7890", "UVW-1122", "JKL-3344", "RST-5566"
        ]))
        for i in range(3):
            plate = plates[randint(0, len(plates) - 1)]  # Select a random plate
            rider_data[i]["plate"] = plate
            plate_labels[i].config(text=plate)  # Update the label with the plate

    # Create UI elements for each rider
    for i, pos in enumerate(positions):
        tk.Label(root, image=R1, bg="#001657").place(x=pos["receipt"][0], y=pos["receipt"][1])
        tk.Button(root, image=C1, command=lambda idx=i: show_ticket(idx), borderwidth=0,
                  bg="#ffffff", activebackground="#ffffff").place(x=pos["choose"][0], y=pos["choose"][1])

        rider_lbl = tk.Label(root, text="", font=("Lexend Zetta", 11), bg="#ffffff", fg="#001657")
        rider_lbl.place(x=pos["rider"][0], y=pos["rider"][1])
        rider_labels.append(rider_lbl)

        plate_lbl = tk.Label(root, text="", font=("Lexend Zetta", 11), bg="#ffffff", fg="#001657")
        plate_lbl.place(x=pos["plate"][0], y=pos["plate"][1])
        plate_labels.append(plate_lbl)

        # Create labels for ride details
        for j, (y, x) in enumerate(pos["labels"]):
            label_texts = ["Name:", "Vehicle:", "Plate No:", "Total Cost:"]
            if j == 1 and vehicle_type:
                text = f"Vehicle:     {vehicle_type}"  # Display vehicle type if provided
            elif j == 3 and cost is not None:
                text = f"Total Cost:     ₱{cost:.2f}"  # Display total cost if provided
            else:
                text = label_texts[j]
            tk.Label(root, text=text, font=("Lexend Zetta", 11), bg="#ffffff", fg="#001657").place(x=x, y=y)

    # Button to generate random riders and plates
    tk.Button(root, image=C2, command=lambda: [ranrider(), ranlis()], borderwidth=0,
              bg="#001657", activebackground="#001657").place(x=401, y=517)

    # Generate initial random riders and plates
    ranrider()
    ranlis()
