#Electricity bill calculator
#Author: Kamaljeet Kaur
#version: Python 3.9.9

units = int(input("enter no. of units consumed"))

#if units consumed is less than 100 then price per unit is:
if(units <= 100):
    bill = 5.95*units
    print(f"bill for consumed unit {units} is: {bill}")

#if units consumed is less than 100 then price per unit is:
elif(units > 100):
    bill = 6.95*(units-100) + 100*(5.95)
    print(f"bill for consumed unit {units} is: {bill}")
else:
    print("please enter valid unit")

