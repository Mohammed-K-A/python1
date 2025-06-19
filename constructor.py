# <<<<<<<<<<<<<<<<<<<<<<<<<<<<  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Parameterized constructor  (modelname and year aan ivdthe constructor)  (self ennullath invoke cheyyan ulla oru fn aan)


# class car:
#     def __init__(self,modelname,year):
#         self.modelname=modelname
#         self.year=year
#     def display(self):
#         print(self.modelname,self.year)
# c1=car("Toyota",2016)
# c1.display()


# Non parameterized constructor

# class Student:
#     def __init__(self):
#         print("This is non parameterized constructor")
#     def show(self,name):
#         print("Hello",name)
# student=Student()
# student.show("John")



# Default constructor

class Student:
    roll_num=101
    name="Joseph"

    def display(self):
        print(self.roll_num,self.name)
    
st=Student()
st.display()
