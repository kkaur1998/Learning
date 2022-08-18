#Program to calculate sum of list
#Author: Kamaljeet Kaur
#Python Version: 3.9.9

mylist = []
sum = 0
length = input("enter number of elements in list")

#validating the value passed by user
if(length.isdigit()!=True):
    length = input("please enter integer as length of list")
else:
    for i in range(int(length)):
        value = input("enter the element")
        if(value.isdigit()):
            mylist.append(int(value))
            sum += int(value)
        else:
            print(value + "is not a valid value to add")
            continue

    

print(mylist)
print("sum of list elements is: ",sum)
    
