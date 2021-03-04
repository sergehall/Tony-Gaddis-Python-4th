# future value

def main():
    present_value = float(input("Enter the account's present value: "))
    interest_rate = float(input("Please enter the monthly interest rate: "))
    months = int(input(
        "Please enter the months that the money will be left in the account: "))
    print()
    future_value = future_value_calculator(present_value, interest_rate, months)
    print("Your future value after", months, "months", end='')
    print(" is $", format(future_value, ",.2f"), sep='')


def future_value_calculator(a, b, c):
    future_value = a * (1 + b) ** c
    return future_value


main()
