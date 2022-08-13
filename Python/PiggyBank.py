#A pigginbank with 10,5,2,1 rs coins --- calculate total amount



ten_coins = input("enter no. of coins of 10 Rs.")
if ten_coins.isnumeric != True:
    ten_coins = int(input("please enter valid no. of coins of 10 Rs"))

five_coins = input("enter no. of coins of 5 Rs.")
if five_coins.isnumeric != True:
    five_coins = int(input("please enter valid no. of coins of 5 Rs"))

two_coins = input("enter no. of coins of 2 Rs.")
if five_coins.isnumeric != True:
    two_coins = int(input("please enter valid no. of coins of 2 Rs"))

one_coins = input("enter no. of coins of 1 Rs.")
if one_coins.isnumeric != True:
    one_coins = int(input("please enter valid no. of coins of 1rs"))

#calculation of total_sum
total_sum = 10*(int(ten_coins)) + 5*(int(five_coins)) + 2*(int(two_coins)) + int(one_coins)
print("total sum is: ",total_sum)


