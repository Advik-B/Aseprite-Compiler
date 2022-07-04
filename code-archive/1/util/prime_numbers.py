from math import sqrt

# if we found any facto then we can print as not a prime number


def is_prime(n: int):
    if n <= 1:
        return False
    prime_flag = next((1 for i in range(2, int(sqrt(n)) + 1) if n % i == 0), 0)
    return prime_flag == 0
