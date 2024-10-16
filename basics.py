# by default  end = \n  and sep= space
# print("harshita",4,5,sep='*', end="@gmail.com")
# print("hello")
# a=None
# b=True
# c="true"
# d=10
# print(type(a),type(b),type(c),type(d))
# a1=complex(10,0)
# b1=complex(2,4)
# print(a1,b1, type(b1))

# size :  boolean (1 byte) < char(2 bytes) < int (4 byte) < float (4 or 8 byte)
#implicit type casting, is on the basis of more sized data type

# print(type(1+2.4))
# poem='''helore
# ut is ebodbej2
# dfefljidd
# deijd eo3ej32 ei3ne32 ien'''
# print(poem)
#STRINGS
name="harshita_is_a_good_girl"
# print(name.title())
# print(name.capitalize())
# print(name[-1])
# print(name[8])
# for i in name:
#     print(i)
# print(name[0:8])
print(name[:8])
print(name[:])
print(name[0:])
print(name[-8:])
str1="hello"
print(str1)
# del str1
print(str1)
print(list(enumerate(str1)))
# print(name[-1::-1])  
# print(name[-8::1])
# print(name[7::-1 ])
# print(name, "is",len(name),"lettered word" )
# greet="hello!!!"
# greet1="hello@@@"
# print(greet1.endswith("@@@@@"))
# print(greet.find("o!@"))
# print(greet1.endswith("@"))

#MATCH CASE 
# x= int(input("enter a number"))
# match x:
#     case _ if x>=18:
#         print("ok")
#     case _ if x>=22:
#         print("extreme ok yes")
#     case _:
#         print("not eligible")

# def greater(a,b):
#     if(a>b):
#         print(a, "is greater than ", b)
#     else:
#         print(b, "is greater than ", a)


# def gmean(a,b):
#     greater(a,b)
#     return (a*b)/(a+b)
# print(gmean(10,20))

# def add(a=2,b=4):
#     print(a+b)
# add(10,20)
# add()
# add(9)
# add(b=10)

# tup1=(1,2,3,4)
# templ=list(tup1)
# templ.pop(2)
# templ.append(5)
# tup1=tuple(templ)
# print(tup1)
# using format string, below
# print("Username {} just logged in".format("Harshita"))
# # using f string, below
# age =21
# print(f"Age of this Username is {age} ") 
# # to retain the variable name in the output, use double {}
# print(f"Age of this Username is {{age}} ") 
# price=299.64654
# print(f"the total price of book is {price:.3f}")  
# print(f"{5*10}")

# import this
# zen of python
# doc string 
def greet():
    '''this is to greet username'''
    print("hello")
    print(greet.__doc__)
# greet()
# print(greet.__doc__)
import sys
p=20
# print(hex(id(p)))
# print(isinstance(9+1j, complex))
# print(sys.getsizeof(p))
# print(bool(0))
# print(bool(1))










