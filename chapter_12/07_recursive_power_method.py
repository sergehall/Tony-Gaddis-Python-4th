# recursive power method

#  7. Рекурсивный метод возведения в степень. Разработайте функцию, в
#  которой рекурсия применяется для возведения числа в степень. Данная
#  функция должна принимать два аргумента: число, которое будет возведено в
#  степень, и показатель степени. Исходите из того, что показатель степени
#  является неотрицательным целым числом.

def main():
    num = int(input("Please enter a number that can be raised to a power:\n"))
    power = int(input("Please enter the value power to exponentiate:\n"))
    print("The number ", num, " to the power of ", power, " is ",
          sum_n(num, power), ".", sep="")


def sum_n(n, my_pow):
    if my_pow <= 0:
        return 1
    return n * sum_n(n, my_pow - 1)


main()
