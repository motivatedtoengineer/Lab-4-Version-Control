# Zeyad Khalil, Andrew Pineda, David Ledesma, Eduardo Nungaray, Christian Perez
# Group: CEO
# Lab 4 Version Control Master File



#   Problem A - David Ledesma

word = input("Input a word to reverse: ")
for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")





#   Problem B - Zeyad Khalil

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:22:18 2020

@author: Shaba
"""

# Program to check if a number is prime or not

num = 407

# To take input from the user
#num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")





#   Problem C - Eduardo Nungaray

# -*- coding: utf-8 -*-
import time
Time = time.localtime()
print(time.asctime(Time))





#   Problem D - Christian Perez

# The code for the fibonacci sequence of a user input number 

a = 0 
b = 1 

x = int(input("Please enter a number: "))

while a <= x:
    print(a) 
    a,b = b, a + b
    





#   Problem E - Andrew Pineda
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

