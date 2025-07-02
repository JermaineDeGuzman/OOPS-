class Vehicle:
    def __init__(self, vehicle_id, model, capacity):
        self.vehicle_id = vehicle_id
        self.model = model
        self.capacity = capacity

    def calculate_cost(self, distance):
        raise NotImplementedError("Subclass must implement this method.")

class Car(Vehicle):
    def calculate_cost(self, distance):
        return distance * 10 + 50

class Van(Vehicle):
    def calculate_cost(self, distance):
        return distance * 8 + 30

class Motorcycle(Vehicle):
    def calculate_cost(self, distance):
        return distance * 5
