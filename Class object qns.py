# 1 . Create a class Student with attributes name, roll_number, and marks. Add a method to display student details.

# class Student:
#     def __init__(self,name,roll_no,marks):
#         self.name=name
#         self.roll_no=roll_no
#         self.marks=marks
#     
#     def display(self):
#         print("Name:",self.name,"\n""Roll No:",self.roll_no,"\n""Mark:",self.marks)

# s1=Student("Kareem","3","58")
# s1.display()



# 2 . Create a class Rectangle with attributes length and width. Add a method to calculate and display the area.

# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
    
#     def calc_area_of_rect(self):
#         calc_area_of_rect = self.length * self.width
#         print("Area of the rectangle is:", calc_area_of_rect)

# rectangle = Rectangle(40, 20)
# rectangle.calc_area_of_rect()



#3 . Create a class Car with attributes brand, model, and year.Add a method to display full details of the car.

# class Car:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year
    
#     def display(self):
#         print("Brand:",self.brand,"\n""Model:",self.model,"\n""Year:",self.year)

# c1=Car("Suzuki","Baleno","2024")
# c1.display()



#4 . Create a class Person with attributes name and age.Add a method to check if the person is eligible to vote (age ≥ 18).

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def check_vote(self):
#         if self.age >= 18:
#             print(self.name,"is eligible to vote.")
#         else:
#             print(self.name,"is not eligible to vote.")

# p1 = Person("Niyas", 17)
# p2 = Person("Swalah", 19)
# p1.check_vote()
# p2.check_vote()



#5 . Create a class BankAccount with attributes account_holder and balance.Add methods to deposit, withdraw, and check balance.      

# class BankAccount:
#     def __init__(self,account_holder,balance):
#         self.account_holder=account_holder
#         self.balance=balance
#         print("Account holder =",self.account_holder) 
    
#     def Deposit(self,amount):
#         if amount>0:
#             self.balance = self.balance + amount 
#             print(amount,"deposited." "\n"  "Balance =" ,self.balance)
#         else:
#             print("Cannot Deposit")     

#     def Withdraw(self,amount):
#         if amount<self.balance:
#             self.balance = self.balance - amount
#             print(amount, "withdrawn."  "\n"  "Balance =", self.balance) 
#         else:
#             print("Insufficient balance.")
        
#     def Check_balance(self):
#         print("Current balance =",self.balance) 

# bank1=BankAccount("Mohammed",0)      
# bank1.Deposit(7000)
# bank1.Withdraw(5000) 
# bank1.Check_balance()





#5 . Create a class BankAccount with attributes account_holder and balance.Add methods to deposit, withdraw, and check balance. (using while True and input the amount)

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        print("Account created for:", self.account_holder)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(amount, "deposited.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn.")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print("Current balance:", self.balance)

# Create account
name = input("Enter account holder name: ")
bank1 = BankAccount(name, 0)

# Menu loop
while True:
    print("\nOptions:\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amt = float(input("Enter amount to deposit: "))
        bank1.deposit(amt)
    elif choice == "2":
        amt = float(input("Enter amount to withdraw: "))
        bank1.withdraw(amt)
    elif choice == "3":
        bank1.check_balance()
    elif choice == "4":
        print("Thank you for using the banking system.")
        break
    else:
        print("Invalid choice. Please enter 1-4.")
        