# Ackermann's Function

# 8. Функция Аккермана. Функция Аккермана является рекурсивным математическим
# алгоритмом, который используется для проверки, насколько успешно система
# оптимизирует свою производительность в случае рекурсии. Разработайте
# функцию ackermann (m, n), которая решает функцию Аккермана. Примените в
# своей функции следующую логику:
# Если т О, то вернуть п + 1.
# Если п =О, то вернуть ackermann(m - 1, 1).
# Иначе вернуть ackermann (т - 1, ackermann(m, п - 1)).
# После того как вы разработаете свою функцию, протестируйте ее с
# использованием небольших значений для т и п.
# https://overcoder.net/q/820250/понимание-функции-аккермана


def main():
    # ask user for data
    m = int(input("Enter a positive integer for m: "))
    n = int(input("Enter a positive integer for n: "))

    print(ackerman2(m, n))


def ackerman2(m, n, s="%s"):
    print(s % ("A(%d,%d)" % (m, n)))
    if m == 0:
        return n + 1
    if n == 0:
        return ackerman2(m - 1, 1, s)
    n2 = ackerman2(m, n - 1, s % ("A(%d,%%s)" % (m - 1)))
    return ackerman2(m - 1, n2, s)


main()
