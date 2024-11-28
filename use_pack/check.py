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
print(np.__version__)  # This will print the installed version of numpy
# l=[7,5,78,34]
l1=[[7,5],[78,34],[3,4]]
# arr=np.array(l)
arr1=np.array(l1,dtype=float)
print(arr1)

# arr1=np.array(l1)
# arr_1=arr1.astype(int).astype(str)
# print(arr1)
# print(arr_1)

# print(type(arr))
# print(arr1)
# print(arr+2)
# print(arr1+2)
# print(l+2)

# print(arr1.size)
# print(arr1.ndim)   # 2-D,3-D...
# print(arr1.shape)  #(row,column)
# print(arr1.dtype)
print(arr1[:2,::-1])

import pandas as pd
ns=pd.Series([2,4,5,61,2])
print(ns)






