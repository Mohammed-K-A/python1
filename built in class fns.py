# Python Built-in Class Fns


class Student:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age

# creates the object of class Student
s=Student("John",101,22)                          #created object of class

# prints attribute name of the object  s               
print(getattr(s,'name'))                               #output = John

# reset the value of attribute age to 23
setattr(s,"age",23)                                  #reset age 22 into 23

# prints the modified value of age
print(getattr(s,'age'))                                #output = 23

# prints true if the student contains the attribute with name id
print(hasattr(s,'id'))                                                    #output = True

# deletes the attribute age
delattr(s,'age')                             #deletes the age attribute

# this will give an error since the attribute age has been deleted
print(s.age)                                                                  #output = error message will display due to the deletion of age attribute

