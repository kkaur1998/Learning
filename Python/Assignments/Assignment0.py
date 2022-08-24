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
# l1 = ["regno","name"]
# l2 = ["regno","marks"]
# dict1 = {}
# dict2 = {}
# dict1 = dict1.fromkeys(l1)
# dict2 = dict2.fromkeys(l2)
# dict1["regno"],dict1["name"] = input("enter regno and name of student").split()
# dict2["regno"] = dict1["regno"]
# dict2["marks"] = int(input("enter marks of student").split())

# for i in dict2.keys()


# dict1 = {"1":{"regno": 12345, "name": "kamal"},"2":{"regno": 23456, "name": "sandeep"},"3":{"regno": 34567, "name": "karam"},"4":{"regno": 45678, "name": "param"},"5":{"regno": 56789, "name": "Preet"}}
# dict2 = {{"regno": 12345, "marks": 80},{"regno": 23456, "marks":70},{"regno": 34567, "marks":65},{"regno": 45678, "marks":86},{"regno": 56789, "marks":95}}



dict1 = {}
dict2 = {}
for i in range(2):
    regno = input(f"enter regno of {i+1}th student")
    name = input(f"enter name of {i+1}th student")
    marks = int(input("enter marks of student"))
    dict1[regno] = {"regno": regno, "name": name}
    dict2[regno] = {"regno": regno, "marks": marks}
print(dict1)
print(dict2)

for i in dict2.keys():
    comp = dict2[i][marks]
    if(comp>=0 and comp<=100):
        if(comp > 90 and comp<=100):
            dict2[i]["grades"] = 'O'
        elif(comp > 80 and comp<=90):
            dict2[i]["grades"] = 'A+'
        elif(comp > 70 and comp<=80):
            dict2[i]["grades"] = 'A'
        elif(comp > 60 and comp<=70):
            dict2[i]["grades"] = 'B+'
        elif(comp > 50 and comp<=60):
            dict2[i]["grades"] = 'B'
        else:
            print("marks can only be between 0 - 100")
    else:
        print("marks can be 0-100 only")





# print(dict1)
# print(list(dict1.keys()))
# for i in dict1.keys():
#     print(i)












"""

Q2. Create a program for a grocery calculator. It will take in key-value pairs for items and their prices, and return the 
subtotal and total, and can print out the list for you for when you're ready to take it."""




"""
Q3. A website requires the users to input username and password to register. Take some sample password in a list and check which 
password will be valid for user.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of password: 6
5. Maximum length of password: 12
"""

# password_list = input().split()
# valid_count = 0
# for i in password_list:
#     if(len(i)>=6 and len(i)<=12):
#         valid_count += 1
#         for j in i:
#             if(j in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"): 
#                 valid_count += 1
#                 continue
#             elif(j in "abcdefghijklmnopqrstuvwxyz"):
#                 valid_count += 1
#                 continue
#             elif(j in "012456789" or j in "$#@"):
#                 valid_count +=1 
#                 continue
#             if(valid_count>=4):
                # break


        


"""
Q1. Suppose there is two different types of dictionary, one dictionary contains employee id and name of employee and another dictionary contains employee id and salary. Take 5 employee details. Now display the employee's designation from the following condition:
If salary between 80,000 to 90,000:designation:Project Manager
salary between 70,000 to 80,000:designation:Team Leader
salary between 60,000 to 70,000:designation:Software Developer
salary between 50,000 to 60,000:designation:Software Trainee
Display result in the form of dictionary."""




"""

Q2. Write a program that computes the net amount of a bank account based on a transaction. The transaction format is shown as following:
D 100
W 200
Here, D means deposit while W means withdrawal.
Take the following input in the form of dictionary:
D 300
D 300
W 200
D 100
{"D":300,"D":300,"W":200,"D":100}
Then, the output should be:
500

Q3. You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. Take inputs from user by a sequence of comma-separated. Then ask options for sort to follow the following criteria:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by height.

Q1. Suppose there is two different types of dictionary, one dictionary contains product id and product name and another dictionary contains product id and product price. Take 5 product details. Now display the product's actual price from the following condition:
If product price range between 5000 to 10000:GST Tax(10%)
product price range between 4000 to 5000:GST Tax(8%)
product price range between 3000 to 4000:GST Tax(7%)
product price range between 2000 to 3000:GST Tax(5%)
Display result in the form of dictionary.

Q2. Write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey", "Football"].

Q1. Suppose there is two different types of dictionary, one dictionary contains customer id and customer name and another dictionary contains customer id and balance amount. Take 5 customer details. Now calculate the customer's total balance amount from the following condition:
If balance amount is between 5000 to 10000:Interest(10%)
balance amount is between 4000 to 5000:Interest(8%)
balance amount is between 3000 to 4000:Interest(7%)
balance amount is between 2000 to 3000:Interest(5%)
Display result in the form of dictionary.
Note:-Interest will be added with balance amount

Q2. Suppose you want to purchase one mobile phone from mobile shop. Perform following operations with the help of List, tuple and dictionary:
a. Display List of Mobile phone with price
b. Calculate Price of according to total no. of mobile phone purchased by customer.
c. Display updated List of Mobile phone with price

Q3. Write a program to solve a question:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
Display output in the form of dictionary.
{"chickens": no. of chickens, "rabbits": no. of rabbits}

1. Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
2. Read n floating point numbers from a user and find their sum of squares and print the result upto 2 decimal places.
3. Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
4. Write a program that reads a 5-digit positive integer and returns the sum of cubes of all digits of that number.
5. Given a range of first 10 numbers, iterate from start number to the end number and print the sum of the current number and previous number during each iteration.
6. Given a string, display only those characters which are present at an even index number.
7. Given a two integer numbers return their product and if the product is greater than 1000, then return their sum.
8. Read n values and print only those numbers which are divisible by 7.
9. Reverse a given number and return true if it is the same as the original number.
10. Calculate income tax for the given income by adhering to the following rules:

For example, suppose that the taxable income is $45000. The income tax payable is:
$10000*0% + $10000*10% + $25000*20% = $6000.
11. Write a program to print the following pattern with * (asterisks):
* * * * * * * * *
* * * * * * *
* * * * *
* * *
*
* * *
* * * * *
* * * * * * *
* * * * * * * * *
12. Write a program to print the following pattern with * (asterisks):
* * * * *
* * * *
* * *
* *
*
* *
* * *
* * * *
* * * * *
13. Write a program to print the following pattern with digits:
1
2 3
4 5 6
7 8 9 1
2 3 4 5 6


"""