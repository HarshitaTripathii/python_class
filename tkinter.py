from tkinter import *
root=Tk()
# setting height and width of window
root.minsize(200,200)
root.maxsize(600,600)
root.geometry("400x400")

# Adding text, but has to be packed
Label(text="hello Harshita").pack()

root.mainloop()