"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, pay = None, commission = 0):
        self.name = name
        self.commission = commission

    def get_pay(self):
        if self.commission:
            self.pay += self.commission
            self.commission = 0
        return self.pay

    def __str__(self):
        pass

class Wage(Employee):
    def __init__(self,name,hours,rate):
        super().__init__(name, commission=0)
        self.hours = hours
        self.rate = rate
        self.pay = hours*rate

    def __str__(self):
        line1 = (f"{self.name} is on contract for {self.hours} hours at a wage of £{self.rate} per hour.")
        lineX = ""
        if self.commission:
            lineX = (f"Additionally, they have earned a commision of £{self.commission}.")
        line2 = (f"In total, their pay is {self.get_pay()}")

        line = line1 + lineX + line2
        print(line)
        return line

class Salaried(Employee):
    def __init__(self, name, salary):
        super().__init__(name, commission=0)
        self.salary = salary
        self.pay = salary
    
    def __str__(self):
        line1 = (f"{self.name} is on contract at a salary of £{self.salary} per month.")
        if self.commission:
            line2 = (f"Additionally, they have earned a commision of £{self.commission}. In total, their pay is {self.get_pay()}")
        else:
            line2 = (f"This is equal to their total pay.")
        
        line = line1 + line2
        print(line)
        return line

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salaried('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Wage('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Salaried('Renee', 3000)
renee.commission = 4*200

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Wage('Jan', 150, 25)
jan.commission = 3*220

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Salaried('Robbie',2000)
robbie.commission = 1500

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Wage('Ariel', 120, 30)
ariel.commission = 600

billie.__str__()
charlie.__str__()
renee.__str__()
jan.__str__()
robbie.__str__()
ariel.__str__()
