
# with star

# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         print(" * ",end=" ")
#     print()


# with numbers

# n=5
# a=1
# for i in range(0,n):
#     for j in range(0,n):
#         print(a,end=" ")
#         a+=1
#     print()



# right half pyramid with star (1-5)

# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()



# inverted right half pyramid with star (5-1)

# n=5
# for i in range(0,n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()




#full pyramid with star

# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end="")
#     for k in range(0,i+1):
#         print("* ",end="")
#     print()


# inverted full pyramid with star

# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end="")
#     for k in range(0,n-i):
#         print("* ",end="")
#     print()



#left half pyramid with star

# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print("",end=" ")
#     for k in range(0,i+1):
#         print("*",end="")
#     print()




# inverted left half pyramid with star

# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end="")
#     for k in range(0,n-i):
#         print("*",end="")
#     print()



# rhombus pattern

# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end="")
#     for k in range(0,n):
#         print("* ",end="")
#     print()



# floyd's triangle

# n=5
# a=1
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(a,end=" ")
#         a+=1
#     print()



# diamond pattern

# n=6
# for i in range(0,n-2):
#     for j in range(0,n-i):
#         print(" ",end="")
#     for k in range(0,i+1):
#         print("* ",end="")
#     print()
# for l in range(0,n-3):
#     for m in range(0,n-2+l):
#         print(" ",end="")
#     for o in range(1,n-2-l):
#         print("* ",end="")
#     print()



# Hourglass pattern

# n=4
# for i in range(0,4):
#     for j in range(0,i+1):
#         print(" ",end="")
#     for k in range(n-i):
#         print("* ",end="")
#     print()
# for b in range(0,3):
#     for c in range(0,n-1-b):
#         print(" ",end="")
#     for d in range(0,b+2):
#         print("* ",end="")
#     print()



# Hollow square pattern

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("* ",end="")
#         else:
#             print(" ",end=" ")
#     print()



# Hollow full pyramid

# n=5
# for i in range(n):
#     for j in range(0,n-i):
#         print(" ",end="")
#     for k in range(0,i+1):
#         if i==(n-1):
#             print("* ",end="")
#         elif k==0 or k==i:
#             print("* ",end="")
#         else:
#             print(" ",end=" ")
#     print()



# Hollow inverted full pyramid

n=5
for i in range(n):
    for j in range(0,i+1):
        print(" ",end="")
    for k in range(0,n-i):
        if i==0 or k==0 or k==n-i-1:
            print("* ",end="")
        else:
            print(" ",end=" ")
    print()




# Hollow diamond pyramid

