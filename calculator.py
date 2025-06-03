print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

option=int(input("Choose an option:"))

if(option==1):
    x=int(input("Enter the first number:"))
    y=int(input("Enter the second number:"))
    sum=x+y
    print(sum)

elif(option==2):
    x=int(input("Enter the first number:"))
    y=int(input("Enter the second number:"))
    sub=x-y
    print(sub)

elif(option==3):
    x=int(input("Enter the first number:"))
    y=int(input("Enter the second number:"))
    mul=x*y
    print(mul)

elif(option==4):
    x=int(input("Enter the first number:"))
    y=int(input("Enter the second number:"))
    if(y>0):
        div=x/y
        print(div)
    else:
        print("Cannot Divide")
else:
    print("Invalid option")