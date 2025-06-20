"""
18. Property Decorators: @property, @setter, and @deleter
Assignment:
Create a class Product with a private attribute _price. Use @property to get the price, 
@price.setter to update it, and @price.deleter to delete it.
"""
class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        print("Setting price...")
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Example usage
p = Product(100)

# Accessing the price
print(p.price)

# Updating the price
p.price = 150
print(p.price)

# Deleting the price
del p.price
