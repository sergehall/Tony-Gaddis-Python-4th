# sum of digits in a string

# 2. Сумма цифр в строке. Напишите программу, которая просит пользователя
# ввести ряд однозначных чисел без разделителей. Программа должна вывести на
# экран сумму всех однозначных чисел в строковом значении. Например,
# если пользователь вводит


def main():
    # mystring = input("Enter a string containing numbers: ")
    mystring = '1234ert567rtuy8UUd939'

    sum_string, sum_letter, letters = sum_str(mystring)
    print("The sum of digits in the number of '",
          mystring, "' is ", sum_string, sep="")
    print("Found_letters '", letters, "' into string = ", sum_letter, sep="")


def sum_str(string):
    sum_string = 0
    sum_letter = 0
    letters = ""
    for ch in string:
        if ch.isdigit():
            sum_string += int(ch)
        if ch.isalpha():
            letters += ch
            sum_letter += 1

    return sum_string, sum_letter, letters


main()
