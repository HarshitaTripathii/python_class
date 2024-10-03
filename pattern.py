# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*", end='')
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
n=6
for i in range(1,7):
    for j in range(i,7):
        if(i==1):
            print("*",end='')
        else:
            if (j>i and j<6):
                print(" ",end='')
            else:
                print("*", end='')
    print()


        
    

