from tkinter import *
from PIL import Image, ImageTk
import os
root=Tk()
root.title(f"Building GUI with Harshita {os.getcwd()}")
# setting height and width of window
root.minsize(200,200)
# root.maxsize(600,600)
root.geometry("1000x1000")

# Adding text, but has to be packed
Label(text="hello Harshita").pack()
'''
photo = PhotoImage(file="pythoned.png")
# photo = PhotoImage(file="images.jpeg")  # error as jpeg images are not supported
Label(image=photo).pack'''

# for jpeg images
img=Image.open(r"C:\Users\91912\Desktop\TUTORIAL\python_class-6\i1.jpg")
phtr=img.resize((300,300))
pht=ImageTk.PhotoImage(phtr)

Label(image=pht, width=200, height=200).pack(anchor="nw", side="right",fill=X)
Label(image=pht, width=200, height=200).pack(anchor='ne', side="left",fill=X)

Label(text='''A class is a user-defined blueprint or prototype from whi
      ch objects are created.  user-defined data structure, which holds its own data 
       and member functions, which can be accessed and used by creating an instance 
        that class. A class is like a blueprint for an object''', 
        cursor="hand2",takefocus=True,wraplength=700,anchor="center",
        bg="grey", padx=30, pady=30, font=("Helvetica", 15, "bold"), borderwidth=5, relief=RIDGE).pack(fill=X)

Label(text="lorem1nifn fnifn fneioc  fenfe oejfe nfenf vnifwnff fefjoA class is a user-defined blueprint or prototype from which objects are created.  user-defined data structure, which holds its own data and member functions, which can be accessed and used by creating an instance that class. A class is like a blueprint for an object 2",  wraplength=300,borderwidth=5, relief=RIDGE,bg="grey", anchor="ne").pack(fill=X)
# Label(image=pht, width=200, height=200, state="disabled").pack()


root.mainloop()