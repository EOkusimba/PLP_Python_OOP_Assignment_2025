# vehicleFxn.py

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        raise NotImplementedError("Subclasses must implement the move() method")

    def __str__(self):
        return f"{self.make} {self.model}"


class Car(Vehicle):
    def move(self):
        print(f"{self} is driving.")


class Plane(Vehicle):
    def move(self):
        print(f"{self} is flying.")


class Boat(Vehicle):
    def move(self):
        print(f"{self} is sailing.")


class Bicycle(Vehicle):
    def move(self):
        print(f"{self} is pedaling.")
