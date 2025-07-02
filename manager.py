import json
import os
from booking import Booking
from vehicle import Car, Van, Bike

class BookingManager:
    def __init__(self, filename='bookings.json'):
        self.filename = filename
        self.bookings = []
        self.load_bookings()

    def add_booking(self, booking):
        self.bookings.append(booking)
        self.save_bookings()

    def cancel_booking(self, booking_id):
        self.bookings = [b for b in self.bookings if b.booking_id != booking_id]
        self.save_bookings()

    def save_bookings(self):
        with open(self.filename, 'w') as file:
            json.dump([b.to_dict() for b in self.bookings], file, indent=4)

    def load_bookings(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for d in data:
                    vehicle_cls = {"Car": Car, "Van": Van, "Bike": Bike}[d["vehicle_type"]]
                    vehicle = vehicle_cls("V" + d["booking_id"], "Model", 4)
                    booking = Booking(d["user"], vehicle, d["start"], d["end"], d["distance"])
                    booking.booking_id = d["booking_id"]
                    self.bookings.append(booking)
