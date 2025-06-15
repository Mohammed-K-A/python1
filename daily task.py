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

