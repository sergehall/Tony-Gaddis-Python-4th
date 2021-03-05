# 5. Напишите функцию, которая принимает список в качестве аргумента
# (допустим, что список содержит целые числа) и возвращает сумму значений в
# списке.

def main():
    x_list = [9, 4, 5, 4, 78]

    print(sum_list(x_list))


def sum_list(list_sum):
    total_sum = 0
    for i in list_sum:
        total_sum += int(i)
    return total_sum


main()
