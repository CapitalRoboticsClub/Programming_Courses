from Check_Prime_Module import *

def main():

    # To take input from the user
    #num = int(input("Enter a number: "))
    num = 2836

    if prime_checker(num):
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


    print(find_all_factors(num))

if __name__ == "__main__":
    main()

    
