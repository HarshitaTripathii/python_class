# print("hello")
# a=int(input("enter a no."))
# b=int(input("enter a no."))
# print(a+b)
# import keyword
# print(keyword.kwlist)
# print(type(keyword.kwlist))
# print(len(keyword.kwlist))


# p=int(input("enter your %"))
# if (p>=90):
#     print("Grade A")
# elif (p>=80):
#     print("Grade B")
# elif (p>=70):
#     print("Grade C")
# elif (p>=60):
#     print("Grade D")
# else:
#     print("fail")


# n=int(input("enter number"))
# sum =0
# while(n!=0):
#     r=n%10
#     sum=sum+r
#     n=n//10
# print(sum)

# count=0
# while(count<5):
#     print(count, "is leass than 5")
#     count =count+1
# else:
#     print(count, "is not less than 5")

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def flower(n,t,arr):
    i=0
    j=n-1
    lst=[]
    while(i<j):
        if(arr[i]+arr[j]==t):
            return (i,j)
        elif(arr[i]+arr[j]>t):
            j=j-1
        else:
            i=i+1
    return None
        
a=[1,1,2,3,4]
ans=flower(5,2,a)
print(ans)



