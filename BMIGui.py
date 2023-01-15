import BMICalculate as bm
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #Label
        self.title("BMI Calculator")
        self.geometry("450x200")
        self.blanks = ttk.Label(self,width=35)
        self.blanks.grid(row=0,column=1)
        self.name = ttk.Label(self,text = "Your Name:   ")
        self.name.grid(row=1,column=1)
        self.weight = ttk.Label(self,text = "Your Weight:   ")
        self.weight.grid(row=2,column=1)
        self.height = ttk.Label(self,text = "Your Height:   ")
        self.height.grid(row=3,column=1)

        #Entry Variable
        self.name_var = tk.StringVar()
        self.weight_var = tk.StringVar()
        self.height_var = tk.StringVar()

        #Entry
        self.Ename = ttk.Entry(self,textvariable=self.name_var)
        self.Ename.grid(row=1,column=2,pady=5)
        self.Eweight = ttk.Entry(self,textvariable=self.weight_var)
        self.Eweight.grid(row=2,column=2,pady=5)
        self.Eheight = ttk.Entry(self,textvariable=self.height_var)
        self.Eheight.grid(row=3,column=2,pady=5)

        self.button = ttk.Button(self, text='Calculate BMI'
                        ,command=lambda:test(self,test2(self)))
        # self.button['command'] = 
        self.button.grid(row=4,column=2)

        def test2(self):
            self.BMI = bm.BMICal(self.name_var.get(),self.weight_var.get(),self.height_var.get())
            return self.BMI.message(self.BMI.Cal(),self.BMI.checkbmi(self.BMI.Cal()))

        def test(self,x):
            ttk.Label(self,text=x).grid(row=5,column=1,columnspan=3)

if __name__ == "__main__":
    app = App()
    app.mainloop()
# BMI = bm.BMICal("Azeem",60,1.7)
# print(BMI.message(BMI.Cal(),BMI.checkbmi(BMI.Cal())))