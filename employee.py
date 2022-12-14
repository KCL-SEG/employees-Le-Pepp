"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, pay = None, commission = 0):
        self.name = name
        self.commission = commission
        self.commissionCalculated = False

    def get_pay(self):
        if self.commission and not self.commissionCalculated:
            self.pay += self.commission
            self.commissionCalculated = True
        return self.pay

    def __str__(self):
        pass

    def addCommission(self, contracts, perContract):
        self.contracts = contracts
        self.perContract = perContract
        self.commission = contracts*perContract

class Wage(Employee):
    def __init__(self,name,hours,rate):
        super().__init__(name, commission=0)
        self.hours = hours
        self.rate = rate
        self.pay = hours*rate

    def __str__(self):
        line = f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour"
        if self.commission != 0:
            if self.contracts == 1:
                line += f" and receives a bonus commission of {self.commission}"
            else:
                line += f" and receives a commission for {self.contracts} contract(s) at {self.perContract}/contract"
        
        self.totalPay = self.get_pay()
        line += f". Their total pay is {self.totalPay}."
        print(line)
        return line

class Salaried(Employee):
    def __init__(self, name, salary):
        super().__init__(name, commission=0)
        self.salary = salary
        self.pay = salary
    
    def __str__(self):
        line = f"{self.name} works on a monthly salary of {self.salary}"
        if self.commission != 0:
            if self.contracts == 1:
                line += f" and receives a bonus commission of {self.commission}"
            else:
                line += f" and receives a commission for {self.contracts} contract(s) at {self.perContract}/contract"
        
        
        self.totalPay = self.get_pay()
        line += f". Their total pay is {self.totalPay}."
        print(line)
        return line

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salaried('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Wage('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Salaried('Renee', 3000)
renee.addCommission(4,200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Wage('Jan', 150, 25)
jan.addCommission(3,220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Salaried('Robbie',2000)
robbie.addCommission(1,1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Wage('Ariel', 120, 30)
ariel.addCommission(1,600)



"""str(billie)
str(charlie)
str(renee)
str(jan)
str(robbie)
str(ariel)"""