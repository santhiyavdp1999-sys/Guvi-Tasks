
# 1. Bank Account   

class Bankaccount:

    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -=amount
            print(f"Withdraw ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

class Savingsaccount(Bankaccount):
    def __init__(self, account_number, balance=0, interest_rate=0.05):
        super().__init__(account_number, balance)
        self.interest_rate= interest_rate
    
    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        print(f"Interest earned: ₹{interest}")
        return interest

class Currentaccount(Bankaccount):
    def __init__(self, account_number, balance=0, min_balance=1000):
        super().__init__(account_number,balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
       if amount > 0 and (self.get_balance() - amount) >= self.min_balance:
        super().withdraw(amount)
       else :
        print(f"Cannot withdraw ₹{amount}. Minimum balance of ₹{self.min_balance} must be maintained.")

if __name__ == "__main__":
    savings = Savingsaccount("SA123", 5000, 0.04)
    savings.deposit(2000)
    savings.calculate_interest()
    savings.withdraw(1000)
    print()

    current = Currentaccount("CA456", 8000,2000)
    current.withdraw(5000)
    current.withdraw(2000)
    print()





# 2. Employee Management

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
    def calculate_salary(self):
        """Base method to be overridden by subclass"""
        return self.base_salary
    
    def __str__(self):
        return f"{self.__class__.__name__} - {self.name}: ₹{self.calculate_salary():,.2f}"


class Regularemployee(Employee):
    def __init__(self, name,base_salary,bonus):
        super().__init__(name, base_salary)
        self.bonus =bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class Contractemployee(Employee):

    def __init__(self, name, hourly_rate, hourly_worked):
        super(). __init__(name, base_salary=0)
        self.hourly_rate=hourly_rate
        self.hourly_worked=hourly_worked
    
    def calculate_salary(self):
        return self.hourly_rate * self. hourly_worked

class Manager(Employee):
    def __init__(self, name, base_salary, allowence, performance_bonus):
        super(). __init__(name, base_salary)
        self.allowence = allowence
        self. performance_bonus = performance_bonus

    def calculate_salary(self):
        return self.base_salary + self.allowence + self.performance_bonus
    
if __name__=="__main__":
    Employee = [
        Regularemployee("Abi", 30000, 5000),
        Contractemployee("Priya", 500, 160),
        Manager("Karthika", 50000, 10000, 15000)
    ]

    for emp in Employee:
        print(emp)




# 3. Vehicle Rental


class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        return self.rental_rate * days

    def __str__(self):
        return f"{self.__class__.__name__} - {self.model}"

class Car(Vehicle):
    def __init__(self,model, rental_rate, luxury=False):
        super().__init__(model,rental_rate)
        self.luxury = luxury

    def calculate_rental(self, days):
        cost = super().calculate_rental(days)
        if self.luxury:
            cost +=500 * days
        return cost

class Bike(Vehicle):
    def __init__(self, model, rental_rate, helmet_included=True):
        super().__init__(model, rental_rate)
        self.helmet_included = helmet_included

    def calculate_rental(self, days):
        cost = super().calculate_rental(days)
        if days > 5:
            cost *=0.9
        return cost

class Truck(Vehicle):
    def __init__(self,model,rental_rate,load_capacity):
        super().__init__(model, rental_rate)
        self.load_capacity = load_capacity 
    
    def calculate_rental(self, days):
        cost = super(). calculate_rental(days)
        cost += self.load_capacity * 200 * days
        return cost

Vehicle = [
    Car("Toyota Camry", 1500, luxury=True),
    Bike("Yamaha FZ", 500, helmet_included=True),
    Truck("Tata LPT", 2500, load_capacity=5)
]

rental_days = 7

for v in Vehicle:
    print (f"{v}: ₹{v.calculate_rental(rental_days):,.2f} for {rental_days} days")





