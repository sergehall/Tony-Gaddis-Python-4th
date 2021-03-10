# sum of numbers

# 6. Сумма чисел. Разработайте функцию, которая принимает целочисленный
# аргумент и возвращает сумму всех целых чисел от 1 до числа, переданного в
# качестве аргумента. Например, если в качестве аргумента передано 50,
# то данная функция вернет сумму чисел 1, 2, 3, 4, ... , 50. Для вычисления
# суммы примените рекурсию.

def main():
    num = int(input("Enter the amount of what number do you want to get?: "))
    print("The total of the numbers from 1 up to", num, "equals to", sum_n(num))


def sum_n(n):
    if n <= 0:
        return 0
    else:
        print(n)
        return n + sum_n(n - 1)


main()
