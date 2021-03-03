# magic dates

month = int(input("Enter a month (1-12): "))
day = int(input("Enter a day (1-30): "))
year = int(input("Enter a year (two-digit): "))

if month * day == year:
    print(month, "/", day, "/", year, " is a magic date.", sep="")
else:
    print(month, "/", day, "/", year, " is NOT a magic date.", sep="")
