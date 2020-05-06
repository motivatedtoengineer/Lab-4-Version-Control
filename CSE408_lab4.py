# The code for the fibonacci sequence of a user input number 

a = 0 
b = 1 

x = int(input("Please enter a number: "))

while a <= x:
    print(a) 
    a,b = b, a + b
    
