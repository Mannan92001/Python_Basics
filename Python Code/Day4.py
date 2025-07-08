# 1. Abstraction
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Create objects
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Area of Circle: {circle.area()}")
print(f"Area of Rectangle: {rectangle.area()}")

# 2. Inheritance
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class inheriting from Animal class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    # Overriding the speak method
    def speak(self):
        print(f"{self.name} barks.")

# Create an object of Dog
dog = Dog("Buddy", "Golden Retriever")
dog.speak()  # Calls the overridden speak method

# 3. Encapsulation
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private variable
    
    # Getter method for balance
    def get_balance(self):
        return self.__balance
    
    # Setter method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")
    
    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance.")

# Create an object of BankAccount
account = BankAccount("Alice", 1000)
print(account.get_balance())  # Access balance through the getter method
account.deposit(500)
account.withdraw(300)

# 4. Polymorphism
class Cat:
    def speak(self):
        print("Meow!")

class Duck:
    def speak(self):
        print("Quack!")

# Function to demonstrate polymorphism
def make_animal_speak(animal):
    animal.speak()

# Create objects
cat = Cat()
duck = Duck()

# Polymorphism: same method name, different behavior
make_animal_speak(cat)  # Output: Meow!
make_animal_speak(duck)  # Output: Quack!