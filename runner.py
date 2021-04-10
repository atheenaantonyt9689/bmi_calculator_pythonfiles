#from bmi import *
#height=int(input("enter height in meters:"))
#weight=int(input("enter weight in kilogram"))
from bmi import BmiCalculator
def run():
    height =input("enter height in ms: ")
    try:
        height=float(height)
    except ValueError:
        print("Enter valid number Exsisting !")
        exit(1)
    weight=input("enter weight in kgs: ")
    try:
        weight=float(weight)
    except ValueError:
        print("enter a valid number Exsisting:")
        exit(1)
    b=BmiCalculator()
    bmi=b.bmi(height,weight)
    bmi_category=b.bmi_description(bmi)
    print("")
    print(f"Your BMI is :{bmi} ({bmi_category})")
run()





