"""
10. Instance Methods
Assignment:
Create a class Dog with instance variables name and breed. Add an instance method bark() that 
prints a message including the dog's name.
"""
class Dog:
    def __init__(self, name, breed):
        self.name = name      # Instance variable for dog's name
        self.breed = breed    # Instance variable for dog's breed

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

# Example usage:
dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()
