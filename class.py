# class in py == object in JS
# this keyword in JS == self parameter in py
class trial:
    name="harshita"
    age=21
    def greet(self):
        print(f"username {self.name} just Logged In")
        print(self)
a=trial()
a.greet()
class check:
    a=20
    b="hello"
    def inner(self):
        return f"{self.a} hello world"
class Incheck(check):
    d=30
    
var1=Incheck()       
print(var1.a)
print(var1.d)
print(var1.inner())    
# print(Incheck.inner())    # it will show error as methods/fxns cannot be accessed like this 

# INHERITANCE  above

# c=check()
# print(c.a)

class details:
    def __init__(self, stud_name,Grad_year,cgpa,stu_age):
        self.name=stud_name
        self.gyear=Grad_year
        self.marks=cgpa
        self.__age=stu_age  #private attribute
    def get_age(self):
        return self.__age
    def checkprint(self):
        if(self.gyear == 2027 and float(self.marks)>=8.0):
            return f"{self.name} of age {self.__age} is eligible to sit in Google Placement"
        else:
            return f"{self.name} is not eligible, TRY NEXT TIME, GOOD LUCK"
student1=details("Harshita", 2027,8.75,21)
student2=details("Riya", 2027,7.5,20)
# print(student1.checkprint())
# print(student1.gyear)
# print(student1.marks)

# ENCAPSULATION 
# try:
#     print(student1.__age)
# except AttributeError:
    # print(f"using   print(student1.__age) will show error")
    # print(f"correct way is   print(student1.get_age())")
    # print(student1.get_age())  #here it is correct 


# print(student1.__age)      # error as no attribute as __age hence no access to this attribute so reate getter method to access it.
# print(student2.checkprint())

# for encapsulation : Control over attribute access (read-only or conditional access)
# Getter methods provide controlled access to class attributes : get_attributename
# suppose we want that age of student cannot be accessed by any objects, we make few changes like add double underscore
#  like : __attributename

# POLYMORPHISM :
# import math 
# class rectangle:
#     def __init__(self, height, width):
#         self.h=height
#         self.w=width
#     def area(self):
#         return self.h*self.w
# class circle:
#     def __init__(self, radius):
#         self.r=radius
#     def area(self):
#         # return (math.pow(self.r,2)*3.14)
#         return ((lambda x : (x**2)*3.14)(self.r))
# shape=circle(4)
# print(shape.area(
