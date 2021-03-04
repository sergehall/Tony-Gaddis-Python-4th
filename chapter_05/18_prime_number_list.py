# 19. Список простых чисел. Это упражнение предполагает, что вы уже
# написали функцию is pr_ime в задаче выше. Напишите еще одну программу,
# которая показывает все простые числа от 1 до 100. Программа должна иметь
# цикл, который вызывает функцию is prime.

def main():
    num = int(input('Entered prime number: '))
    print("The prime numbers from 1 to", num, "are listed below.")
    is_prime_list(num)


def is_prime_list(num):
    print("Prime number: ", sep="", end="")
    for i in range(2, num + 1):
        if is_prime(i):
            print(i, end="")

        if is_prime(i) and i != num:
            print(", ", end="")


def is_prime(num):
    for i in range(2, num + 1):
        for j in range(2, i):
            if num % j == 0:
                # если делитель найден, число не простое.
                return False
    return True


main()
