"""
17. Class Decorators
Assignment:
Create a class decorator add_greeting that modifies a class to add a greet() 
method returning "Hello from Decorator!". Apply it to a class Person.
"""
# Class decorator definition
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Applying the class decorator
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Using the decorated class
p = Person("Arsalan")
print(p.greet())
