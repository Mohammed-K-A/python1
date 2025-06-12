#Day_3
# name=input("What is your name? ")
# age=int(input("How old are you? "))
# print("Hello, ",name,"!","You are ",age," years old. ")

#--------------------------------------------------------------------------------------------------------------

#Day_4

# a=int(input("Enter the First number : "))
# b=int(input("Enter the Second number : "))
# if(a>b):
#     a+=10
# else:
#     a-=5
# print("Updated number : ",a)

#--------------------------------------------------------------------------------------------------------------

#Day_5

# name=input("Enter your name: ")
# age=int(input("Enter your age: ")) 
# fn=int(input("Enter your favorite number: ")) 
# print(f"Hello, {name}! You are {age} years old, and your favorite number is {fn}.")

#--------------------------------------------------------------------------------------------------------------

#Day_8

#grade
# i=int(input("Enter your Mark : "))
# if(i<101 and i>-1):
#     if(i>=95):
#         print("Your grade is A+,Congratulations on achieving a High Distinction!")
#     elif(i>=90 and i<95):
#         print("Your grade is A")
#     elif(i>=80 and i<90):
#         print("Your grade is B")
#     elif(i>=70 and i<80):
#         print("Your grade is C")
#     elif(i>=60 and i<70):
#          print("Your grade is D")
#     elif(i<60 ):
#         print("You failed")
# else:
#     print(' Enter Invalid Mark')


#+-0
# i=int(input("Enter your number : "))
# if(i<0):
#     print(i,'is a Negative number')
# elif(i>0):
#         print(i,'is a Positive number')

# else:
#     print('is zero')
    
#--------------------------------------------------------------------------------------------------------------

#Day_9

#Sum of digits from 1 to 10
# add=0
# for i in range(0,11):
#     add += i
    
# print("Sum : ", add)

#Filter even numbers from list
# e=[1,2,3,4,5,6,7,8,9,10]
# for i in e:
#     if(i%2==0):
#         print(i)


# Multiplication table
# t=0
# for i in range(1,11):
#     for j in range(1,6):
#         t=i*j
#         print(f"{i} x {j} = {t}",end="      ")
#     print()
        

    
#--------------------------------------------------------------------------------------------------------------

#Day_15

# e=["Fried chicken","Momos","Sandwich","Fries","Potato chips"]
# for i in e:
#     print("I love eating ",i)

    
#--------------------------------------------------------------------------------------------------------------

#Day_16

#vowels
# f='Python Programming is fun!'
# vowels='aeiou'
# u=''
# for i in f:
#     if i in vowels:
#         u+=i
# print('Vowels in ',f,'is :',u)

#even numbers
# n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# list = [i for i in n if i % 2 != 0]
# print(list)


# n= [1,2,3,4,5,6,7,8,9,10]
# a = [x ** 2 for x in n]
# print(a)

# list = [i for i in range(11) if i % 2 == 0]
# print(list)

#--------------------------------------------------------------------------------------------------------------

# #Day_17

# x="timing"
# # print("First letter: ",x[0])
# # print("Second letter: ",x[-1])

# # print("Reversed string : ",x[::-1])

# print(x.count('i'))


# r="How much is it ?"
# e=r.replace(" ","_")
# print(e)


# o="mom"

# if(o==o[::-1]):
#     print(o,"is Palindrome")
# else:
#     print(o,"is not Palindrome")


#--------------------------------------------------------------------------------------------------------------

#Day_18

# students=['Lilly','Ayesha','Miya','Linsy','Winter']
# grades=['C','D+','C+','D','B']
# v=zip(students,grades)
# print(dict(v))
#--------------------------------------------------------------------------------------------------------------

#Day_19


# week=('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
# print("Second Element of tuple: ",week[1])
# print("Slicing : ",week[4:7])
# print("Index of Wednesday : ",week.index('Wednesday'))


#set
# s1={4,3,6,44,7,88}
# s2={4,5,2,77,65,88}

# print(s1&s2) #-------------------Intersection
# print(s1|s2) #-------------------Union

# print(s1-s2) #-------------------Difference
# print(s1>s2) #------------------- s2 is not subset of s1