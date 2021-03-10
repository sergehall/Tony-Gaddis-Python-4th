# recursive printing

# 1. Рекурсивная печать. Разработайте рекурсивную функцию, которая принимает
# целочисленный аргумент п и распечатывает числа от 1 до п.

def main():
    print("This program displays the numbers from\n"
          "1 up through the 'n' that you stated")
    print()
    n = int(input("Please enter an integer: "))
    n_print(n)


def n_print(n):
    if n == 0:
        return
    else:
        n_print(n - 1)
        print(n)


main()
