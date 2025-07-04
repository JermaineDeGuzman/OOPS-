# Parent class for all types of vehicles
class Vehicle:
    def __init__(self, vehicle_id, model, capacity):
        # Initialize the vehicle with ID, model name, and passenger capacity
        self.vehicle_id = vehicle_id
        self.model = model
        self.capacity = capacity

    # Abstract method to calculate the cost of a ride
    def calculate_cost(self, distance):
        raise NotImplementedError("Subclass must implement this method.")

# Child CLass representing a Car
class Car(Vehicle):
    def calculate_cost(self, distance):
        return distance * 10 + 50

# Child Class representing a Van
class Van(Vehicle):
    def calculate_cost(self, distance):
        return distance * 8 + 30

# Child Class representing a Motorcycle
class Motorcycle(Vehicle):
    def calculate_cost(self, distance):
        return distance * 5