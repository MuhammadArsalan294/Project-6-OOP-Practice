"""
4. Class Variables and Class Methods
Assignment:
Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. 
Show that it affects all instances.
"""
class Bank:
    bank_name = "HBL"

    def __init__(self):
        pass

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print(f"Bank name changed to: {cls.bank_name}")

bank1 = Bank()

print("Before:", bank1.bank_name)

Bank.change_bank_name("UBL")

print("After:", bank1.bank_name)
