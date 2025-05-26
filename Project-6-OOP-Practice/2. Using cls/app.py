"""
2. Using cls
Assignment:
Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method 
with cls to manage and display the count.
"""
class Counter:
    count = 0  # Class variable to keep track of the number of instances

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        print(f"Total objects created: {cls.count}")


# Example usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.get_count()  # Output: Total objects created: 3

class Counter:
    class_variable = "Class Variable"

    def __init__(self):
        pass
    
    @classmethod
    def class_method(cls):
        print(f"{cls.class_variable}")


count1 = Counter()

Counter.class_method()