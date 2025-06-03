number=input("Enter the no:")
sum_digits = 0

for digit in str(number):
    sum_digits += int(digit)

print("Sum of digits:", sum_digits)
