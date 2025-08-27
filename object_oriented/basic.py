# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#
#     def start_engine(self):
#         print(f"{self.make} {self.model}'s engine started.")
#
# my_car = Car("Ford", "Mustang")
# my_car.start_engine()
#
# class BankAccount:
#     def __init__(self, balance=0):
#         self.__balance = balance
#
#     def deposit(self, amount=0):
#         if amount>0:
#             self.__balance += amount
#
#     def withdraw(self, amount=0):
#         if amount>self.__balance and amount > 0:
#             self.__balance -= amount
#
#     def get_balance(self):
#         return self.__balance
#
# account = BankAccount(500)
# account.deposit(100)
# account.deposit(50)
# print(account.get_balance())
#
#
# #polymorphism
# class Bird:
#     def fly(self):
#         print("Bird flying...")
#
# class Penguin:
#     def fly(self):
#         print("Penguin can not flying...")
#
# def animal_fly(animal):
#     animal.fly()
#
# bird = Bird()
# penguin = Penguin()
#
# animal_fly(bird)

# open close principle
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class Paypal(PaymentMethod):
    def pay(self, amount):
        print(f"Payment method paypal is {amount}")


class Stripe(PaymentMethod):
    def pay(self, amount):
        print(f"Payment method stripe is {amount}")


class PaymentProcessor:
    def process_payment(self, payment_method: PaymentMethod, amount):
        payment_method.pay(amount)


processor = PaymentProcessor()
processor.process_payment(Paypal(), 100)
