# lamda arguments : expression
# num=lambda a,b : 10*a+5*b
# print(num(10,2))
# print(num(b=10,a=2))

# notify=lambda x,name : print(f"username is {name} and age is {x}")
# notify("harshita", 21)
# print(notify("harshita", 21))

# map/filter/reduce are higher order fxns ,which takes another fxn as argument

# map apply fxn to each element in a sequence and return a sequence with modified elements
# map synyax : map(fxn, iterable)
# l=[10,20,30]
# new=map(lambda x: x*x, l)
# newl=list(map(lambda x: x*x, l))
# print(type(new))
# print(new)
# print(type(newl))
# print(newl)

#filter fxn filters the the elements in sequence based on the given predicate and returns a new sequence having elements that meets the predicate
# syntax is filter(predicate, iterable) , here predicate is a fxn that return boolean value.
# l=[10,20,30]
# ltype=filter(lambda x : x>16, l)
# newl=list(filter(lambda x : x>16, l))
# print(newl)
# print(type(ltype))

# import functools for using reduce .
# syntax is reduce(fxn, iterable)
# reduce takes 2 arguments at a time and return a result.
# it apply fxn on 1st 2 elements in a sequence and then apply fxn to 
# the result and next element.
# import  functools
# l=[10,20,30]
# result=functools.reduce(lambda x,y : x+y,l)
# print(result)

# is and == both are comparision operator 
# is check the location of object in memory, == checks the value.
#  all the immutable values like constants/ tuple/strings get the 
# same memory location,bcoz, they will not get changed then why to waste memory.
# a=10
# b=10
# x=[1,2,3]
# y=[1,2,3]

# print(a==b)
# print(a is b)
# print(x==y)
# print(x is y)
import random
opt=[1,2,3]
result=["Win","Lost","Draw"]
while(True):
    print("enter\n 1 : Snanke\n 2 : Gun\n 3 : Water\n 4 : Exit")
    user=int(input("enter your choice"))
    if (user==4):
        break
    comp=random.choice(opt)
    print(f"computer's choice is {comp}")
    if (user==comp):
        print(result[2])
    elif (comp+1==user or user+2==comp):
        print(result[0])
    else:
        print(result[1])
print("Game over !!")
