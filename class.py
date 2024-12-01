# class in py == object in JS
# this keyword in JS == self parameter in py
# instance == objects 
# methods == functions
# 1. instance method
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
# print(var1.a)
# print(var1.d)
# print(var1.inner())    
# print(Incheck.inner())    # it will show error as methods/fxns cannot be accessed like this 

# INHERITANCE  above

# c=check()
# print(c.a)

class details:
    total=0
    def __init__(self, stud_name,Grad_year,cgpa,stu_age):
        self.name=stud_name
        self.gyear=Grad_year
        self.marks=cgpa
        self.__age=stu_age  #private attribute
        # self.total += 1 # it does not work 
        details.total += 1

    def get_age(self):
        return self.__age
    
    def set_age(self,new_age):
        if (new_age>0):
            self.__age=new_age
            return self.__age
        else:
            print("enter valid age")
    
    @staticmethod
    def returnCheck():
        return "hello all!"
    
    @property
    def cgpa(self):
        return self.marks

    
    def checkprint(self):
        if(self.gyear == 2027 and float(self.marks)>=8.0):
            return f"{self.name} of age {self.__age} is eligible to sit in Google Placement"
        else:
            return f"{self.name} is not eligible, TRY NEXT TIME, GOOD LUCK"
# print(details.total)
student1=details("Harshita", 2027,8.75,21)
student2=details("Riya", 2027,7.5,20)
student3=details("arya", 2027,9.5,20)


# using setter method, we can change private attributes also
# goto set_age()
# print(student3.set_age(39))
# print(student3.get_age())

# print(student1.returnCheck())  #return error : if "self" is not mentioned :else if  no constructor(self) and no decorator(@..)
# print(details.returnCheck())  #By default, methods in a Python class that do not include self can be called directly using the
# class name. However, for clarity and convention, such methods should be explicitly decorated with @staticmethod
#  @staticmethod works on both, obj.method() and class.method()

#  ATTRIBUTES EDITABLE
student4=details("neha", 2027,6.5,20)
student4.name="shikha"
# print(student4.name)
# print(student4.checkprint())

# READ ONLY ATTRIBUTES but accessible
# @property decorator
# /this decorator allows the method to be used as property
# print(student3.cgpa())   #error, as not to be used as method
print(student3.cgpa)




# print(student2.checkprint())
# print(details.total)

# print(student1.checkprint())
# print(student1.gyear)
# print(student1.marks)

# ENCAPSULATION 
# try:
#     print(student1.__age)
# except AttributeError:
#     print(f"using   print(student1.__age) will show error")
#     print(f"correct way is   print(student1.get_age())")
#     print(student1.get_age())  #here it is correct  and get_age is a function


# print(student1.__age)      # error as no attribute as __age hence no access to this attribute so create getter method to access it.
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
# print(shape.area)
