import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, simpledialog
from vehicle import Car, Van, Motorcycle # Import vehicle classes
from booking import Booking # Import Booking class
from manager import BookingManager # Import Booking class
from PIL import Image, ImageTk  # For handling image icons
from distances import destinations # Dictionary for Locations and Distances
from Riders import show_riders_window # Function to show rider info window

class RideBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ride Booking System")
        self.root.geometry("1000x600")

        self.manager = BookingManager() # Initialize booking manager
        self.is_dark = False  # Track current theme
        self.manual_distance_unlocked = False  # Allow manual distance input
        self.image_obj = ImageTk.PhotoImage(Image.open('dark.png'))  # Dark mode icon
        self.my = ImageTk.PhotoImage(Image.open('light.png')) # Light mode icon
        self.bookings_visible = False # Track booking table visibility


        self.destinations = destinations # Predefined distances

        # Create a sorted list of unique city names from the destinations dictionary        
        self.city_list = sorted(set([city for pair in self.destinations.keys() for city in pair]))
        
        # Emoji icons for vehicles
        self.vehicle_icons = {
            "Car": "🚗",
            "Van": "🚐",
            "Motorcycle": "🏍"
        }

        self.create_styles() # Apply initial styles
        self.create_widgets() # Build UI components

    def create_styles(self):
        self.style = ttk.Style()
        self.set_theme() # Set the theme based on current mode

    def set_theme(self):
        self.style.theme_use("clam")  # Use clam theme for compatibility

        if self.is_dark:
            # Configure dark theme colors and images
            self.root.configure(bg="#001657")
            self.style.configure("TLabel", background="#001657", foreground="white")
            self.style.configure("TFrame", background="#001657")
            self.style.configure("TEntry", fieldbackground="#001657", foreground="white")
            self.style.configure("TCombobox", fieldbackground="#021347", foreground="white")
            self.style.map("TCombobox", fieldbackground=[("readonly", "#021347")], foreground=[("readonly", "white")])
            self.style.configure("TButton", background="#021347", foreground="white")
            self.style.map("TButton", background=[("active", "#555")], foreground=[("active", "white")])
            self.style.configure("Treeview", background="#021347", foreground="white", fieldbackground="#021347")
            self.style.configure("Treeview.Heading", background="#001657", foreground="white")
            self.my= ImageTk.PhotoImage(Image.open('light.png'))   
            self.logo=tk.Label(self.root, image=self.my, bg="#001657", borderwidth=0)
            self.logo.image=self.my
            self.logo.pack()
            self.logo.place(x=625, y=15)
        
        else:
            # Configure light theme colors and images
            self.root.configure(bg="#f4f4f4")
            self.style.configure("TLabel", background="#f4f4f4", foreground="black")
            self.style.configure("TFrame", background="#f4f4f4")
            self.style.configure("TEntry", fieldbackground="white", foreground="black")
            self.style.configure("TCombobox", fieldbackground="white", foreground="black")
            self.style.map("TCombobox", fieldbackground=[("readonly", "white")], foreground=[("readonly", "black")])
            self.style.configure("TButton", background="white", foreground="black")
            self.style.map("TButton", background=[("active", "#e6e6e6")], foreground=[("active", "black")])
            self.style.configure("Treeview", background="white", foreground="black", fieldbackground="white")
            self.style.configure("Treeview.Heading", background="#e0e0e0", foreground="black")
            self.image_obj= ImageTk.PhotoImage(Image.open('dark.png'))  
            self.logo=tk.Label(self.root, image=self.image_obj,bg="#f4f4f4", borderwidth=0)
            self.logo.image=self.image_obj
            self.logo.pack()
            self.logo.place(x=625, y=15)

    def toggle_theme(self):
        self.is_dark = not self.is_dark  # Toggle the theme state
        self.set_theme()
        new_text = "Toggle Light Mode" if self.is_dark else "Toggle Dark Mode"
        self.theme_button.config(text=new_text)

    def create_widgets(self):
        # Create input form and buttons
        top_frame = ttk.Frame(self.root)
        top_frame.pack(padx=20, pady=10, fill="x")
        self.image_obj= ImageTk.PhotoImage(Image.open('dark.png'))  
        self.logo=tk.Label(self.root, image=self.image_obj,bg="#f4f4f4", borderwidth=0)
        self.logo.image=self.image_obj
        self.logo.pack()
        self.logo.place(x=625, y=15)

        # User input fields
        ttk.Label(top_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(top_frame, width=20)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Vehicle Selections
        ttk.Label(top_frame, text="Vehicle:").grid(row=0, column=2, padx=5, pady=5)
        self.vehicle_var = tk.StringVar(value="Car")
        self.vehicle_box = ttk.Combobox(top_frame, textvariable=self.vehicle_var, values=[f"{self.vehicle_icons[v]} {v}" for v in ["Car", "Van", "Motorcycle"]], state="readonly")
        self.vehicle_box.grid(row=0, column=3, padx=5, pady=5)
        self.vehicle_box.bind("<<ComboboxSelected>>", lambda e: self.update_estimated_cost())

        # Start and End Locations
        ttk.Label(top_frame, text="Start:").grid(row=1, column=0, padx=5, pady=5)
        self.start_var = tk.StringVar()
        self.start_combo = ttk.Combobox(top_frame, textvariable=self.start_var, values=self.city_list)
        self.start_combo.grid(row=1, column=1, padx=5, pady=5)
        self.start_combo.bind("<<ComboboxSelected>>", self.update_distance)

        ttk.Label(top_frame, text="End:").grid(row=1, column=2, padx=5, pady=5)
        self.end_var = tk.StringVar()
        self.end_combo = ttk.Combobox(top_frame, textvariable=self.end_var, values=self.city_list)
        self.end_combo.grid(row=1, column=3, padx=5, pady=5)
        self.end_combo.bind("<<ComboboxSelected>>", self.update_distance)

        # Distance Input
        ttk.Label(top_frame, text="Distance (mi):").grid(row=2, column=0, padx=5, pady=5)
        self.distance_var = tk.StringVar()
        self.distance_entry = ttk.Entry(top_frame, width=20, textvariable=self.distance_var, state="readonly")
        self.distance_entry.grid(row=2, column=1, padx=5, pady=5)

        # Manual Input Toggle
        self.unlock_button = ttk.Button(top_frame, text="Input Manually", command=self.unlock_distance)
        self.unlock_button.grid(row=2, column=2, padx=5, pady=5)
        
        # Cost Label
        ttk.Label(top_frame, text="Estimated Cost:").grid(row=2, column=3, padx=5, pady=5)
        self.estimated_cost_var = tk.StringVar(value="₱0.00")
        self.estimated_cost_label = ttk.Label(top_frame, textvariable=self.estimated_cost_var)
        self.estimated_cost_label.grid(row=2, column=4, padx=5, pady=5)

        # Buttons: Book, Filter, Cancel, Theme
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Book Ride", command=self.book_ride).grid(row=0, column=0, padx=10)
        self.toggle_button_text = tk.StringVar(value="Show All Bookings")
        ttk.Button(button_frame, textvariable=self.toggle_button_text, command=self.show_bookings).grid(row=0, column=1, padx=10)
        ttk.Button(button_frame, text="Cancel Ride", command=self.cancel_booking).grid(row=0, column=2, padx=10)
        self.theme_button = ttk.Button(button_frame, text="Toggle Dark Mode", command=self.toggle_theme)
        self.theme_button.grid(row=0, column=3, padx=10)

        # Filter section
        filter_frame = ttk.LabelFrame(self.root, text="Filters")
        filter_frame.pack(fill="x", padx=20, pady=5)
        ttk.Label(filter_frame, text="Filter by User:").grid(row=0, column=0, padx=5)
        self.filter_user_var = tk.StringVar()
        self.filter_user_entry = ttk.Entry(filter_frame, textvariable=self.filter_user_var, width=20)
        self.filter_user_entry.grid(row=0, column=1, padx=5)

        ttk.Label(filter_frame, text="Filter by Vehicle:").grid(row=0, column=2, padx=5)
        self.filter_vehicle_var = tk.StringVar()
        self.filter_vehicle_box = ttk.Combobox(filter_frame, textvariable=self.filter_vehicle_var, values=["Car", "Van", "Motorcycle"], state="readonly", width=18)
        self.filter_vehicle_box.grid(row=0, column=3, padx=5)
        ttk.Button(filter_frame, text="Apply Filters", command=self.apply_filters).grid(row=0, column=4, padx=5)
        ttk.Button(filter_frame, text="Remove Filters", command=self.clear_filters).grid(row=0, column=5, padx=5)

        # Summary label for bookings
        self.summary_label = ttk.Label(self.root, text="Total Bookings: 0 | Total Earnings: ₱0.00")
        self.summary_label.pack(pady=5)

        # Table for booking list
        self.tree = ttk.Treeview(self.root, columns=("ID", "User", "Vehicle", "Start", "End", "Distance", "Cost"), show='headings')
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=20, pady=10)

    def unlock_distance(self):
        # Allow user to manually input distance
        self.manual_distance_unlocked = True
        self.distance_entry.config(state="normal")
        self.distance_var.trace_add("write", lambda *args: self.update_estimated_cost())

    def update_distance(self, event=None):
        # Auto-update distance based on selected cities
        start = self.start_var.get()
        end = self.end_var.get()

        if not start or not end or start == end:
            self.distance_var.set("")
            self.distance_entry.config(state="readonly")
            self.estimated_cost_var.set("₱0.00")
            return

        # Look up distance in dictionary
        distance = self.destinations.get((start, end)) or self.destinations.get((end, start))

        if distance is not None:
            self.distance_var.set(str(distance))
            self.distance_entry.config(state="readonly")
            self.manual_distance_unlocked = False
        else:
            self.distance_var.set("")
            if self.manual_distance_unlocked:
                self.distance_entry.config(state="normal")
            else:
                self.distance_entry.config(state="readonly")
        self.update_estimated_cost()

    def update_estimated_cost(self):
        # Estimate fare cost based on distance and vehicle type
        try:
            distance = float(self.distance_var.get())
        except:
            self.estimated_cost_var.set("₱0.00")
            return

        v_type = self.vehicle_var.get().split(" ", 1)[-1]
        rates = {"Car": 20, "Van": 30, "Motorcycle": 10}
        rate = rates.get(v_type, 0)
        cost = distance * rate
        self.estimated_cost_var.set(f"₱{cost:.2f}")

    def book_ride(self):
        # Collect input and validate
        user = self.name_entry.get()
        v_icon_label = self.vehicle_var.get()
        v_type = v_icon_label.split(" ", 1)[-1] 
        start = self.start_var.get()
        end = self.end_var.get()
        distance_str = self.distance_entry.get()

        if not all([user, start, end, distance_str]):
            messagebox.showwarning("Missing Info", "Please fill in all fields.")
            return

        try:
            distance = float(distance_str)
        except:
            messagebox.showerror("Invalid Distance", "Please enter a valid distance.")
            return

        # Allow adding new distance entry manually
        if not distance and self.manual_distance_unlocked:
            try:
                distance = float(self.distance_var.get())
                self.destinations[(start, end)] = distance
            except ValueError:
                messagebox.showerror("Error", "Invalid distance.")
                return

        # Create vehicle and booking instance
        vehicle_cls = {"Car": Car, "Van": Van, "Motorcycle": Motorcycle}[v_type]
        vehicle = vehicle_cls("ID", "Model", 4)
        booking = Booking(user, vehicle, start, end, distance)
        self.manager.add_booking(booking)
        
        # Success message
        messagebox.showinfo("Success", f"Booking ID: {booking.booking_id}")
        self.clear_inputs()
        self.estimated_cost_var.set("₱0.00")
        show_riders_window(self.root, vehicle_type=v_type, cost=booking.cost)

        if self.bookings_visible:
          self.refresh_bookings_table()

    def show_bookings(self):
        # Toggle bookings table visibility
        if self.bookings_visible:
            self.tree.pack_forget()
            self.toggle_button_text.set("Show All Bookings")
            self.summary_label.config(text="Total Bookings: 0 | Total Earnings: ₱0.00")
            self.bookings_visible = False
        else:
            self.tree.pack(fill="both", expand=True, padx=20, pady=10)
            self.refresh_bookings_table()
            self.toggle_button_text.set("Hide Bookings")
            self.bookings_visible = True

    def refresh_bookings_table(self):
        # Refresh table with filtered data
        self.tree.delete(*self.tree.get_children())
        filter_user = self.filter_user_var.get().strip()
        filter_vehicle = self.filter_vehicle_var.get().strip()
        total = 0
        cost_total = 0

        for b in reversed(self.manager.bookings):
            if (filter_user and filter_user.lower() not in b.user.lower()):
                continue
            if (filter_vehicle and filter_vehicle != b.vehicle.__class__.__name__):
                continue
            self.tree.insert("", "end", values=(b.booking_id, b.user, b.vehicle.__class__.__name__, b.start, b.end, b.distance, f"₱{b.cost:.2f}"))
            total += 1
            cost_total += b.cost

        self.summary_label.config(text=f"Total Bookings: {total} | Total Earnings: ₱{cost_total:.2f}")

    def apply_filters(self):
        if self.bookings_visible:
            self.refresh_bookings_table()

    def clear_filters(self):
        self.filter_user_var.set("")
        self.filter_vehicle_var.set("")

    def cancel_booking(self):
        # Cancel selected booking from table
        selected = self.tree.selection()
        if selected:
            booking_id = self.tree.item(selected[0])['values'][0]
            self.manager.cancel_booking(booking_id)
            messagebox.showinfo("Cancelled", f"Booking {booking_id} cancelled.")
        else:
            messagebox.showwarning("No selection", "Please select a booking to cancel.")

    def clear_inputs(self):
        # Reset input fields
        self.name_entry.delete(0, tk.END)
        self.start_var.set("")
        self.end_var.set("")
        self.distance_entry.delete(0, tk.END)
        self.vehicle_var.set(f"{self.vehicle_icons['Car']} Car")

# Start the main GUI loop
if __name__ == "_main_":
    root = tk.Tk()
    app = RideBookingApp(root)
    root.mainloop()