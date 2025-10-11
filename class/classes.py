#classes and objects 
# STEP 1: Define the blueprint (Class)
class Dog:
    # STEP 2: Constructor - runs when creating new dogs
    def __init__(self, name, age, breed):
        # STEP 3: Give each dog its own characteristics
        self.name = name
        self.age = age 
        self.breed = breed
        self.is_hungry = True  # All dogs start hungry
    
    # STEP 4: Define what dogs can do (Methods)
    def bark(self):
        return "Woof! Woof!"
    
    def eat(self):
        self.is_hungry = False
        return f"{self.name} is eating and now full!"
    
    def describe(self):
        return f"I'm {self.name}, a {self.age}-year-old {self.breed}"
    
    def is_dog_hungry(self):
        if self.is_hungry:
            return f"{self.name} is hungry!"
        else:
            return f"{self.name} is full!"

# STEP 5: Create actual dog objects
my_dog = Dog("Buddy", 3, "Golden Retriever")
friends_dog = Dog("Luna", 2, "Husky")

# STEP 6: Use the dogs
print("=== MY DOG ===")
print(my_dog.describe())      # I'm Buddy, a 3-year-old Golden Retriever
print(my_dog.bark())          # Woof! Woof!
print(my_dog.is_dog_hungry()) # Buddy is hungry!

print(my_dog.eat())           # Buddy is eating and now full!
print(my_dog.is_dog_hungry()) # Buddy is full!

print("\n=== FRIEND'S DOG ===")
print(friends_dog.describe()) # I'm Luna, a 2-year-old Husky
print(friends_dog.bark())     # Woof! Woof!

#################
class Dog():
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def bark():
        return "woof!"
    def eat(self):
        return f"{self.name}is eating!"
    def get_info(self):
        return f"{self.name}is{self.age}years old"


dog1 = Dog("buddy" , 3)
dog2 = Dog("max",5)
print(dog1.name)
print(dog1.age)
print(dog1.bark())