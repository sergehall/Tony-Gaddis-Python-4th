# 6. Допустим, что переменная names ссылается на список строковых значений.
# Напишите программный код, который определяет, находится ли имя 'Руби' в
# списке names. Если это так, то выведите сообщение 'Привет, Руби! ' . В
# противном случае выведите сообщение ' Руби отсутствует ' .

def main():
    names = ['Ruby', 'Nina', 'Bob']
    search_name = input('Search name: ')
    search_name_in_list(names, search_name)


def search_name_in_list(list_x, search_name):
    if search_name in list_x:
        print('Hello', search_name, '!')
    else:
        print(search_name, 'not found.')


main()
