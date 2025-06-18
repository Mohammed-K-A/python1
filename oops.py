#  What is OOP (Object-Oriented Programming)?

#  OOP is a way of writing code that is based on real-world objects. It helps organize code better, reuse it, and make it easier to maintain.
#  In simple words: OOP lets you bundle data (variables) and actions (functions) together into objects.


#  Main Concepts of OOP


#  1. Class

#  A class is like a blueprint or template for creating objects.


#  Example:

# class Car:
#     def start(self):
#         print("Car started")


#  2. Object

#  An object is a real-world thing created from a class.


#  Example:

# my_car = Car()
# my_car.start()  # Output: Car started


#  3. Encapsulation

#  Hiding internal details and only showing necessary parts.


#  Example:

# class BankAccount:
#     def __init__(self):
#          self.__balance = 0
#     def deposit(self, amount):
#         self.__balance += amount


#  4. Inheritance

#  A class can inherit features from another class.


#  Example:

# class Animal:
#     def sound(self):
#         print("Makes sound")
# class Dog(Animal):
#     def bark(self):
#         print("Barks")
# d = Dog()
# d.sound()
# d.bark()


#  5. Polymorphism

#  Same function name, but different behavior depending on the object.
#  oru fn name use cheyth diff object ukale pravarthipikkunnu


#  Example:

# class Bird:
#     def fly(self):
#         print("Bird can fly")
# class Penguin(Bird):
#     def fly(self):
#         print("Penguin can't fly")
# b1 = Bird()
# b2 = Penguin()
# b1.fly()
# b2.fly()



#  Why Use OOP?

# - Keeps code clean and organized
# - Reusability (you don't need to write the same code again)
# - Easier to debug and maintain
# - Models real-life things