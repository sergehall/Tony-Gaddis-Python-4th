# word frequency
# 5. Частотность слов. Напишите программу, которая считывает содержимое
# текстового  файла. Она должна создать словарь, в котором ключами являются
# отдельные слова в файле, и значениями - количество появлений каждого слова.
# Например, если слово 'это' появляется 128 раз, то словарь должен содержать
# элемент с ключом 'это' и значением 128. Программа должна либо показать
# частотность

from collections import Counter


def main():
    # Here you will add the key-word and the value-frequency of it in the text
    your_dict = {}

    # creat file text_file_9.4.txt
    my_str = "Welcome! Are are are you completely new to programming? " \
             "'If not then we presume you will be looking for information " \
             "about why and and  how to get started with Python. " \
             "Fortunately an experienced programmer in any programming " \
             "language (whatever it may be) can pick up Python very very " \
             "very very very quickly. It's also easy for beginners " \
             "to use 4 4 4 4   and learn, so jump in!"

    content_clear, dict_count = creat_file(my_str)

    # Total number of unique words
    print("-----------------------------------")
    print("Total number of unique words = ", len(content_clear))
    print("-----------------------------------")
    print("A dictionary with unique words in the key and the "
          "number of that word in the text below.")
    print(dict_count)


# записываем текстовый литерал в файл и очищаем от спец.
# знаков в начале слов и в конце.
def creat_file(str_literal):
    new_file = open('text_file_9.4.txt', 'w')
    content = str_literal.split()

    # empty list where we will add the values and then
    # take len to find out the number
    content_clear = []

    # Using a loop, we clear all the words from the characters
    # at the beginning and end of the word and write it to the file
    # ? ! , . { } ( ) " '
    for i in content:
        if i.endswith('.') or i.endswith(',') or i.endswith('!') \
                or i.endswith(':') or i.endswith(')') or i.endswith('?') \
                or i.endswith('}') or i.endswith('"'):
            new_file.write(i[:-1] + '\n')
            content_clear.append(i[:-1])
            continue
        if i.startswith('.') or i.startswith(',') or i.startswith('!') \
                or i.startswith(':') or i.startswith('(') \
                or i.startswith('?') or i.startswith('{') \
                or i.startswith("'") or i.startswith('"'):
            new_file.write(i[1:] + '\n')
            content_clear.append(i[1:])
            continue
        else:
            new_file.write(i + '\n')
            content_clear.append(i)

    new_file.close()

    # Creating a dictionary where the key is a unique word,
    # and the value is how many times it occurs in the text.
    dict_count = Counter(content_clear)

    # creating a file text_count_9.4.txt containing unique words and
    # their frequency
    new_file_count = open('text_count_9.4.txt', 'w')
    for i in dict_count:
        new_file_count.write(i + ' ' + str(dict_count[i]) + '\n')

    new_file_count.close()

    return content_clear, dict_count


main()
