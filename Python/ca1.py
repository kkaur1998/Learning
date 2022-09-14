personal_details= {'1234': {"name":"kamal","age":24}, '2345': {"name":"Bubby","age":23}, '3456': {"name":"Param","age":20}, '4567': {"name":"Sandeep","age":22}}
professional_details= {'1234': {"designation":"manager","salary":90000}, '2345': {"designation":"lead","salary":80000}, '3456': {"designation":"associate","salary":24000}, '4567': {"designation":"operator","salary":30000}}
leave_balance = {'1234': 12, '2345': 10, '3456': 3, '4567': 2}
leaves_taken = {'1234': 5, '2345': 7, '3456': 3, '4567': 2}
net_salary = {}
for id in personal_details.keys():
    bonus = 0
    salary = professional_details[id]['salary']
    if(leaves_taken[id] <= leave_balance[id]):
        if(salary>5000):
            bonus = (15/100)*salary
            net_salary[id] = bonus+salary
        elif(salary>=4000 and salary<50000):
            bonus = (10/100)*salary
            net_salary[id] = bonus+salary
        elif(salary>= 50000):
            bonus = salary *0.05
            net_salary[id] = bonus+salary
    else:
        net_salary[id]= salary

    leave_balance[id] -= leaves_taken[id]


print("Net salary of employees: ", net_salary)
