# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*", end='')
#     print()
# for i in range(3,0,-1):
#     for j in range(1,i+1):
#         print("*", end ='')
#     print()

# for i in range(1,5):
#     for j in range(i,5):
#         print("*", end='')
#     print()

# for i in range(1,5):
#     for j in range(1,5):
#         if(j>=i):
#             print("*", end='')
#         else:
#             print(" ",end='')
#    print()
# n=6
# for i in range(1,7):
#     for j in range(i,7):
#         if(i==1):
#             print("*",end='')
#         else:
#             if (j>i and j<6):
#                 print(" ",end='')
#             else:
#                 print("*", end='')
#     print()

# n=6
# for i in range(1,6):
#     for j in range(1,(i+1)):
#         if(i==5):
#             print("*",end='')
#         else:
#             if (j>1 and j<i):
#                 print(" ",end='')
#             else:
#                 print("*", end='')
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==n or (i+j)==(n+1)):
#             print("*",end='')
#         elif(j!=1 and (i+j)!=2*i):
#             print(" ",end='')
#         else:
#             print("*", end='')
#     print()
n=int(input("enter number of rows"))
for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        if(i+j<=2*i):
            print("* ", end='')
        elif(i+j==(n+1)):
            print("* ", end='')
        else:
            print("  ",end='' )
    print()


        
    

