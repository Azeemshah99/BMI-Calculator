class BMICal:

    #Weight(kg) and Height(m)
    name = ""
    weight = ""
    height = ""

    def __init__(self,name,weight,height):
        self.name = name
        self.weight = float(weight)
        self.height = float(height)
    
    def Cal(self):
        self.BMI = self.weight/(self.height*self.height)
        return "{:2f}".format(self.BMI)
    
    def checkbmi(self,bmi):
        bmi = float(bmi)
        if bmi<18.5:
            return f"You are Underweight, please eat more {self.name}!!!"
        elif bmi <= 24.9:
            return f"You are Normal weight, Goodjob {self.name}!!!"
        elif bmi < 29.9:
            return f"You are Overweight, please do some exercise {self.name}"
        elif bmi < 34.9:
            return f"You are Obese, please eat healthy and exercise. You can do this {self.name}!"
        else: return f"You are Severely Obese, please seek help from profesional"


    def message(self,bmi,check):
        return f"""
    {self.name} with the weight of {self.weight}kg and height of {self.height}m
    your BMI are {float(bmi)}, {check}"""
        
