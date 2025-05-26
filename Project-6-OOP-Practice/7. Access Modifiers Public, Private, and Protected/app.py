"""
7. Access Modifiers: Public, Private, and Protected
Assignment:
Create a class Employee with:
a public variable name,
a protected variable _salary, and
a private variable __ssn.
Try accessing all three variables from an object of the class and document what happens.
"""
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def private(self):
        return self.__ssn
    
emp = Employee("Ali", 30000, "1234")

print(emp.name)
print(emp._salary)
print(emp.private())
# OR
print(emp._Employee__ssn)