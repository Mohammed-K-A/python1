# map object എന്നത് എന്താണ്?

# അതൊരു iterator ആണു.

# അതിന്റെ ഫലം ഉടൻ കാണിക്കില്ല.

# അതിന്റെ ഉള്ളടക്കം കാണാൻ നിങ്ങൾക്ക് list(result) പോലെ മാറ്റണം.


# What is map()?

#  The map() function in Python is used to apply a given function to all the items in an iterable (like a list or tuple) and return a map object (an iterator)
#  You can convert the map object to a list or other iterable type using the list() function



#  Syntax:
# map(function, iterable)


# Example: 

# def square(n):                              #output = [1,4,9,16]
#     return n * n
# numbers = [1, 2, 3, 4]
# result = map(square, numbers)
# print(list(result))




#  <<<<<<<<<<<<<<<<<<<<<<<  Using map() with lambda  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# Lambda functions are often used with map() to create anonymous functions for short operations.
#  
# Example:
 
# numbers = [1, 2, 3, 4]                                  #output = [1,4,9,16]
# result = map(lambda x: x * x, numbers)
# print(list(result))




# <<<<<<<<<<<<<<<<<<<<<  Using map() with multiple iterables   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#  The map() function can also take more than one iterable. The function should then take as many arguments as there are iterables.

#  Example:

# numbers1 = [1, 2, 3]                                              # Output: [5, 7, 9]
# numbers2 = [4, 5, 6]
# result = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result))  



#  Key Points:

# - map() returns a map object which is an iterator.
# - You need to convert it to list, tuple, etc., to view the results.
# - Works with user-defined functions and lambda functions.
# - Can take multiple iterables as input
