# ...................Default arguments..............................


# def function(n1,n2=20):
#     print("number 1 is: ",n1)
#     print("number 2 is: ",n2)

# print("Passing only 1 argument")
# function(30)



# .....................Keyword arguments.................................


# def function(n1,n2):
#     print("number 1 is: ",n1)
#     print("number 2 is: ",n2)

# print("Without using keyword")
# function(n2=50,n1=20)



# ................................anonymous fns.......................................


# single line fn
# keyword here is lambda
# no fn,return type,argument etc...


# Syntax:  .........................
# lambda[argument1[,argument2... argumentn]]: expression


# Code:  ..............

# lambda_=lambda argument1,argument2:argument1+argument2

# print("Value of fn is : ",lambda_(20,30))
# print("Value of fn is : ",lambda_(40,50))



# ................................Python fn within another fn..................


# def word():
#     string='Python fn tutorial'
#     x=5
#     def number():
#         print(string)
#         print(x)
#     number()
# word()



# .....................................Recursive fn....................................


def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))
num=3
print("The factorial of",num,"is",factorial(num))


# working of this above code

# factorial(3)                    1st call with 3
# 3*factorial(2)                  2nd call with 2
# 3*2*factorial(1)                3rd call with 1
# 3*2*1                           return from 3rd call as number=1
# 3*2                             return from 2nd call
# 6                               return from 1st call


