# Syntax of the while loop is:

#  while <condition>:  
#       { code block } 


# Concept of while loop

# count = 1
# while count <= 5:
# 	print(count)
# 	count += 1



# 1. Print numbers from 10 to 1.
# Write a Python program using a while loop to print numbers from 10 down to 1.


# count=10
# while count>0:
#     print(count)
#     count=count-1



# 2. Sum of digits.
# Write a program that takes a number as input and calculates the sum of its digits using a while loop


# num=int(input("Enter the number:"))
# digit_sum=0
# while num>0:
#     digit=num % 10
#     digit_sum=digit_sum+digit
#     num=num // 10
# print("Sum of digits is",digit_sum)


# 3. Check if a number is a palindrome.
# Write a Python program using a while loop to check if the entered number is a palindrome (same forwards and backwards)


# num=int(input("Enter a number:"))
# orginal=num
# rev=0
# while num>0:
#     rev=rev*10 + num%10
#     num=num//10
# if orginal==rev:
#     print("The number is palindrome")
# else:
#     print("The number is not palindrome")



# 4. Count the number of digits.   
# Input a number and count how many digits it has using a while loop.


# num=int(input("Enter the number:"))
# count=0
# if num==0:
#     count=1
# else:
#     while num>0:
#         count=count+1
#         num=num//10
# print("Number of digits:",count)



# 5. Keep asking input until user enters ‘quit’
# Write a program that keeps asking the user to enter a word, and stops only when they type 'quit'.


# a=""
# while a.lower()!= "quit":
#     a=input("Enter the word:")



# 6. Count how many times a digit appears
# Input a number and a digit, then count how many times that digit appears in the number using a while loop.


# num=int(input("Enter the number :"))
# digit=int(input("Enter the digit to count:"))
# count=0
# while num>0: 
#     d=num%10
#     if d==digit:
#         count+=1
#     num=num//10       
# print(count,"times the digit appears")



# 7. Check for Armstrong number
# Input a number and use a while loop to check if it’s an Armstrong number (e.g., 153 → 1³ + 5³ + 3³ = 153).


# num= int(input("Enter a number: "))
# original=num  
# sum = 0
# while num > 0:
#     digit = num % 10        
#     sum += digit ** 3       
#     num = num // 10         
# if sum == original:
#     print(original, "is an Armstrong number.")
# else:
#     print(original, "is not an Armstrong number.")




# input any number using while loop and if entered -1 , add all the numbers entered previously as input


a=int(input("Enter a number:"))
sum=0
while a!=-1:
    sum=sum+a
    a=int(input("Enter a number:"))
print(sum)
