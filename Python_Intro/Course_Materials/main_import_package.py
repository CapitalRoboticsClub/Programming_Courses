from package_demo import check_prime_module, hello_module

def main():

    # To take input from the user
    #num = int(input("Enter a number: "))
    num = 2836

    if check_prime_module.prime_checker(num):
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


    print(check_prime_module.find_all_factors(num))

    hello_module.say_hello()

if __name__ == "__main__":
    main()

    
