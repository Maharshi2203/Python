# OOP helps you organize code into reusable blueprints called classes.

# Used in:

# Web frameworks like Django and Flask
# Backend systems
# Game development
# Automation tools

# 1. Real-World Analogy

# Think of a Car.

# Properties (Data)
# brand
# model
# speed
# Behaviors (Functions)
# start()
# accelerate()
# stop()

# In OOP:

# Class = Blueprint
# Object = Actual instance created from the blueprint


# 2. Creating a Class
class Car:
    pass

# This creates an empty blueprint.

# 3. Creating an Object
car1 = Car()
print(car1)

# 4. __init__() Constructor
# Automatically runs when an object is created.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# 5. What is self?
# self refers to the current object.
car1 = Car("Toyota", "Fortuner")

# Python internally does:
Car.__init__(car1, "Toyota", "Fortuner")

# 6. Accessing Attributes
print(car1.brand)
print(car1.model)

# 7. Adding Methods
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} started")

car = Car("BMW")
car.start()

# 🧠 Why OOP Matters

# Without OOP:

# Data and functions are scattered.

# With OOP:

# Data + behavior are grouped together.

# This makes code:

# Cleaner
# Reusable
# Easier to maintain

# Public vs Private Attributes (Convention)
class User:
    def __init__(self, password):
        self._password = password
# A single underscore means “internal use”.

# 🧬 9. Inheritance
# Create a new class based on another class.
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("Woof")

dog = Dog()
dog.speak()
dog.bark()


# 10. Polymorphism
# Different classes can implement the same method.

class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")