#  file encryption and decryption
# 3. Шифрование и дешифрование файлов. Напишите программу, которая применяет
# словарь для присвоения "кодов" каждой букве алфавита. Например:
# codes = { , А, : , % , , , а, : , 9 ,, , Б, : , @,, , 6 , : , #, ... }
# Здесь букве А присвоен символ %, букве а - число 9, букве Б - символ @
# и т. д. Программа должна открыть заданный текстовый файл, прочитать его
# содержимое и применить словарь для записи зашифрованной версии содержимого
# файла во второй файл. Каждый символ во втором файле должен содержать код
# для соответствующего символа из первого файла. Напишите вторую программу,
# которая открывает зашифрованный файл и показывает его дешифрованное
# содержимое на экране.

def main():
    """
      my_crypt.txt  - file created for encryption
      en_crypt.txt - encrypted file
      de_crypt_code.txt - decrypted file the result is the same as my_crypt.txt
    """
    # словарь для шифрования ключ - соответствует реальной букве ,
    codes = {'A': '!', 'B': '@', 'C': '23', 'D': '$', 'E': '%', 'F': '^',
             'G': '&', 'H': '*', 'I': '(',
             'J': ')', 'K': '-', 'L': '_', 'M': '+', 'N': '=', 'O': '`',
             'P': '~', 'Q': '{', 'R': '[',
             'S': '}', 'T': ']', 'U': ':', 'V': ';', 'W': '"', 'X': '<',
             'Y': '>', 'Z': '0', 'a': '1',
             'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7',
             'h': '8', 'i': '9', 'j': 'a',
             'k': 'b', 'l': 'c', 'm': 'd', 'n': 'e', 'o': 'f', 'p': 'g',
             'q': 'h', 'r': 'i', 's': 'j',
             't': 'k', 'u': 'l', 'v': 'm', 'w': 'n', 'x': 'o', 'y': 'p',
             'z': 'q', ' ': 't', '1': '18', '.': '..', ',': '__'}

    print()
    print("Welcome to File Encryption and Decryption Program")
    print()
    print("Enter the text manually press 1.")
    print("Use the text that you have already prepared enter 2.")
    choice = int(input("1 or 2: "))
    s_str = 1  # By default
    if choice == 1:
        s_str = input("Enter your text: ")
    if choice == 2:
        s_str = 'California is a state Q1 United States.'

    creat_file(s_str)
    encrypting_file(codes)
    decrypt_file(codes)

    print()
    print("Done and written in files.")
    print("*************************************************")
    print('The file with the text you entered: my_crypt.txt')
    print("Encrypt a file: en_crypt.txt")
    print("Decrypt a file: de_crypt_code.txt")


# creat file my_crypt.txt
def creat_file(s_str):
    new_file = open('my_crypt.txt', 'w')
    for i in s_str:
        new_file.write(i + '\n')
    new_file.close()


# the function opens the file my_crypt.txt, reads it, encrypts it
# and write to a new file en_crypt.txt
def encrypting_file(codes):
    my_crypt = open('my_crypt.txt', 'r')
    en_crypt = open('en_crypt.txt', 'w')
    content = my_crypt.readlines()
    for i in content:
        if codes.get(i.rstrip('\n')):
            en_crypt.write((codes.get(i.rstrip('\n'))) + '\n')
        else:
            en_crypt.write('Not found ' + str(i) + '\n')

    my_crypt.close()
    en_crypt.close()


# Decrypting the file en_crypt.txt
def decrypt_file(codes):
    en_crypt = open('en_crypt.txt', 'r')
    de_crypt_code = open('de_crypt_code.txt', 'w')

    content = en_crypt.readlines()
    # пробегаемся по всему контенту и ищем вторым циклом в словаре шифра
    # есть ли у нас совпадения если есть такое значение то печатаем его
    # ключ, если находим флаг в виде текстового литерала 'Not found ',
    # то добавляет последнее значение в этой строке(оно мжет быть разным
    # и добавляется при шифровании последним значением,
    # пример 'Not found Q')
    for i in content:
        for k, v in codes.items():

            if i.rstrip('\n') == v:
                de_crypt_code.write(k + '\n')

            if i.rstrip('\n')[:10] == 'Not found ':
                de_crypt_code.write(i.rstrip('\n')[10:] + '\n')
                break

    en_crypt.close()
    de_crypt_code.close()


main()
