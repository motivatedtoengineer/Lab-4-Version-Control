# Andrew Pineda
# 5/5/2020
# Lab 4 - Problem E
# This program is intended to check passwords to make sure they meet a criteria.

# This specific criteria would be the password must have 7 characters, and 
# out of those 7, at least one character must be a number 0-9 and at least one 
# character must be a special character.

import re

x = input("Please enter your password: ")
y = True

while y:
    if (len(x) < 7):
        break
    elif not re.search("[0-9]", x):
        print("Password does not meet the conditions, missing a number.")
        break
    elif not re.search("[~!@#$%^&*()_+=,<>?/';:]", x):
        print("Password does not meet the conditions, missing a special character.")
        break
    else:
        print("Password Accepted.")
        y = False
        break

if y:
    print("Password not accepted.")