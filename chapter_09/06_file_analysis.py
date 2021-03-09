# file analysis
# # 6. Анализ файла. Напишите программу, которая читает содержимое двух
# текстовых файлов
# # и сравнивает их следующим образом:
# # • показывает список всех уникальных слов, содержащихся в обоих файлах;
# # • показывает список слов, входящих в оба файла;
# # • показывает список слов из первого файла, не входящих во второй;
# # • показывает список слов из второго файла, не входящих в первый;
# # • показывает список слов, входящих либо в первый, либо во второй файл,
# но не входящих в оба файла одновременно.
# # Подсказка: для выполнения этого анализа используйте операции
# над множествами.

def main():
    my_str = "Welcome! Are are are you completely new to programming? 'If" \
             " not then we presume you will be looking for information about " \
             "why and how to get started with Python. Fortunately an " \
             "experienced programmer in any programming language (whatever " \
             "it may be) can pick up Python very quickly. It's also easy for" \
             " beginners to use and learn, so jump in! can pick up Python " \
             "very quickly. Newton "

    my_str2 = "Welcome! Are are are you completely new to programming? 'If " \
              "not then we presume you will be looking for information about " \
              "why and how to get started with Python. Fortunately an " \
              "experienced programmer in any programming language (whatever " \
              "it may be) can pick up Python very quickly. It's also easy " \
              "for beginners to use and learn, so jump in! can pick " \
              "up Python very quickly. Lomonosov"

    file_name = 'text_count_9.6.txt'
    file_name2 = 'text_count_9_6_2.txt'

    # программа записывающая текст в файл
    def creat_file(str_literal, name_file):
        # name_file = input('enter name file: ')  # называем файл

        str_literal_split = str_literal.split()  # разделяем str по пробелам

        new_file = open(str(name_file), 'w')
        for i in str_literal_split:
            new_file.write(i + '\n')
        new_file.close()

    creat_file(my_str, file_name)
    creat_file(my_str2, file_name2)

    # Программа отрывающа я файл и записывает значения в set предварительно
    # Циклом перед записью очищаем все слова от знаков в начале и конце
    # словаи записываем это в файл
    # ? ! , . { } ( ) " '
    def clear(name_file):
        out_file = open(str(name_file), 'r')
        content = out_file.readlines()
        # создаем список в котором убраны в конце слова '\n'
        content_rstrip = []
        for i in content:
            content_rstrip.append(i.rstrip())

        content_clear = set(
            [])  # пустое множество куда бужем складывать значения и потом
        for i in content_rstrip:
            if i.endswith('.') or i.endswith(',') or i.endswith('!') \
                    or i.endswith(':') or i.endswith(')') \
                    or i.endswith('?') or i.endswith('}') \
                    or i.endswith('"'):
                content_clear.update([i[:-1]])
                continue
            if i.startswith('.') or i.startswith(',') or i.startswith(
                    '!') or i.startswith(':') or i.startswith('(') \
                    or i.startswith('?') or i.startswith('{') \
                    or i.startswith("'") or i.startswith('"'):
                content_clear.update([i[1:]])
                continue
            else:
                content_clear.update([i])

        out_file.close()

        # print(content_clear)
        # print(len(content_rstrip))

        return content_clear  # возращаем set очищиный по краям от знаков

    print()
    print('Set all unique words contained in both files:')
    union_file = clear(file_name) | clear(file_name2)
    print(union_file)
    print('Number of words: ', len(union_file))
    print()
    print('Set words included in both files:')
    inter_file = clear(file_name) & clear(file_name2)
    print(inter_file)
    print('Number of words: ', len(inter_file))
    print()
    print('Set words from the first file that are not '
          'included in the second one:')
    diff_file = clear(file_name) - clear(file_name2)
    print(diff_file)
    print('Number of words: ', len(diff_file))
    print()
    print('Set words from the second file that are not'
          ' included in the first one:')
    diff_file2 = clear(file_name2) - clear(file_name)
    print(diff_file2)
    print('Number of words: ', len(diff_file2))
    print()
    print('Shows a set of words that are included in either the \n '
          'first or second file, but are not included in both \n'
          'files at the same time:')
    symm_diff_file = clear(file_name) ^ clear(file_name2)
    print(symm_diff_file)
    print('Number of words: ', len(symm_diff_file))


main()
