"""
21. Make a Custom Class Iterable
Assignment:
Create a class Countdown that takes a start number. Implement __iter__() and __next__() 
to make the object iterable in a for-loop, counting down to 0.
"""

class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self  # Returns the iterator object itself

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            num = self.current
            self.current -= 1
            return num

# Example usage:
for number in Countdown(5):
    print(number)
