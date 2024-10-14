# # error handling
# def func():
#     a=input("enter a number ")
#     print(f"multiplication of {a} is below")
#     try:
#         for i in range (1,11):
#             print(f"{a} X {i} = {int(a)*i}")
#         print([2,3][int(a)])
#         return 1
#     except ValueError:
#         print(" input is not integer ")
#         c=10
#         print(c)
#         return 0
#     except IndexError:
#         print("Out of index")
#         print("this is imp line of code")
#         return 0
#     print("i am outside finally and will not be executed")
#     # finally:
#     #     print("i am inside finally and will always executed")
# print(func())

# raising custom errors
# i=int(input("enter a number between 5  and 10 : "))
# if(i>10 or i<5):
#     raise ValueError("Enter number in given range")
# print(i)

# ch=input("enter a number")
# if(str(ch).lower()=="quit"):
#     pass
# elif(ch.isalpha()):
#     raise TypeError("enter a number")
# else:
#     print(ch)

# print(type(chr(65)))
import random
def rn():
    return chr(random.randint(97,122))
name=input("enter a name")
def code1(nameInput):
    if(len(name)<3):
       return nameInput[::-1]
    elif(len(nameInput)>=3):
        return rn()+rn()+rn()+nameInput[1:len(nameInput)]+nameInput[0]+rn()+rn()+rn()
# print(code1(name))

def decode1(codeName):
    if(len(name)<3):
       return codeName[::-1]
    elif(len(codeName)>=3):
        name1=codeName[3:-3]
        original_name=name1[-1]+name1[0:-1]
        return original_name
    
print(decode1("pqtarryhsky"))

    



