# Program to check if a number is prime or not
import time
start_time = time.time()

def Prime(num):
    flag = True

    # prime numbers are greater than 1
    if num > 1:
       # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               flag = False 
               break
    return flag


# To take input from the user
#num = int(input("Enter a number: "))
num = 28374677

if Prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

print("My program took", time.time() - start_time, "seconds to run")

    
