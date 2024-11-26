# # writing rt/wt/at means dealing with text files
# # writing rb/wb/ab means dealing with binary files binary files include images, pdfs etc.

# # here closing file is imp otherwise, sometimes, code will not run.
# f=open("text.txt", 'w')
# f.write("ARYA HELLO\n")
# f=open("text.txt",'r')
# # content=f.read()
# # print(content)
# f.close()

# f=open("text.txt", "w")
# f.write("today is monday, i want to spend it more")
# f=open("text.txt", 'r')
# content=f.read()
# print(content)
# f=open("text.txt", 'a')
# f.write("\nand this is another line")
# f.close()


# # use "with - as" keywords to avoid closing as it automatically closes the file.
# with open("text1.txt", 'a') as f:
#     f.write("hello guys") 

# # readline()
# i=0
# f=open("text1.txt", 'r')
# while True:
#     line=f.readline()
#     if not line:
#         break
#     i=i+1
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     print(f"the marks of stu {i} in maths is {m1} and Eng is {m2}")

# # next line character is also counted in bytes to be printed
# f=open("text1.txt", 'r')
# content=f.read(5)
# print(content)
# content1=f.read(4)
# print(content1)

# # cursor is moving after every function call
# f=open("text1.txt", 'r')
# line=f.readline()
# lineL=f.readlines()
# print(lineL)
# print(line)

# f=open("text1.txt", 'w')
# addl=["hello yashi\n", "arya hello","\nsoni hello"," hello everyone"]
# f.writelines(addl)

# # seek() is used to move the cursor from current position to given position as argument.
# f=open("text1.txt",'a+')
# f.seek(10)
# print(f.tell())
# print(f.read(5))
# print(f.readline())
# # tell() is used to tell the current position of the cursor.

# # truncate(size_of_file) fxn is used to specify the size of the file.

# f=open("text1.txt",'w')
# f.write("hello world, my name is harshita, i am doing python full")
# f.truncate(10)

# f=open("text1.txt",'w')
# f.truncate(10)
# f.write("hello world, my name is harshita, i am doing python full")

# # lamda arguments : expression
# num=lambda a,b : 10*a+5*b
# print(num(10,2))
# print(num(b=10,a=2))

# notify=lambda x,name : print(f"username is {name} and age is {x}")
# notify("harshita", 21)
# print(notify("harshita", 21))

f=open("check.txt", 'w+')
line=["i love java", "java is my love", "all love java"]
f.writelines(line)
content=f.read()
print(content)
f.close()


