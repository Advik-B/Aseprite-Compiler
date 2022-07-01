from math import sqrt

# if we found any facto then we can print as not a prime number
def is_prime(n: int):
    # this flag maintains status whether the n is prime or not
    prime_flag = 0

    if n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                prime_flag = 1
                break
        if prime_flag == 0:
            return True
        else:
            return False
    else:
        return False
