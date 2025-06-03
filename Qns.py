# # sum of all even numbers btw 1 and N

# num=int(input("Enter the number:"))
# sum=0
# for i in range(num+1):
#     if i%2==0:
#         sum=sum+i
# print(sum)


# count vowels in a string

# str=input("enter the string")
# vowels=['A','a','E','e','I','i','O','o','U','u']
# count=0
# for i in str:
#     if i in vowels:
#         count=count+1
# print(count)



# Find the maximum number in a list.Given a list of numbers, use a for loop to find the maximum number


# list1=[100,200,500,50,150,300]
# max=0
# for i in list1:
#     if i>max:
#         max=i
# print("the maximum number is",max)


# Calculate the product of all numbers in a list.Given a list of numbers, write a program to calculate the product (multiplication) of all the numbers using a for loop.


# list=[2,3,4,5,6]
# mul=1
# for i in list:
#     mul=mul*i
# print("The product of all number is",mul)


# Reverse a string using a for loop.Input a string and print its reverse using a for loop.


# str=input("Enter a string:")
# rev=""
# for i in str:
#     rev=i+rev
# print(rev)


# Print characters at even indices.Input a string and use a for loop to print characters at even positions (index 0, 2, 4, …).


# str=input("Enter a character:")
# b=""
# for i in range(0,len(str),2):
#     b=b+' '+(str[i])
# print(b)


#  Find common elements in two lists.Input two lists and use a for loop to print elements present in both


list1=input("Enter the elements of first list:").split()
list2=input("Enter the elements of second list:").split()
common=[]
for i in list1:
    if i in list2:
        common.append(i)
print("The common elements are",common)
