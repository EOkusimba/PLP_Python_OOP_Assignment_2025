#finalFxn.py

class Car:
    def __init__(self, make, model, year, color, range_km):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self._range_km = range_km  # Encapsulated attribute

    def get_range(self):
        return self._range_km

    def can_drive(self, distance):
        return distance <= self._range_km

    def drive(self):
        print(f"{self.make} {self.model} can complete the trip!")

    def stop(self):
        print(f"{self.make} {self.model} cannot complete the trip — consider refueling.")

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}, {self.color}) - Range: {self._range_km} km"


class ElectricCar(Car):
    def __init__(self, make, model, year, color, range_km):
        super().__init__(make, model, year, color, range_km)

    def stop(self):
        print(f"{self.make} {self.model} cannot complete the trip — please recharge.")
