from tkinter import *
from PIL import Image , ImageTk
import os

root=Tk()
root.title(f" Welcome to {os.getcwd()}")


f1=Frame(root, bg='grey', borderwidth=6, relief=RIDGE)
f1.pack(side=LEFT, fill=Y)

f2=Frame(root, bg='grey', borderwidth=6, relief=RIDGE)
f2.pack(side=TOP, fill=X)

# f3=Frame(root, bg='grey', borderwidth=6, relief=RIDGE)
# f3.pack( fill=BOTH)

Label(f1, text="Project PyCharm").pack()
b1=Button(f1, bg="Black", fg="white", text="Press")
b1.pack()
Label(f2, text="Welcome All !").pack()
# Label(f3).pack()
root.mainloop()