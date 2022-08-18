mylist = input("enter list elements").split()
print(mylist)
count_list = []
for i in mylist:
    if(i not in count_list):
        print(f"count of {i}:", mylist.count(i))
        count_list.append(i)
