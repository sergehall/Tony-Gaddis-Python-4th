# 11. Разделитель слов. Напишите программу, которая на входе принимает
# предложение, в котором все слова написаны без пробелов, но первая буква
# каждого слова находится в верхнем регистре. Преобразуйте предложение в
# строковое значение, в котором слова отделены пробелами, и только первое
# слово начинается с буквы в верхнем регистре. Например, строковое значение
# "ОстановисьИПочувствуйЗапахРоз" будет преобразовано в "Остановись и
# почувствуй запах роз".


def main():
    print()
    print('PythonIsAprogrammingLanguageThatLetsYouWork'
          'QuicklyAndIntegrateSystemsMoreEffectively.')
    print()
    my_string = input("Enter a string like one above: ")
    word_separator(my_string)


def word_separator(string):
    print(string[0].upper(), end='')
    for i in range(1, len(string)):
        if string[i].isupper():
            print(' ', end='')
            print(string[i].lower(), end='')
        else:
            print(string[i], end='')


main()

