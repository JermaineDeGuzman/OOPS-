import tkinter as tk
from random import randint

def show_riders_window(parent, vehicle_type=None, cost=None):
    root = tk.Toplevel(parent)
    root.title("Choose your Driver:")
    root.geometry("1000x600")
    root.config(background="#001657")

    # === Prepare rider and plate labels ===
    rider_labels = []
    plate_labels = []

    # === Receipt images ===
    R1 = tk.PhotoImage(file="Receipt.png")
    C1 = tk.PhotoImage(file="Choose.png")
    C2 = tk.PhotoImage(file="Findr.png")

    # Prevent images from being garbage collected
    root.R1 = R1
    root.C1 = C1
    root.C2 = C2

    # Place Receipts
    tk.Label(root, image=R1, bg="#001657").place(x=12, y=85)
    tk.Label(root, image=R1, bg="#001657").place(x=328, y=40)
    tk.Label(root, image=R1, bg="#001657").place(x=647, y=85)

    # Buttons to choose driver
    tk.Button(root, image=C1, command=root.destroy, borderwidth=0, bg="#ffffff", activebackground="#ffffff").place(x=123, y=423)
    tk.Button(root, image=C1, command=root.destroy, borderwidth=0, bg="#ffffff", activebackground="#ffffff").place(x=439, y=387)
    tk.Button(root, image=C1, command=root.destroy, borderwidth=0, bg="#ffffff", activebackground="#ffffff").place(x=758, y=423)

    # Button to randomize riders and plates
    tk.Button(root, image=C2, command=lambda: [ranrider(), ranlis()], borderwidth=0, bg="#001657", activebackground="#001657").place(x=401, y=517)

    # Create rider labels
    for x, y in [(124, 237), (444, 189), (762, 237)]:
        lbl = tk.Label(root, text="", font=("Lexend Zetta", 11), bg="#ffffff", fg="#001657")
        lbl.place(x=x, y=y)
        rider_labels.append(lbl)

    # Create plate labels
    for x, y in [(156, 283), (455, 240), (794, 283)]:
        lbl = tk.Label(root, text="", font=("Lexend Zetta", 11), bg="#ffffff", fg="#001657")
        lbl.place(x=x, y=y)
        plate_labels.append(lbl)

    # === Randomize Rider Names ===
    def ranrider():
        riders = list(set([
            "Maria Santos", "Jose Ruiz", "Ana Cruz", "Pedro Reyes",
            "Ava Fyang", "Ben Garcia", "Sofia Lim", "Miguel dela Cruz"
        ]))
        for i in range(3):
            rider_labels[i].config(text=riders[randint(0, len(riders) - 1)])

    # === Randomize Plate Numbers ===
    def ranlis():
        plates = list(set([
            "ABC-1234", "XYZ-5678", "PQR-9012", "LMN-3456",
            "EFG-7890", "UVW-1122", "JKL-3344", "RST-5566"
        ]))
        for i in range(3):
            plate_labels[i].config(text=plates[randint(0, len(plates) - 1)])

    # Static labels for layout (with optional vehicle and cost display)
    labels = [
        ("Name:", 237, 61),  ("Vehicle:", 260, 61), ("Plate No:", 283, 61), ("Total Cost:", 305, 61),
        ("Name:", 189, 380), ("Vehicle:", 215, 380), ("Plate No:", 241, 380), ("Total Cost:", 263, 380),
        ("Name:", 237, 696), ("Vehicle:", 260, 696), ("Plate No:", 283, 696), ("Total Cost:", 305, 696)
    ]

    for text, y, x in labels:
        if text == "Vehicle:" and vehicle_type:
            tk.Label(root, text=f"Vehicle:     {vehicle_type}", font=("Lexend Zetta", 11), bg="#ffffff", fg="#001657").place(x=x, y=y)
        elif text == "Total Cost:" and cost is not None:
            tk.Label(root, text=f"Total Cost:     ₱{cost:.2f}", font=("Lexend Zetta", 11), bg="#ffffff", fg="#001657").place(x=x, y=y)
        else:
            tk.Label(root, text=text, font=("Lexend Zetta", 11), bg="#ffffff", fg="#001657").place(x=x, y=y)

    # Show initial values
    ranrider()
    ranlis()
