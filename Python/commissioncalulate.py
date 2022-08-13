sold_items = input("enter the units sold by employee")
if(sold_items.isdigit()):
    solid_items = int(sold_items)
    if(sold_item < 200):
        comission = 5*sold_items
    elif(sold_items >= 200):
        comission = 5*200 + (sold_items-200)*10
    print(f"The comission earned by employee: {comission}")
else:
    sold_items = int(input("please enter valid input: "))
