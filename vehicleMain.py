# vehicleMain.py

from vehicleFxn import Car, Plane, Boat, Bicycle

vehicles = [
    Car("Toyota", "Yaris"),
    Plane("Boeing", "747"),
    Boat("Yamaha", "WaveRunner"),
    Bicycle("Giant", "Escape 3")
]

print("\n------ Vehicle Movements ------")
for v in vehicles:
    v.move()
