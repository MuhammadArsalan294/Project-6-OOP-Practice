"""
14. Aggregation
Assignment:
Create a class Department and a class Employee. Use aggregation by having a Department object store
a reference to an Employee object that exists independently of it.
"""
class Employee:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return f"Employee Name: {self.name}"

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: reference to an independent Employee

    def show_details(self):
        return f"Department: {self.dept_name}, {self.employee.get_details()}"

emp = Employee("Muhammad Arsalan")       
dept = Department("Accounts", emp)      
print(dept.show_details())              
