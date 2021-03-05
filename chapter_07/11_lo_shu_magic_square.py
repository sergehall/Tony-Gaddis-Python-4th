# lo shu magic square
# by default, there is a random substitution of numbers in the matrix
# with the specified diagonal. You can comment out a random option and
# open one of the examples of the magic square while setting its diagonal.

import random

diagonal = int(input('Enter the diagonal length of the magic square:\n'))


def main():
    # creat the matrix
    magic_square = [[random.randint(1, 100) for i in range(diagonal)] for j in
                    range(diagonal)]

    # пример магического квадрата 2х2
    # magic_square = [[2, 2], [2, 2]]

    # пример магического квадрата 3х3
    # magic_square = [[4, 9, 2],
    #                 [3, 5, 7],
    #                 [8, 1, 6]]

    # пример магического квадрата 4х4
    # magic_square = [[7, 12, 1, 14],
    #                 [2, 13, 8, 11],
    #                 [16, 3, 10, 5],
    #                 [9, 6, 15, 4]]

    # пример магического квадрата 8х8.
    # magic_square = [[8, 58, 59, 5, 4, 62, 63, 1],
    #                 [49, 15, 14, 52, 53, 11, 10, 56],
    #                 [41, 23, 22, 44, 45, 19, 18, 48],
    #                 [32, 34, 35, 29, 28, 38, 39, 25],
    #                 [40, 26, 27, 37, 36, 30, 31, 33],
    #                 [17, 47, 46, 20, 21, 43, 42, 24],
    #                 [9, 55, 54, 12, 13, 51, 50, 16],
    #                 [64, 2, 3, 61, 60, 6, 7, 57]]

    # checking the matrix
    checking_magic_square(magic_square)


# функция получает суммы столбцов, диагоналейб строк. Эти суммы вставляет
# в список for_comparison_list.
def checking_magic_square(magic_square_list):
    index = 0
    total_index_diagonal_general = 0
    total_index_diagonal_secondary = 0
    for_comparison_list = []

    # цикл для получения сум столбцов.
    for i in range(diagonal):
        s = 0
        for j in range(diagonal):
            s += magic_square_list[j][i]
        for_comparison_list.append(s)

    # цикл получения сумм строк, главной и всомогательной диагонали.
    while index < diagonal:
        r = sum(magic_square_list[index])
        total_index_diagonal_general += magic_square_list[index][index]
        total_index_diagonal_secondary += magic_square_list[index][
            ((diagonal - 1) - index)]
        for_comparison_list.append(r)
        index += 1
    for_comparison_list.append(total_index_diagonal_general)
    for_comparison_list.append(total_index_diagonal_secondary)

    print()
    print("The sum of the numbers of each diagonal.\n",
          for_comparison_list, sep="")
    print()

    for r in magic_square_list:
        print(r)
    print("----------------------")
    # проверка двумерного списка является ли он магическим.
    i = 0
    while i < len(for_comparison_list) - 1:
        if for_comparison_list[i] == for_comparison_list[i + 1]:
            i += 1
        else:
            print('Magic square is False!')
            break
        if i == len(for_comparison_list) - 1:
            print('Magic square is True!')
            return True


main()
