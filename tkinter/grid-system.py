from tkinter import *

root = Tk()

#creating a label widget
label1 = Label(root,text="Hello World")
label2 = Label(root,text="Hey I am CuriousInvention")

#Where to position
label1.grid(row=0,column=0)
label2.grid(row=1,column=0)

root.mainloop()
