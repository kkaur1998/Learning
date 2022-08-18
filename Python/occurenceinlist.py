#Program to calculate occurence of each element of list
#Author: Kamaljeet Kaur
#Python Version: 3.9.9

count_list = []
mylist = []
sum = 0
length = input("enter number of elements in list")

#validating the value passed by user
if(length.isdigit()!=True):
    length = input("please enter integer as length of list")
else:
    for i in range(int(length)):
        value = input("enter the element")
        mylist.append(value)
    for i in mylist:
        if(i not in count_list):
            print(f"count of {i}:" , mylist.count(i))
            count_list.append(i)
    
        
