# 6. Среднее количество слов. Среди исходного кода главы 8, а также в
# подпапке data "Решений задач по программированию" соответствующей главы вы
# найдете файл text.txt. В нем в каждой строке хранится одно предложение.
# Напишите программу, которая читает содержимое файла и вычисляет среднее
# количество слов в расчете на предложение.

def main():
    # файл не найден , создал его сам
    open_file = open('text.txt', 'w')
    line1 = open_file.write('The Declaration of Independence states the '
                            'principles on which our government\n, and our '
                            'identity as Americans, are based.')
    line2 = open_file.write('Unlike the other founding documents,\n'
                            'the Declaration of Independence is not legally '
                            'binding, butit is powerful.\n')
    line3 = open_file.write('Abraham Lincoln called it "a rebuke '
                            'and a stumbling-block to tyranny and\n'
                            'oppression."')
    line4 = open_file.write('It took Thomas Jefferson 17 days to write '
                            'the Declaration\nof Independence.')
    line5 = open_file.write('The Bill of Rights is the first 10 amendments'
                            ' to the Constitution.' + '\n')
    line6 = open_file.write('It continues to inspire people around the world'
                            ' to fight for freedom  and equality.' + '\n')
    line7 = open_file.write('The American Flag and Its Flying Rules.')
    line8 = open_file.write('The history of the United States' + '\n')
    line9 = open_file.write('English people in 1607 went to the place now '
                            'called Jamestown,  Virginia.' + '\n')

    open_file.close()

    # программа для подсчета слов в предложении

    def count_word():
        open_file_read = open('text.txt', 'r')
        content = open_file_read.readline()  # по одной строке считываем из
        # файла
        content_len = 0  # всего слов во всех предложениях
        num_string = 0
        while num_string < len(content):
            # разбиваем строку на массив слов, пробел как символ между срок,
            # что бы потом пройтись по нему  len() и узнать количество слов в
            # этой строке
            content_split = content.split()
            content_len += len(content_split)
            content = open_file_read.readline()
            num_string += 1
        # среднее число слов в предложениях.
        average_num = round(content_len / num_string, 2)
        print('Всего слов = ', content_len)
        print('Количество предложений', num_string)
        print('Среднее количество слов в предложениях =', average_num,
              ' (', content_len, '/', num_string, ' = ', average_num, ')')

    count_word()


main()

#
# def main():
#     # open the file
#     infile = open("text.txt", "r")
#
#     # read the lines. remember it creates a list.
#     lines = infile.readlines()
#
#     # to print the lines uncomment below
#     # print(lines)
#
#     # set accumulators.
#     line_count = 0
#     total_word_count = 0
#
#     # read each element in lines list. each element is a sentence.
#     for line in lines:
#         line_count += 1
#
#         # remember: By default, the split method uses spaces as separators
#         # (that is, it returns a list of the words
#         # in the string that are separated by spaces).
#         word_count = len(line.split())
#         total_word_count += word_count
#
#     # calculate the average
#     average = total_word_count / line_count
#
#     # print the average
#     print("The average number of words per sentence is",
#           format(average, ",.2f"))
#
#     # ask user to see if they want to see the table.
#     print()
#     table = input(
#         "If you want to see the table of each line with a count of words enter y: ")
#     print()
#
#     while table == "y" or table == "Y":
#         line_count = 0
#         total_word_count = 0
#         print("Line\t\tWord Count")
#         print("------------------------")
#         for line in lines:
#             line_count += 1
#             print(line_count, end="\t\t")
#             word_count = len(line.split())
#             print(word_count)
#         break
#
#
# # call the main function
# main()
