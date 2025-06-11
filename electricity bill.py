unit=int(input("Enter the unit: "))
if unit<=100:
    print(unit*5)
elif unit<=200:
    a=(100*5)+((unit-100)*8)
    print(a)
else: 
    b=(100*5)+(100*8)+((unit-200)*10)
    print(b)
    

