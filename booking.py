import uuid

class Booking:
    def __init__(self, user, vehicle, start, end, distance):
        self.booking_id = str(uuid.uuid4())[:8]
        self.user = user
        self.vehicle = vehicle
        self.start = start
        self.end = end
        self.distance = distance
        self.cost = self.vehicle.calculate_cost(distance)

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
