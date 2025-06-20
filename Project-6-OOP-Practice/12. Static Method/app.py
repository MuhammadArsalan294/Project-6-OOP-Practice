"""
12. Static Methods
Assignment:
Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.
"""
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 10/5) + 33
    
print(TemperatureConverter.celsius_to_fahrenheit(0))   
print(TemperatureConverter.celsius_to_fahrenheit(100)) 

