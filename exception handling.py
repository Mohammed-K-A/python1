# Type error

# x=5
# y="hello"
# z=x+y        

# Output
# Raises a TypeError:unsupported operand type(s) for +:'int' and 'str'


# try catch block to resolve it:
# x=5
# y="hello"
# try:
#     z=x+y
# except TypeError:
#     print("Error:cannot add an int and a str")




# Try and Except statement - Catching exceptions

# a=[1,2,3]
# try:
#     print("Second element=",a[1])
#     print("Fourth element=",a[3])
# except:
#     print("An error occurred")



# a=[1,2,3]
# try:
#     print("Second element=",a[1])
#     print("Fourth element=",a[3])
# except Exception as e:
#     print(e)





# Raising Exception


try:
    raise NameError("Hi there")
except NameError:
    print("An exception")
    raise