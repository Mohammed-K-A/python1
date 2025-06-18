# f=open('file.py','x')       #file creation


# <<<<<<<<<<<<<<<<<<<  read  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# file=open('file.py','r')    #to read the whole file
# for each in file:
#     print(each)


# f=open('file.py','r')       #to read line by line of the file 
# print(f.readline())
# print(f.readline())
# f.close()



# file=open("file.py","r")      #to read the whole file without using for loop
# print(file.read())



# with open("file.py") as file:      #to read file by another method
#     data=file.read()
# print(data)



# file=open("file.py","r")          #to read characterwise
# print(file.read(5))



# with open("file.py","r") as file:         #to split characters in file
#     data=file.readlines()
#     for line in data:
#         word=line.split()
#         print(word)



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<  write  >>>>>>>>>>>>>>>>>>>>>>>>>>>>


# file=open('file write.py','w')                                            #write cheyyumbol munnathe content poyi new content add aavum
# file.write("This is the write command")
# file.write("\nIt allows us to write in a particular file")
# file.close()


# file=open('file write.py','w')             
# file.write("Hi")
# file.write("hello")
# file.close()


# file=open('file write.py','a')                   #append the file(content munnathethinte koode add aavum puthiyath)
# file.write("This will add this line")
# file.close()