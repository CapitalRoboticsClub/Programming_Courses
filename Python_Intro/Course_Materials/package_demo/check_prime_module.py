def prime_checker(num):
    flag = True
    # prime numbers are greater than 1
    if num > 1:
       # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               flag = False 
               break
    return flag

def find_all_factors(num):
    factors = []
    if num > 1:
       # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               factors.append(i)
    return factors




    
