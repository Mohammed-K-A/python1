# example of user defined fn

def square(num):
    return num**2
object_=square(6)
print("the square of the given number is:",object_)

# user input for only 1 operation

# def square(num):
#     return num**2                                                                        
# square_=int(input("Enter a number: "))
# print("the square of the given number is:",square(square_))

# OR for more than 1 operation

# def square(num):
#     return num**2                                                                        
# square_=int(input("Enter a number: "))
# a=square(square_)
# print("the square of the given number is:",a)


# overriding

# def square(num,num1):
#     return(num**num1)

# def square(num,num1):
#     return(num+num1)

# a=int(input("Enter the number: "))
# b=int(input("Enter the power: "))
# print(square(a,b))

# calling a fn

# def a_function(string):
#     "This prints the value of length of string"
#     return len(string)

# print(a_function("Functions"))
# print(a_function("Python"))


# With argument with return type
# fn to calculate square of num

# def square(num):
#     return num*num
# result=square(5)
# print("Square:",result)

# With argument without return type
# fn to print greeting message

# def greet(name):
#     print("Hello",name + "!")
# greet("Anu")


# Without argument with return type
# fn that returns a welcome message

# def get_message():
#     return "Welcome to Python Programming!"

# msg=get_message()
# print(msg)


# Without argument without return type
# fn to print num from 1 to 5

def print_numbers():
    for i in range(1,6):
        print(i)
print_numbers()