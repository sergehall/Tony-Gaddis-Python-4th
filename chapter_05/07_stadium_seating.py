# stadium seating

def main():
    class_a_numbers = int(input("How many Class A tickets are sold?: "))
    class_b_numbers = int(input("How many Class B tickets are sold?: "))
    class_c_numbers = int(input("How many Class C tickets are sold?: "))
    print()
    total(class_a_numbers, class_b_numbers, class_c_numbers)

def total(a, b, c):
    total_all = 20 * a + 15 * b + 10 * c
    print("The total income generated from tickets are $",
          format(total_all, ",.2f"), sep='')


main()
