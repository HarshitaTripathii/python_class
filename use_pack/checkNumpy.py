from my_pack import class1
# a=class1.add(9,1)
# print(a)

# name="harshita"
# count=0
# rname=name[::-1]
# if(name==rname):
#     print("palindrome")
# else:
#     print(" not palindrome")
# for i in name:
#     if (i.lower() in "aeiou"):
#         count=count+1
# print(count)

import numpy as np
# print(np.__version__)  # This will print the installed version of numpy
l=[7,5,78,34]
l1=[[7,5],[78,34],[3,4]]
arr=np.array(l)
arr1=np.array(l1)
# arr1=np.array(l1,dtype=float)
# print(arr1)

# arr1=np.array(l1)
# arr_1=arr1.astype(int).astype(str)
# print(arr1)
# print(arr_1)

# print(type(arr))
# print(arr1)
# print(arr+2)
# print(arr1+2)
# print(l+2)

# print(arr1.ndim)
# print(arr)   # 2-D,3-D...
# print(arr.ndim)   # 2-D,3-D...
# print(arr1.size
# print(arr1.shape)  #(row,column)  #returns tuple
# print(arr.shape)  #(row,column)  #returns tuple
# print(arr1.dtype))
# print(arr.size)
# print(arr1[:2,::-1])

#zeros
np1=np.zeros(5)
# print(type(np1[1]))
# print(np1) # all 0s are float
# print(np1.shape) # all 0s are float
# print(np1.size) # all 0s are float

#Multidimentional zeros
# np11=np.zeros((2,10))
# np11=np.zeros((3,10))

#example with normal array
l2=[0.,0.,0.,0.,0.]
l2a=np.array(l2)
# print(l2a)
# print(l2a.shape)
# print(l2a.size)

np11=np.zeros((3,5))
# print(np11)
# print(np11.shape)
# print(np11.size)

#full
# np2=np.full((size),element)

np2=np.full((5),6)
# print(np2)

#Mulltidimentional 
np22=np.full((3,5),10)
# print(np22)

#arange(size , stating from 0)  
np3=np.arange(5)
# print(np3)  #[0 1 2 3 4]

np33=np.arange(20,10,-2)
# print(np33)

#slicing in "normal array" is similar to slicing in list in py

list1=[[2,3,4,5,6,7],[8,9,10,11,12,13]]
list1p=np.array(list1)
#slicing 1:
# print(list1p[1,2])  # 1=1st row  2= element at index 2 in "1st row"  output:10  fetching 1 element so return number

#slicing 2:
# print(list1p[1:2,2:3]) #1:2 = 2nd row 2:3= elemnt at index 2 in "2nd row" slicing so return array
# negative slicing not working

#slicing 3:
# want elements from all rows 
# print(list1p[:,2:4]) # : means all rows i.e [:] and 2:4 means element at index 2,3  return array

#NUMPY UNIVERSAL FUNCTION
'''
ls=[2,4,0,9,36,-1,78,-78]
lsn=np.array(ls)
# print(np.sqrt(lsn))   #return array and float type || run after removing -ve no.
print(np.sign(ls))  #[ 1  1  0  1  1 -1  1 -1]
print(np.max(ls))
print(np.min(ls))
'''

'''# array.copy()
# it will create a copy and no linkage/connection
# change in one will not effect other
l4=np.array([10,20,30,40])
l4_1=l4.coy()p
print(f"original is {l4}")
print(f"copied is {l4_1}")

l4[0]=99
print(f"original is {l4}")
print(f"copied is {l4_1}")

l4_1[2]=88
print(f"original is {l4}")
print(f"copied is {l4_1}")'''

'''# array.view()
# it will create a copy and  linkage/connection also
# change in one will effect other
l4=np.array([10,20,30,40])
l4_1=l4.view()
print(f"original is {l4}")
print(f"copied is {l4_1}")

l4[0]=99
print(f"original is {l4}")
print(f"copied is {l4_1}")

l4_1[2]=88
print(f"original is {l4}")
print(f"copied is {l4_1}")'''

'''# reshape(desired row, desired column)
#  remember : row * coln == no. of elements
l5=np.array([10,20,30,40,50,60,70,80,90,100,110,120])
print(l5.reshape(6,2))
l6=l5.reshape(2,6)

# flatten to 1-D array : use -1 as parameter
print(l6.reshape(-1))'''

# iteration
l5=np.array([10,20,30,40,50,60,70,80,90,100,110,120])
l6=l5.reshape(2,6)
l7=l5.reshape(3,2,2)

'''for x1 in l5:
    print(x1)

for x2 in l6:
    for x2_2 in x2:
        print(x2_2)

for x3 in l7:
    for x3_3 in x3:
        for x3_3_3 in x3_3:
            print(x3_3_3)'''

'''#instead of using this nested loop depending upon the dimensions use np.nditer(array_name)
for i in np.nditer(l7):
    print(i)'''

'''#  SORTING : np.sort(array_name)  // returns a copy, do not change the original one
l8=(np.array([1,4,9,6,3,5,7,9,3,2,4,9,3,1,45,-1])).reshape(4,2,2)
print(f"original array is {l8}")
l8s=np.sort(l8)
print(f"sorted array is {l8s}")
print(f"original array is {l8}")
l9=np.sort((np.array([60,-2,48,2,55])))
print(l9)'''

l6=np.array([10,20,4,10,44,57,10,3,23,10])
l6_=np.where(l6==10)  #returns a tuple
print(l6)
print(l6_[0])
print(l6[l6_[0]])










import pandas as pd
ns=pd.Series([2,4,5,61,2])
# print(ns)






