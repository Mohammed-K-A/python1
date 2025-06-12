i=int(input("enter the mark:"))
if(i<0 or i>100):
    print("Invalid mark")
elif(95<=i<=100):
    print("High Distinction!")
elif(i>=91):
    print("O Grade")
elif(i>=81):
    print("A+ Grade")
elif(i>=71):
    print("A Grade")
elif(i>=61):
    print("B+ Grade") 
elif(i>=51):
    print("B Grade")
elif(i>=41):
    print("C+ Grade")
elif(i>=31):
    print("C Grade")
elif(i>=21):
    print("D Grade")
else:
    print("Failed")