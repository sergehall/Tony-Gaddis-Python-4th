# 8. Имена и адреса электронной почты. Напишите программу, которая
# сохраняет имена и адреса электронной почты в словаре в виде пар
# ключ/значение. Программа должна вывести меню, которое позволяет
# пользователю отыскать адрес электронной почты человека, добавить новое имя
# и адрес электронной почты, изменить существующий адрес электронной почты и
# удалить существующее имя и адрес электронной почты. Программа должна
# законсервировать словарь и сохранить его в файле при выходе пользователя из
# программы. При каждом запуске программы она должна извлечь словарь
# из файла и его расконсервировать.

import pickle


def main():
    #  Открываем функцией reactivate_dict() законсервированный файл ,
    #  это у нас словарь где ключ имя, а значение email присваеваем
    #  переменной person_name_email и дальше с ней работаем
    #  как со словарем передавая его в другие фунции.
    person_name_email = reactivate_dict()

    # функция выбора команды и ее исполнение.
    choose_commanda(person_name_email)

    # законсервирование обновленного словаря
    preserve_dict(person_name_email)


def choose_commanda(dict_name_email):
    print('Если вы хотите найти email по имени нажмите 1')
    print('Если вы хотите добать новую пару имя и email нажмите 2')
    print('Если вы хотите изменить email нажмите 3')
    print('Если вы хотите удалить пару ключ и значение нажмите 4')

    again = True
    while again:
        try:
            command = int(input('Enter number: '))
            if 1 <= command <= 4:
                again = False
                if command == 1:
                    search_name(dict_name_email)
                if command == 2:
                    add_name_email(dict_name_email)
                if command == 3:
                    add_email(dict_name_email)
                if command == 4:
                    del_name_email(dict_name_email)
            else:
                print('Введи число от 1 до 4.')
        except ValueError:
            print('Enter number not str.')


#  расконсервируем обьект
def reactivate_dict():
    person_name_email = {}
    end_of_file = False
    input_file = open('name_email.dat', 'rb')

    while not end_of_file:
        try:
            # Расконсервировать следующий объект.
            person = pickle.load(input_file)
            person_name_email.update(person)
        except EOFError:
            # Установить флаг, чтобы обозначить, что бьm достигнут конец файла.
            end_of_file = True
    # close file
    input_file.close()
    print('Текущий словарь взятый из бинарного файла:')
    print(person_name_email)
    return person_name_email


#  поиск в словаре имени и email
def search_name(name_email):
    again = 'y' # Для управления повторением цикла

    while again == 'y':
        name = input('What name are you looking for? ')
        name_search = name_email.get(name, 'Not found')
        print('Name: ', name, '; ', 'email: ', name_search)
        again = input('Would you like to try again? If yes = y, no = any ')


#  функция добовляет в словарь новую пару имя и email
def add_name_email(dict_name_email):
    again = 'y'  # Для управления повторением цикла

    while again.lower() == 'y':
        # update new name and email
        name = input('Enter new name: ')
        if name in dict_name_email:
            print('Такое имя есть в словаре.')
            again = input('Желаете ввести еще данные? (y/n): ')
            continue
        email = input('Enter new email: ')
        dict_name_email.update({name: email})
        # Пользователь желает ввести еще данные?
        again = input('Желаете ввести еще данные? (y/n): ')


#  функция изменяет email
def add_email(dict_name_email):
    again = 'y'  # Для управления повторением цикла

    while again.lower() == 'y':
        # update new name and email
        name = input('Enter a name yoy are looking for: ')
        if name in dict_name_email:
            email = input('Enter email: ')
            dict_name_email.update({name: email})
            again = input('Желаете еще изменить данные? (y/n): ')
        else:
            print('Такого имени нет в словаре.')
            again = input('Желаете еще изменить данные? (y/n): ')


#  функция del key and values из словаря
def del_name_email(dict_name_email):
    again = 'y'  # Для управления повторением цикла

    while again.lower() == 'y':
        # update new name and email
        name = input('Enter a name you want to delete: ')
        if name in dict_name_email:
            del dict_name_email[name]
            again = input('Желаете еще удалить пару? (y/n): ')
        else:
            print('Такого имени нет в словаре.')
            again = input('Желаете еще удалить пару? (y/n): ')


# консервируем обьект
def preserve_dict(dict_name_email):
    # Открыть файп для двоичной записи.
    output_file = open('name_email.dat', 'wb')
    pickle.dump(dict_name_email, output_file)
    output_file.close()
    print(dict_name_email)


main()
