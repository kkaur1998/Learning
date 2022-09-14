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

password_list = input().split()
valid_count = 0
for i in password_list:
    if(len(i)>=6 and len(i)<=12):
        # valid_count += 1
        for j in i:
            if(j in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"): 
                # valid_count += 1
                continue
            elif(j in "abcdefghijklmnopqrstuvwxyz"):
                # valid_count += 1
                continue
            elif(j in "012456789" or j in "$#@"):
                # valid_count +=1 
                continue
            # if(valid_count>=4):
            #     break

