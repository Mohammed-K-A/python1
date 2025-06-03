print("Enter 3 numbers:")
a=int(input("Enter the 1st no:"))
b=int(input("Enter the 2nd no:"))
c=int(input("Enter the 3rd no:"))
if(a==b and b==c and a==c):
    print("Numbers are equal")
elif(a>b and a>c):
    print(a,"is greatest")
elif(b>a and b>c):
    print(b,"is greatest")
else:
    print(c,"is greatest")