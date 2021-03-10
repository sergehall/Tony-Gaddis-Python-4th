# largest file item

# 4. Максимальное значение в списке. Разработайте функцию, которая
# принимает список в качестве аргумента и возвращает самое большое значение в
# списке. В данной функции для нахождения максимального значения должна
# использоваться рекурсия.

def main():
    my_list = [79, 4, 6, 768, 9, 5, 90]
    print("my_list :", my_list)
    print()
    print("The largest number is: ", max_n(my_list))


def max_n(n):
    if len(n) <= 1:
        return n[0]
    else:
        print(n[1:])
        m = max_n(n[1:])
        return m if m > n[0] else n[0]


main()