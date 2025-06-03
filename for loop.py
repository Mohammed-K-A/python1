# Concept of for loop

# numbers=[4,2,6,7,3,5,8,10,6,1,9,2]
# square=0
# squares=[]
# for value in numbers:
#     square=value**2
#     squares.append(square)
# print("The list of square is",squares)



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




# else statement with for loop



# string="python loop"
# for s in string:
#     if s=="o":
#         print("If block")
# else:
#     print(s)



# range function


# print(range(15))
# print(list(range(15)))
# print(list(range(1,5)))
# print(list(range(1,25,4)))

tuple_=("Python","Loops","Sequence","Condition","Range")
for iterator in range(len(tuple_)):
    print(tuple_[iterator].upper())