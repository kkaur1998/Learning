"""

Q2. Create a program for a grocery calculator. It will take in key-value pairs for items and their prices, and return the 
subtotal and total, and can print out the list for you for when you're ready to take it."""


items_dict = {}
lenght = int(input('enter the number of items: '))
for i in range(lenght):
    item, price = input("enter item and price respectively: ").split()
    items_dict[item] = float(price)

print(items_dict)
total = 0
for i in items_dict.keys():
    total+=items_dict[i]
    
print("items bought are: ", list(items_dict.items()))
print("total bill: ", total)

