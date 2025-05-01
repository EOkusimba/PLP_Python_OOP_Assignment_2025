# vehicleMain.py

from finalFxn import Car, ElectricCar

# Instantiate cars
car_1 = Car("Toyota", "Corolla", 2020, "Red", 1500)
car_2 = Car("Honda", "Civic", 2019, "Blue", 2000)
car_3 = ElectricCar("Tesla", "Model 3", 2022, "White", 500)
car_4 = ElectricCar("Nissan", "Leaf", 2021, "Green", 1200)
car_5 = Car("Ford", "Mustang", 2021, "Black", 500)

cars = [car_1, car_2, car_3, car_4, car_5]

# User input and decision logic
try:
    full = input("Is your fuel tank or battery fully filled/charged? (yes/no): ").strip().lower()

    if full not in ['yes', 'no']:
        print("Invalid response. Please enter 'yes' or 'no'.")
    else:
        distance = int(input("What distance do you plan to cover (in km)?: "))
        if distance < 0:
            print("Distance cannot be negative.")
        else:
            print("\n--- Trip Check Results ---")
            for c in cars:
                print(f"\nChecking: {c}")
                original_range = c.get_range()
                available_range = original_range if full == 'yes' else original_range // 2

                if distance <= available_range:
                    c.drive()
                else:
                    c.stop()
except ValueError:
    print("Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")
