# PLP_Python_OOP_Assignment_2025

Assignment 1: Design Your Class! 🏗
    
    Create a class representing anything you like (a Smartphone, a Book, or a Superhero!).
    
    Add attributes and methods to bring the class to life!
    
    Use constructors to initialise each object with unique values.
    
    Add an inheritance layer to explore polymorphism or encapsulation.

#Activity 2: Polymorphism Challenge! 🎭

    Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).


1. Car Refuel Advisory Program
Files

        vehicleFxn.py — Contains class definitions for Car and ElectricCar.
        
        finalMain.py — Main file that handles user input and simulates trip logic.

Description
  This script:
     
    Models a list of cars (including electric ones).
    
    Prompts the user for:
    
    Whether the fuel tank or battery is full.
    
    How far they plan to drive.
    
    Uses the car's range to determine whether it can complete the trip or needs to refuel/recharge.


Key OOP Concepts

    Encapsulation: Vehicle range is accessed via get_range().
    
    Inheritance: ElectricCar class inherits from Car.
    
    Methods: drive(), stop(), and can_drive() handle logic and feedback.


How to Run

        Ensure both files are in the same folder and run:
        python finalMain.py


2. Vehicle Movement (Polymorphism Demo)
      Files
      
        vehicleFxn.py — Contains a base Vehicle class and four subclasses: Car, Plane, Boat, and Bicycle.
        
        vehicleMain.py — Lets the user choose a vehicle and displays how it moves.

    Description
    This interactive script:
    
        Lists four vehicles.
        
        
        Asks the user to choose one.
        
        
        Outputs that vehicle’s unique movement using the move() method.


Key OOP Concepts

    Inheritance: All vehicle types inherit from a base Vehicle class.
    
    Polymorphism: Each subclass defines its own version of move().


How to Run

    Ensure both files are in the same folder and run:
    python vehicleMain.py

Requirements

    Python 3.7 or higher
    No external libraries needed
