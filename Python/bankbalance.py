n = int(input())
for i in range(n):
    withdraw_amount, balance = input().split()
    if(withdraw_amount.isdigit() and balance.isdigit()):
        withdraw_amount= int(withdraw_amount)
        balance = int(balance)
        if(balance >= (withdraw_amount+0.5)):
            if(withdraw_amount % 5) == 0:
                    balance = balance - (withdraw_amount + 0.5)
            else:
                print(balance)
            print(balance)
        else:
           print("you don't have sufficient balance")
    else:
        withdraw_amount, balance = input("please enter valid withdraw amount and bank balance).split()
