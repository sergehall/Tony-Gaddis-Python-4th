# # 5. Алфавитный переводчик номера телефона. Многие компании используют телефонные
# # номера наподобие 555-GET-FOOD, чтобы клиентам было легче запоминать эти номера.
# # На стандартном телефоне буквам алфавита поставлены в соответствие числа следующим
# # образом: А,В и С=2 ; D,Е и F=З. phone_num = input('nnn-XXX-XXXX. Где n-
# цифра, X - буквы: ')

def main():
    print("'x' can be either a letter or a number.")
    phone_num = input('Enter a phone number in the format xxx-xxx-xxxx: ')
    print(phone_num)
    print("Phone number alphabet:", phone_num)
    print("Phone number: ", end="")
    print_number_alphabet(phone_num)


def print_number_alphabet(num_phone):
    for ch in num_phone:
        if ch.islower():
            ch = ch.upper()
        if ch.isdigit():
            print(ch, end='')
        elif ch == '-':
            print('-', end='')
        elif ch == 'A' or ch == 'B' or ch == 'C':
            print('2', end='')
        elif ch == 'D' or ch == 'E' or ch == 'F':
            print('3', end='')
        elif ch == 'G' or ch == 'H' or ch == 'I':
            print('4', end='')
        elif ch == 'J' or ch == 'K' or ch == 'L' \
                or ch == 'V':
            print('5', end='')
        elif ch == 'M' or ch == 'N' or ch == 'O' \
                or ch == 'U':
            print('6', end='')
        elif ch == 'P' or ch == 'Q' or ch == 'R' \
                or ch == 'S' or ch == 'T':
            print('7', end='')
        elif ch == 'W' or ch == 'X' or ch == 'Y' \
                or ch == 'Z':
            print('8', end='')
        else:
            print('-', end='')


main()


