from tkinter import Tk,Radiobutton, Button, Label, StringVar,IntVar,Entry

class TipCalculator():
    def __init__(self):
        window = Tk()
        window.title("Tip Calculator")
        window.configure(background="sky blue")
        window.geometry("375x250")
        window.resizable(width=False, height=False)

        ##
        self.meal_cost = StringVar()
        self.tip_percent = IntVar()
        self.tip = StringVar()
        self.total_cost = StringVar()

        ##
        tip_percent = Label(window,text="Tip Percentage", bg="purple",fg="white")
        tip_percent.grid(column=0,row=0,padx=15)

        bill_amount = Label(window,text="Bill Ammount", bg="black",fg="white")
        bill_amount.grid(column=1,row=0,padx=15)

        bill_amount_entry = Entry(window,textvariable=self.meal_cost,width=14,fg="white")
        bill_amount.grid(column=2,row=0)

        ##
        window.mainloop()


TipCalculator()
