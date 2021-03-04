# maximum of two values

def main():
    print("This program compares two numbers that you entered.")
    number1 = int(input("Please enter the number 1: "))
    number2 = int(input("Please enter the number 2: "))
    calculate_greater(number1, number2)


def calculate_greater(a, b):
    if a > b:
        print("The number", a, "is greater than number", b)
    elif a == b:
        print("The numbers are the same. The number you entered is", a)
    else:
        print("The number", b, "is greater than number", a)


main()
