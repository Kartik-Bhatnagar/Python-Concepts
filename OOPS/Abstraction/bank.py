"""
Exercise Instructions
Instructions
Create a class called Bank and pass ABC to it.

Inside the class you have to define two methods:

2.1: Define a function called basicinfo() and add a print statement inside it saying
"This is a generic bank" and returning the string "Generic bank: 0".

2.2: Define a second function called withdraw and keep it empty by adding a pass keyword under it.
Make this function abstract by adding '@abstractmethod' right above it.


Create another class called Swiss and pass the class Bank inside it. This means you are inheriting from class Bank.

3.1: Create a constructor for this class that initializes a class variable bal to 1000

Override both functions from the Bank class: basicinfo() and withdraw().

4.1: Define a function called basicinfo() and add a print statement inside it stating “This is the Swiss Bank”
and returning a string with "Swiss Bank: " followed by the current bank balance.
For example, if self.bal = 80, then it would return "Swiss Bank: 80"

4.2 Define a second function, called withdraw and pass one parameter to it (other than self): amount.
Amount represents the amount that will be withdrawn.

4.2.1: Update the class variable bal by deducting the value of amount from it.
4.2.2: Print the value of amount giving output such as: “Withdrawn amount: 30"
4.2.3: Print the new balance giving an output such as: “New balance: 970”
4.2.4: Return the new balance
Note: Make sure to verify that there is enough money to withdraw!
If amount is greater than balance, then do not deduct any money from the class variable bal. Instead, print a statement saying "Insufficient funds", and return the original account balance instead.
"""
from abc import ABC,abstractmethod


class Bank(ABC):
	#this is the parent class
	#abstract class
    def basicinfo():
        print("This is a generic bank")
        return "Generic Bank: 0"
    
    @abstractmethod
    def withdraw():
        pass

class Swiss(Bank):
    def __init__(self):
        self.bal = 1000
    
    def basicinfo(self):
        print("This is the Swiss Bank")
        return f"Swiss Bank: {self.bal}"
        
    def withdraw(self,amount):
        if amount < self.bal:
            self.bal = self.bal -amount
            print(f"Withdrwan amount: {amount}")
            print(f"New Balance : {self.bal}")
            
        else:
            print(f"Insufficient Balance.\nAmount requested {amount} Balance available {self.bal}")
        
        return self.bal
                
    
s1 = Swiss()
print(s1.basicinfo())
s1.withdraw(500)
s1.withdraw(800)
print(s1.basicinfo() )
