# <<<<<<<<<<<<<<  classwork  >>>>>>>>>>>>>>>>>>>

# 1 . Write a function that takes a list of numbers and returns the maximum.

# def num():
#     a=[2,1,4,7,5,6,3]
#     max=0
#     for i in a:
#         if i>max:
#             max=i
#     print(max)
# num()



# 2 . Define a function that returns the reverse of a given string.

# def str():
#     a=input("Enter a string:")
#     rev=""
#     for i in a:
#         rev=i+rev
#     print(rev)
# str()


# 3 . Write a function that takes a string and counts the number of vowels.

# def vow():
#     a=input("Enter a character:")
#     count=0
#     for i in a:
#         if i in['a','i','o','e','u','A','E','I','O','U']:
#             count=count+1
#     print(count)
# vow()



# 4 . Create a function to check if a number is a palindrome.

# def pal():
#     num=int(input("Enter a number:"))
#     orginal=num
#     rev=0
#     while num>0:
#         rev=rev*10 + num%10
#         num=num//10
#     if orginal==rev:
#         print("The number is palindrome")
#     else:
#         print("The number is not palindrome")
# pal()



# 5 . Define a function that accepts a list and returns a new list with only even numbers.

# def even_no():
#     n=int(input("Enter a number : "))
#     even_list=[]
#     for i in range(1,n+1):
#         if (i % 2 == 0):
#             even_list.append(i)
#     print(even_list) 
# even_no()



# 6 . Write a function that calculates the power of a number (without using ** or pow).

# def power(num, power):
#     ans = 1
#     for i in range(power):
#         ans = ans * num
#     print("power:", ans)
# a=int(input("Enter number : "))
# b=int(input("Enter power : "))
# power(a,b)



#7 . Create a menu-driven program using functions:

# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def mul(x,y):
#     return x*y
# def div(x,y):
#     if y!=0:
#         return x/y
#     else:
#         print("Cannot divide by 0!")

# def home():
#     while True:
#         print("\nMENU:")
#         print("1.ADD")
#         print("2.SUBTRACT")
#         print("3.MULTIPLY")
#         print("4.DIVIDE")
#         print("5.EXIT")

#         choice=int(input("Enter your choice:"))

#         if choice == 5:
#             print("Exited!")
#             break

#         a=int(input("Enter 1st number:"))
#         b=int(input("Enter 2nd number:"))

#         if choice == 1:
#             print("Answer:",add(a,b))

#         elif choice == 2:
#             print("Answer:",sub(a,b))

#         elif choice == 3:
#             print("Answer:",mul(a,b))

#         elif choice == 4:
#             print("Answer:",div(a,b))

#         else:
#             print("Invalid choice")

# home()




#  <<<<<<<<<<<<<<<<<<<<<<<<  homework   >>>>>>>>>>>>>>>>>>>>>>>>>>


# <<<<<<<<<<< recursive fns >>>>>>>>>>>>>>>>>

# 1 . Write a recursive function to print numbers from n to 1.

# def print_no(n):
#     if n != 0:   
#         print(n)
#         print_no(n - 1)
# no=int(input("Enter a number:"))
# print_no(no)


# 2 . Write a recursive function to calculate the sum of first n natural numbers.

# def sum_no(n):
#     if n != 0:
#         return n + sum_no(n - 1)
#     else:
#         return 0
# no = int(input("Enter a number: "))
# print("Sum =", sum_no(no))


#3 . Write a recursive function to find the sum of digits of a number.

# def sum_dig(num):
#     if num!=0:
#         return num % 10 + sum_dig(num // 10)
#     else:
#         return 0
# sum = int(input("Enter a number: "))
# print("Sum of digits :", sum_dig(sum))


#4. Write a recursive function to reverse a string.

# def reverse(string):
#     if len(string) == 0:
#         return string
#     return reverse(string[1:]) + string[0]

# text = input("Enter a string: ")
# print("Reverse of the string:", reverse(text))



# <<<<<<<<<<<<<<<<<  lambda fns  >>>>>>>>>>>>>>>>>>>>>>>


#1 . Write a lambda function to find the square of a number.

# square=lambda num1: num1**2
# num=int(input("Enter a number:"))
# print("The square of number is:",square(num))


#2 . Write a lambda function to check if a number is even or odd.

# even = lambda n: "Even" if n % 2 == 0 else "Odd"
# num = int(input("Enter a number: "))
# print("The number",num,"is", even(num))


#3 . Write a lambda function to find the maximum of two numbers.

# max = lambda num1,num2: num1 if num1>num2 else num2
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# print("The greater number is:", max(num1,num2))


# 4 . Write a lambda function to check if a string starts with the letter 'A

# txt = lambda str: "True" if str[0]=='A' or str[0]=='a' else "False"
# a=input("Enter a string: ")
# print("It is", txt(a),"that the string starts with the letter A or a")

