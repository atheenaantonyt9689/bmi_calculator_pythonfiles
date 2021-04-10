from test_bmi import *
height=int(input("enter height in meters:"))
weight=int(input("enter weight in kilograms:"))

obj=BmiCalculator(height,weight)
obj.bmi(height,weight)

