import json  # For reading/writing booking data in JSON format
import os    # For checking if the bookings file exists
from booking import Booking  # Import the Booking class
from vehicle import Car, Van, Motorcycle  # Import vehicle types

class BookingManager:
    def __init__(self, filename='bookings.json'):
        # Initialize the BookingManager with a default file name
        self.filename = filename
        self.bookings = []  # Store all current bookings in a list
        self.load_bookings()  # Load existing bookings from file (if any)

    def add_booking(self, booking):
        # Add a new booking to the list and save to file
        self.bookings.append(booking)
        self.save_bookings()

    def cancel_booking(self, booking_id):
        # Remove a booking with the given booking_id and save the updated list
        self.bookings = [b for b in self.bookings if b.booking_id != booking_id]
        self.save_bookings()

    def save_bookings(self):
        # Save all bookings to a JSON file by converting them to dictionaries
        with open(self.filename, 'w') as file:
            json.dump([b.to_dict() for b in self.bookings], file, indent=4)

    def load_bookings(self):
        # Load bookings from the JSON file if it exists
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for d in data:
                    # Recreate the correct vehicle object based on type
                    vehicle_cls = {"Car": Car, "Van": Van, "Motorcycle": Motorcycle}[d["vehicle_type"]]
                    vehicle = vehicle_cls("V" + d["booking_id"], "Model", 4)
                    
                    # Rebuild the Booking object from the saved data
                    booking = Booking(d["user"], vehicle, d["start"], d["end"], d["distance"])
                    booking.booking_id = d["booking_id"]  # Restore original ID
                    self.bookings.append(booking)