# initials.
# 1. Инициалы. Напишите программу, которая получает строковое значение,
# содержащее имя, отчество и фамилию человека и показывает инициалы.
# Например, если пользователь вводит Михаил Иванович Кузнецов, то программа
# должна вывести М.И.К.

def main():
    # name = input("Enter your full name: ")
    name = "Mихаил Иванович Mузнецов"

    print(name)
    print("Your initials: ", initials(name))


def initials(full_name):
    initial = ""
    for ch in full_name.split():
        initial += ch[:1] + "."

    return initial


main()
