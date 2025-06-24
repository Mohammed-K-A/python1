# Qn: First unique character in a string
# Given a string s, find its first non-repeating character and return its index. If it does not exist, return -1.

# string = input("Enter a string: ")
# if 1 <= len(string) <= 10**5:
#     for i in range(len(string)):
#         count=string.count(string[i])
#         if count == 1:
#             print(i)
#             break
#     else:
#         print("-1")
# else:
#     print("Enter a valid length")




# Qn. First missing positive number

a= [4,3,5,77,94]
b=[]

for i in a:
    if i > 0:
        b.append(i)

c = 1
while True:
    if c not in b:
        print("First missing positive:", c)
        break
    c += 1















