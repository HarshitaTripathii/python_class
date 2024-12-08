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

'''photo = PhotoImage(file="pythoned.png")
# photo = PhotoImage(file="images.jpeg")  # error as jpeg images are not supported
Label(image=photo).pack()'''

# for jpeg images
img=Image.open("images.jpeg")
pht=ImageTk.PhotoImage(img)
Label(image=pht).pack()
Label(text='''A class is a user-defined blueprint or prototype from whi
      ch objects are created. Classes provide a means of bundling 
      data and functionality together. Creating a new class creates a new 
        of object, allowing new instances of that type to be made. Each class 
          can have attributes attached to it to maintain its state. Class instances can 
          also have methods (defined by their class) for modifying their state.
         The class creates a user-defined data structure, which holds its own data 
       and member functions, which can be accessed and used by creating an instance 
        that class. A class is like a blueprint for an object''', bg="grey", padx=30, pady=30, font=("Helvetica", 15, "bold")).pack()

root.mainloop()