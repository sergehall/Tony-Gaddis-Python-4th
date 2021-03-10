# recursive list sum

# 5. Рекурсивная сумма списка. Разработайте функцию, которая принимает
# список чисел в качестве аргумента. Она должна рекурсивно вычислить сумму
# всех чисел в списке и вернуть это значение.


def main():
    my_list = [1, 2, 3, 4, 5, 6]
    print("my_list :", my_list)
    print("Summa numbers of list: ", sum_n(my_list))


def sum_n(n):
    if len(n) <= 1:
        print(n[0], n)
        return n[0]
    else:
        m = sum_n(n[1:])
        print(m + n[0], n[:])
        return m + n[0]


main()