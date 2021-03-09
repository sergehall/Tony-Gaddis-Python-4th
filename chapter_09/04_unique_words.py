# unique words
# # 4. Уникальные слова. Напишите программу, которая открывает заданный
# текстовый файл (text_file_9.4.txt) и затем показывает список всех
# уникальных слов в файле. (Подсказка: храните слова в качестве элементов
# множества.)

def main():
    my_str = "Welcome! Are are are you completely new to programming? " \
             "'If not then we presume you will be looking for information " \
             "about why and how to get started  with Python. Fortunately an " \
             "experienced programmer in any programming language " \
             "(whatever it may be) can pick up Python very quickly. " \
             "It's also easy for beginners to use and learn, so jump in!"
    print()
    print("Unique words are below: ")
    print(creat_file(my_str))
    print("Total unique words in the text =", len(creat_file(my_str)))

    # записываем текстовый литерал в файл и очищаем от спец. знаков
    # в начале слов и в конце.  фунция чтения файла и определения в нем
    # уникальных слов
def creat_file(str_literal):
    # creat file text_file_9.4.txt.
    # Where will all the unique words be written
    new_file = open('text_file_9.4.txt', 'w')
    content = str_literal.split()

    # пустое множество куда бужем складывать значения и потом возмем
    # len что бы ущнать количество
    content_clear = set([])

    # Циклом очищаем циклом все слова от знаков в начале
    # и конце словаи записываем это в файл
    # ? ! , . { } ( ) " '
    for i in content:

        if i.endswith('.') or i.endswith(',') \
                or i.endswith('!') or i.endswith(':') \
                or i.endswith(')') or i.endswith('?') \
                or i.endswith('}') or i.endswith('"'):
            new_file.write(i[:-1] + '\n')
            content_clear.update([i[:-1]])
            continue
        if i.startswith('.') or i.startswith(',') \
                or i.startswith('!') or i.startswith(':') \
                or i.startswith('(') or i.startswith('?') \
                or i.startswith('{') or i.startswith("'") or \
                i.startswith('"'):
            new_file.write(i[1:] + '\n')
            content_clear.update([i[1:]])
            continue
        else:
            new_file.write(i + '\n')
            content_clear.update([i])

    new_file.close()
    return content_clear


main()
