# Import the uuid module to generate unique booking IDs
import uuid

# Class to represent a booking for a vehicle
class Booking:
    def __init__(self, user, vehicle, start, end, distance):
        # Generate a unique booking ID (first 8 characters of a UUID)
        self.booking_id = str(uuid.uuid4())[:8]
        
        # Store booking details
        self.user = user
        self.vehicle = vehicle
        self.start = start
        self.end = end
        self.distance = distance
        
        # Calculate cost using the vehicle's cost formula
        self.cost = self.vehicle.calculate_cost(distance)

    # Convert booking information to a dictionary (useful for displaying or saving)
    def to_dict(self):
        return {
            "booking_id": self.booking_id,
            "user": self.user,
            "vehicle_type": self.vehicle.__class__.__name__,
            "start": self.start,
            "end": self.end,
            "distance": self.distance,
            "cost": self.cost
        }