class BmiCalculator:
    def __init__(self,height,weight):
        self.height=height
        self.weight=weight
       # self.bmi=0.00
        

    def bmi(self):  
        bmi=self.height/self.weight**2
        return bmi

    def bmi_description(self,bmi_value):
        
        print("bmi from function",bmi_value)
        if bmi_value < 18.00:
            return "UnderWeight"
        elif bmi_value>=18.5 and bmi_value<=24.9:
            return "Normal Weight"
        elif bmi_value>=25 and bmi_value<=29.9:
            return "Over Weight "
        else:
            return "Obsesity- BMI of 30 or greater"
                   
obj =BmiCalculator(33,34)
bmi_value=obj.bmi(height,weight)
obj.bmi_description(bmi_value)

print("BMI OUTPUT:",bmi_value)
