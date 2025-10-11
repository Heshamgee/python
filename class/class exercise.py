# class_exercises.py
# Python Class Practice Exercises

print("=== PYTHON CLASS PRACTICE EXERCISES ===")
print("Follow the instructions below each exercise!")

"""
EXERCISE 1: Basic Class Creation
Create a Book class that has:
- Attributes: title, author, pages
- Methods: get_info() that returns a string with book information
"""
print("\n=== EXERCISE 1: Basic Book Class ===")
# TODO: Write your code here
class Book:
    def __init__(self, title, author, pages):
        # Your code here: initialize attributes
        pass
    
    def get_info(self):
        # Your code here: return book information
        pass

# Test your code (uncomment when ready)
# book1 = Book("Python 101", "John Doe", 300)
# print(book1.get_info())  # Should print: "Python 101 by John Doe, 300 pages"

"""
EXERCISE 2: Bank Account Class
Create a BankAccount class that has:
- Attributes: account_holder, balance (start at 0)
- Methods: 
    deposit(amount) - adds to balance
    withdraw(amount) - subtracts from balance (only if enough money)
    get_balance() - returns current balance
"""
print("\n=== EXERCISE 2: Bank Account Class ===")
class BankAccount:
    def __init__(self, account_holder):
        # Your code here
        pass
    
    def deposit(self, amount):
        # Your code here
        pass
    
    def withdraw(self, amount):
        # Your code here: only withdraw if enough balance
        pass
    
    def get_balance(self):
        # Your code here
        pass

# Test your code
# account = BankAccount("Alice")
# account.deposit(1000)
# account.withdraw(300)
# print(account.get_balance())  # Should show 700

"""
EXERCISE 3: Student Management System
Create a Student class that has:
- Attributes: name, grade, subjects (list)
- Methods:
    add_subject(subject) - adds a subject to the list
    remove_subject(subject) - removes a subject
    get_average() - returns grade (you can improve this later)
    display_info() - shows all student info
"""
print("\n=== EXERCISE 3: Student Class ===")
class Student:
    def __init__(self, name, grade):
        # Your code here
        pass
    
    def add_subject(self, subject):
        # Your code here
        pass
    
    def remove_subject(self, subject):
        # Your code here
        pass
    
    def display_info(self):
        # Your code here
        pass

# Test your code
# student1 = Student("Bob", 85)
# student1.add_subject("Math")
# student1.add_subject("Science")
# student1.display_info()

"""
EXERCISE 4: Car Rental System
Create a Car class that has:
- Attributes: make, model, year, is_rented (boolean)
- Methods:
    rent() - marks car as rented if available
    return_car() - marks car as available
    get_status() - returns rental status
"""
print("\n=== EXERCISE 4: Car Rental System ===")
class Car:
    def __init__(self, make, model, year):
        # Your code here
        pass
    
    def rent(self):
        # Your code here: only rent if not already rented
        pass
    
    def return_car(self):
        # Your code here
        pass
    
    def get_status(self):
        # Your code here
        pass

# Test your code
# car1 = Car("Toyota", "Camry", 2022)
# print(car1.get_status())  # Should be available
# car1.rent()
# print(car1.get_status())  # Should be rented

"""
EXERCISE 5: Shopping Cart System
Create a ShoppingCart class that has:
- Attributes: items (list), total_price
- Methods:
    add_item(name, price) - adds item to cart
    remove_item(name) - removes item from cart
    calculate_total() - calculates total price
    display_cart() - shows all items and total
"""
print("\n=== EXERCISE 5: Shopping Cart ===")
class ShoppingCart:
    def __init__(self):
        # Your code here
        pass
    
    def add_item(self, name, price):
        # Your code here
        pass
    
    def remove_item(self, name):
        # Your code here
        pass
    
    def calculate_total(self):
        # Your code here
        pass
    
    def display_cart(self):
        # Your code here
        pass

# Test your code
# cart = ShoppingCart()
# cart.add_item("Laptop", 1000)
# cart.add_item("Mouse", 25)
# cart.display_cart()

"""
EXERCISE 6: Library Management (Challenge!)
Create a Library class that manages multiple Book objects:
- Attributes: books (list of Book objects)
- Methods:
    add_book(book) - adds a book to library
    remove_book(title) - removes book by title
    find_book(title) - finds and returns a book
    list_books() - displays all books
"""
print("\n=== EXERCISE 6: Library Management (Challenge!) ===")
class Library:
    def __init__(self):
        # Your code here
        pass
    
    def add_book(self, book):
        # Your code here
        pass
    
    def remove_book(self, title):
        # Your code here
        pass
    
    def find_book(self, title):
        # Your code here
        pass
    
    def list_books(self):
        # Your code here
        pass

# Test your code (you'll need the Book class from Exercise 1)
# library = Library()
# book1 = Book("Python 101", "Author A", 300)
# book2 = Book("Java Basics", "Author B", 400)
# library.add_book(book1)
# library.add_book(book2)
# library.list_books()

"""
EXERCISE 7: Game Character (Advanced)
Create a GameCharacter class that has:
- Attributes: name, health, level, experience
- Methods:
    attack() - returns random damage
    take_damage(damage) - reduces health
    heal(amount) - increases health (max 100)
    level_up() - increases level when enough experience
    is_alive() - returns True if health > 0
"""
print("\n=== EXERCISE 7: Game Character (Advanced) ===")
import random

class GameCharacter:
    def __init__(self, name):
        # Your code here
        pass
    
    def attack(self):
        # Your code here: return random damage between 5-15
        pass
    
    def take_damage(self, damage):
        # Your code here
        pass
    
    def heal(self, amount):
        # Your code here: don't exceed 100 health
        pass
    
    def gain_experience(self, exp):
        # Your code here: level up if experience >= level * 100
        pass
    
    def level_up(self):
        # Your code here: increase level, reset experience
        pass
    
    def is_alive(self):
        # Your code here
        pass
    
    def display_stats(self):
        # Your code here
        pass

# Test your code
# hero = GameCharacter("Warrior")
# hero.gain_experience(150)
# print(hero.display_stats())

"""
BONUS EXERCISE: Real World Project - Restaurant System
Create a complete restaurant ordering system with:
- MenuItem class (name, price, category)
- Order class (table_number, items, total)
- Restaurant class (menu, orders)

This is a big project - try to design it yourself!
"""

print("\n" + "="*50)
print("INSTRUCTIONS:")
print("1. Complete one exercise at a time")
print("2. Test your code after each exercise")
print("3. If stuck, review the basic examples")
print("4. Don't forget to use 'self' in methods!")
print("5. Test edge cases (like withdrawing more than balance)")
print("="*50)