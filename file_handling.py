# writing rt/wt/at means dealing with text files
# writing rb/wb/ab means dealing with binary files binary files include images, pdfs etc.

# here closing file is imp otherwise, sometimes, code will not run.
# f=open("text.txt", 'w')
# f.write("ARYA HELLO\n")
# f=open("text.txt",'r')
# # content=f.read()
# # print(content)
# f.close()
# f=open("text.txt", "w")
# f.write("today is monday, i want to spend it more")
f=open("text.txt", 'r')
content=f.read()
print(content)

# use "with - as" keywords to avoid closing as it automatically closes the file.
# with open("text1.txt", 'a') as f:
#     f.write("hello guys") 