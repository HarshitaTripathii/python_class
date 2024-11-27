from my_pack import class1
# a=class1.add(9,1)
# print(a)

name="harshita"
count=0
rname=name[::-1]
if(name==rname):
    print("palindrome")
else:
    print(" not palindrome")
for i in name:
    if (i.lower() in "aeiou"):
        count=count+1
print(count)





