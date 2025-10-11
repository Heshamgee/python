# exercise_solutions.py
# Solutions for the class exercises (Don't peek until you try!)

print("=== EXERCISE SOLUTIONS ===")
print("Only look after you've tried the exercises!")

"""
EXERCISE 1 SOLUTION
"""
print("\n--- Exercise 1 Solution ---")
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def get_info(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

# Test
book1 = Book("Python 101", "John Doe", 300)
print(book1.get_info())

"""
EXERCISE 2 SOLUTION
"""
print("\n--- Exercise 2 Solution ---")
class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds!"
    
    def get_balance(self):
        return f"Balance: ${self.balance}"

# Test
account = BankAccount("Alice")
print(account.deposit(1000))
print(account.withdraw(300))
print(account.get_balance())

"""
EXERCISE 3 SOLUTION
"""
print("\n--- Exercise 3 Solution ---")
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.subjects = []
    
    def add_subject(self, subject):
        self.subjects.append(subject)
        return f"Added {subject}"
    
    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)
            return f"Removed {subject}"
        return "Subject not found"
    
    def display_info(self):
        subjects_str = ", ".join(self.subjects) if self.subjects else "No subjects"
        return f"Student: {self.name}, Grade: {self.grade}, Subjects: {subjects_str}"

# Test
student1 = Student("Bob", 85)
student1.add_subject("Math")
student1.add_subject("Science")
print(student1.display_info())

# Continue with other solutions...
