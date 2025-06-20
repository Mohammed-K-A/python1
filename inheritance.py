# Single inheritance

# inherits the behaviour of parent class to child class

# class Animal:
#     def speak(self):
#         print("Animal Speaking")
# # child class Dog inherits the base class Animal
# class Dog(Animal):
#     def bark(self):
#         print("Dog barking")

# d=Dog()
# d.bark()
# d.speak()


# ..............................................................................................
# Multi-level Inheritance

# mukalilthe class ne inherit cheyyunna reethi

# class Animal:
#     def speak(self):
#         print("Animal Speaking")
# # child class Dog inherits the base class Animal
# class Dog(Animal):
#     def bark(self):
#         print("Dog barking")
# # child class Dogchild inherits another child class Dog
# class Dogchild(Dog):
#     def eat(self):
#         print("Eating bread....")

# d=Dogchild()
# d.bark()
# d.speak()
# d.eat()


# .......................................................................................
# Multiple Inheritance

# ithil 1st class last class aayittum 2nd class last class aayittum aan connection. 1st classum 2nd classum connection illa 

# class Calculation1:
#     def Summation(self,a,b):
#         return a+b
# class Calculation2:
#     def Multiplication(self,a,b):
#         return a*b
# class Derived(Calculation1,Calculation2):
#     def Divide(self,a,b):
#         return a/b

# d=Derived()
# print(d.Summation(10,20))
# print(d.Multiplication(10,20))
# print(d.Divide(10,20))



# ..........................................................................................
# Hierarchical Inheritance

# oru parent class ine baaki ulla child class inherit cheyyunna reethi. ithil child class inte object diff aayirikkum . pinne child classes thammil connection undaavilla.



# # Base class
# class Parent:
#     def func1(self):
#         print("This function is in parent class")
    
# # Derived class 1
# class Child1(Parent):
#     def func2(self):
#         print("This function is in child 1")

# # Derived class 2
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child 2")

# c1=Child1()
# c1.func1()
# c1.func2()

# c2=Child2()
# c2.func1()
# c2.func3()



# ...................................................................................
# Hybrid Inheritance

# munnathe ethenkilum 2 inheritance koodi chernnathaan hybrid inheritance

# class Hotel:
#     def shop(self):
#         print("The Hotel has variety of food.")
# class Porotta(Hotel):
#     def taste(self):
#         print("Porotta tastes good.")
# class Biriyani(Hotel):
#     def smell(self):
#         print("Biriyani smells good.")
# class Food(Porotta,Biriyani):
#     def color(self):
#         print("Food are served in the hotel.")

# t=Porotta()
# t.shop()
# t.taste()

# s=Biriyani()
# s.shop()
# s.smell()




# h=Food()
# h.shop()
# h.taste()
# h.smell()
# h.color()


# .....................................................................................................................
# Polymorphism

# class Animal:
#     def speak(self):
#         print("speaking")
# class Dog(Animal):
#     def speak(self):
#         print("Barking")

# d=Dog()
# d.speak()



# class Bank:
#     def getroi(self):
#         return 10
# class SBI(Bank):
#     def getroi(self):
#         return 7
# class ICICI(Bank):
#     def getroi(self):
#         return 8
    
# b1=Bank()
# b2=SBI()
# b3=ICICI()
# print("Bank Rate of interest:",b1.getroi())
# print("SBI Rate of interest:",b2.getroi())
# print("ICICI Rate of interest:",b3.getroi())





# class Bird:
#     def intro(self):
#         print("There are many types of birds")
#     def flight(self):
#         print("Most of the birds can fly but some cannot")
# class Sparrow(Bird):
#     def flight(self):
#         print("Sparrow can fly")
# class Ostrich(Bird):
#     def flight(self):
#         print("Ostriches cannot fly")

# bird1=Bird()
# bird2=Sparrow()
# bird3=Ostrich()

# bird1.intro()
# bird1.flight()
# bird2.intro()
# bird2.flight()
# bird3.intro()
# bird3.flight()







# ............................................................................................
# Protected members

# class Base: 
# 	def __init__(self): 
# 		# Protected member 
# 		self._a = 2
# # Creating a derived class 
# class Derived(Base): 
# 	def __init__(self): 
# 		# Calling constructor of 
# 		# Base class 
# 		Base.__init__(self) 
# 		print("Calling protected member of base class: ", self._a) 
# 		# Modify the protected variable: 
# 		self._a = 3
# 		print("Calling modified protected member outside class: ", self._a) 
# obj1 = Derived() 

# obj2 = Base() 

# # Calling protected member 
# # Can be accessed but should not be done due to convention 
# print("Accessing protected member of obj1: ", obj1._a) 

# # Accessing the protected variable outside 
# print("Accessing protected member of obj2: ", obj2._a) 



# Private members

class Base: 
    def __init__(self):
        self.a = "Hello"
        self.__c = "World"

# Creating a derived class 
class Derived(Base): 
    def __init__(self): 

# Calling constructor of Base class 
        Base.__init__(self) 
        print("Calling private member of base class: ") 
        print(self.__c) 
obj1 = Base() 
print(obj1.a)

# Uncommenting print(obj1.c) will raise an AttributeError 
# Uncommenting obj2 = Derived() will also raise an AttributeError as private member of base class is called inside derived class 


