# Task 3

# name=input("What is your name?")
# age=int(input("How old are you?"))
# print(f"Hello,{name}!,You are {age} years old.") 

# task 4

# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# if n1 > n2:
#     n1 = n1 + 10
# else:
#     n1 = n1 - 5
# print("Updated first number:", n1)

# task 5

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# fav_number = int(input("Enter your favorite number: "))
# print(f"Hello, {name}! You are {age} years old, and your favorite number is {fav_number}.")

# task 8

# i=int(input("enter the mark:"))
# if(i<0 or i>100):
#     print("Invalid mark")
# elif(95<=i<=100):
#     print("High Distinction!")
# elif(i>=91):
#     print("O Grade")
# elif(i>=81):
#     print("A+ Grade")
# elif(i>=71):
#     print("A Grade")
# elif(i>=61):
#     print("B+ Grade") 
# elif(i>=51):
#     print("B Grade")
# elif(i>=41):
#     print("C+ Grade")
# elif(i>=31):
#     print("C Grade")
# elif(i>=21):
#     print("D Grade")
# else:
#     print("Failed")


# num=int(input("Enter a number : "))
# if num==0:
#     print(num,"is zero")
# elif num>0:
#     print(num,"is positive")
# else:
#     print(num,"is negative")




# Task 9

# sum = 0 
# for i in range(1,11):
#      sum = sum + i 
#      print("Sum:", sum)


# even_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in even_numbers:
#     if i % 2 == 0:
#         print(i)


# n=5
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         a=i*j
#         print(f"{i}*{j}={i*j}", end="\t")
#     print()




# Task 10

# pswd="python123"
# password= ""
# while password !=pswd:
#     password=input("Enter password : ")
# else:
#     print("Correct password.") 


# Find a Number in the List

# numbers=[1,2,3,4,5,6,7,8,9,10]
# target=3

# for i in numbers:
#     if i==target:
#         print("Number found!")
#         break
# else:
#     print("Number not found!")


# secret=24 
# guess=2  
# for i in range(guess):
#     a=int(input("Guess the secret number: "))
#     if a==secret:
#         print("Congratulations!....You guessed the correct number.")
#         break 
# else:
#     print("You failed to guess the number.") 




# >.........................................................................tsk 11
# Create a program to print a rectangle with 4 rows and 6 columns of stars.


# for i in range(4):        
#     for j in range(6):    
#         print("*", end=" ")
#     print()  

# 

# for i in range(5):
#     for j in range(5):
#         if i==0 or i==4 or j==0 or j==4:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# for i in range(5,0,-1):
#     for j in range(1, i + 1):
#         print(j,end=" ")
#     print()



# >................................................tks12

# def calculate_total(price,tax=5):
#     return price + (price*tax/100)
# print(calculate_total(100))



# items=["orange","cake"]
# def add_item(item):
#     global items  
#     items.append(item)
# add_item("apple")
# print(items)



# >>>>>>>>>>>>>>>......................................tsk 13

# Recursive function to reverse a string

# def reverse_string(s):
#     if len(s)==0: 
#         return s
#     else:
#         return reverse_string(s[1:]) + s[0] 
# print(reverse_string("hello")) 



# square=lambda x: x*x
# print(square(7))



# Task 15

# my_fav_food=['Mandi','Biriyani','Fried Chicken','Porotta','Masala Dosa']
# for i in my_fav_food:
#     print(f"I love eating {i}")


# Task 16

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square = [x ** 2 for x in numbers]
# print("square of numbers = ",square)



# text = 'Python Programming is fun!'
# vowels = 'aeiouAEIOU'
# vowel_list = [char for char in text if char in vowels]
# print("Extracted vowels are : ",vowel_list)


# no = list(range(1, 21))
# even_num = [i for i in no if i % 2 == 0]
# print("Even numbers = ",even_num)




# Task 17

# char = "Hello"
# print(char[0], char[-1]) 


# text= "Hello"
# reversed_text = text[::-1] 
# print(reversed_text)


# text = "Hello"
# print(text.count("l"))


# txt = "How are you?" 
# print(txt.replace(" ", "_"))


# pal_word = "malayalam" 
# print(pal_word == pal_word[::-1])




# Task 18

# names=["rashid","momi","sulu","fahad"]
# grades=[85, 92, 78, 90]
# s_grades=dict(zip(names, grades))
# print(s_grades)


# list1=[10,20,30,40]
# list2=[1,2,3,4]
# sum=[a + b for a, b in zip(list1, list2)]
# print(sum)




# Task 19

# days_of_week=('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
# print("First day: ",days_of_week[0])
# print("Second day: ",days_of_week[1])
# print("Third day: ",days_of_week[2])
# print("Slicing : ",days_of_week[3:6])
# print("Index of Wednesday : ",days_of_week.index('Wednesday'))



# student_name = ["Mohammed", "Rashid", "Fahad", "Mohammed", "Sultan", "Rashid"]
# unique_students = set(student_name)
# print("Unique Students:", unique_students)


# set1={3,6,1,7,11,15,24,36,77,100,2}
# set2={4,6,3,100,36,71,54}


# print("Union:", set1 | set2)


# print("Intersection:", set1 & set2)


# print("Difference (set 1 - set 2):", set1 - set2)


# is_subset = set2.issubset(set1)
# print("Is set 2 a subset of set 1?", is_subset)

