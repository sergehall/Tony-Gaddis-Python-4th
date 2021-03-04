# prime numbers

def main():
    number = int(input("Please enter a number to check if "
                       "it is prime or not:\n"))

    if is_prime(number):
        print("Your number", number, "is a prime number.")
    else:
        print("Your number", number, "is NOT a prime number.")


def is_prime(num):
    for i in range(2, num + 1):
        for j in range(2, i):
            if num % j == 0:
                # если делитель найден, число не простое.
                return False
    return True


main()
