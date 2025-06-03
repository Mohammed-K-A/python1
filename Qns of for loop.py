# Concept of for loop

# numbers=[4,2,6,7,3,5,8,10,6,1,9,2]
# square=0
# squares=[]
# for value in numbers:
#     square=value**2
#     squares.append(square)
# print("The list of square is",squares)



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# 1. sum of all even numbers btw 1 and N

# num=int(input("Enter the number:"))
# sum=0
# for i in range(num+1):
#     if i%2==0:
#         sum=sum+i
# print(sum)


# 2. count vowels in a string

# string=input("enter the string")
# vowels=['A','a','E','e','I','i','O','o','U','u']
# count=0
# for i in string:
#     if i in vowels:
#         count=count+1
# print(count)



# 3. Find the maximum number in a list.
# Given a list of numbers, use a for loop to find the maximum number


# list1=[100,200,500,50,150,300]
# max=0
# for i in list1:
#     if i>max:
#         max=i
# print("the maximum number is",max)


# 4. Calculate the product of all numbers in a list.
# Given a list of numbers, write a program to calculate the product (multiplication) of all the numbers using a for loop.


# list=[2,3,4,5,6]
# mul=1
# for i in list:
#     mul=mul*i
# print("The product of all number is",mul)


# 5. Reverse a string using a for loop.
# Input a string and print its reverse using a for loop.


# str=input("Enter a string:")
# rev=""
# for i in str:
#     rev=i+rev
# print(rev)


# 6. Print characters at even indices.
# Input a string and use a for loop to print characters at even positions (index 0, 2, 4, …).


# str=input("Enter a character:")
# b=""
# for i in range(0,len(str),2):
#     b=b+' '+(str[i])
# print(b)



# 7. Find common elements in two lists.
# Input two lists and use a for loop to print elements present in both


# a=[1,2,3,4,6,3]
# b=[3,1,9,20,4]
# c=[]
# for i in a:
#     if i in b and i not in c:
#          c.append(i)
# print(c)



# 8. Sum of digits btw numbers using for loop


num=int(input("Enter the number:"))
b=len(str(num))
sum=0
for i in range(0,b):
    d=num%10
    sum=sum+d
    num=num//10
print("Sum is",sum)
