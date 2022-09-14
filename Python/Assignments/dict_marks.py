"""Q1. Suppose there is two different types of dictionary, one dictionary contains registration number and name of student and 
another dictionary contains registration number and marks. Take 5 student details. Now display the student's result in terms of 
grade from the following condition:
If marks between 90 to 100:grade'O'
marks between 80 to 90:grade'A+'
marks between 70 to 80:grade'A'
marks between 60 to 70:grade'B+'
marks between 50 to 60:grade'B'
Display result in the form of dictionary.
"""

dict1 = {}
dict2 = {}
n = int(input("enter number of studetns"))
for i in range(2):
    regno = input(f"enter regno of {i+1}th student")
    name = input(f"enter name of {i+1}th student")
    marks = int(input("enter marks of student"))
    dict1[regno] = name
    dict2[regno] = marks
print(dict1)
print(dict2)

for i in dict2.keys():
    comp = dict2[i]
    if(comp>=0 and comp<=100):
        if(comp > 90 and comp<=100):
            dict2[i] = 'O'
        elif(comp > 80 and comp<=90):
            dict2[i] = 'A+'
        elif(comp > 70 and comp<=80):
            dict2[i] = 'A'
        elif(comp > 60 and comp<=70):
            dict2[i] = 'B+'
        elif(comp > 50 and comp<=60):
            dict2[i] = 'B'
        else:
            print("marks can only be between 0 - 100")
    else:
        print("marks can be 0-100 only")
print(dict2)
