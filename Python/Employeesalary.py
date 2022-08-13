#Calculation of Employee Salary
#Author: Kamaljeet Kaur
#Python Version: 3.9.9

salary = input("enter salary of employee")
while(salary.isnumeric == False):
    salary = input("please enter valid salary")
    

#if salary is below 20000
if(salary <= 20000):
    bonus = 0.15*salary 
    total_salary = salary + bonus

elif(salary <= 50000):
    bonus = 0.10*salary 
    total_salary = salary + bonus

elif(salary > 50000):
    bonus = 0.10*salary 
    total_salary = salary + bonus
    
total_salary = salary + (bonus/100) * salary
print(f"total salary of employee is : {total_salary}")
