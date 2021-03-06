# 3. Принтер дат. Напишите программу, которая считывает от пользователя
# строковое значение, содержащее дату в формате дд/мм/гггг. Она должна
# напечатать дату в формате 12 марта 2018 г.

def main():
    # get the date from the user.
    date = get_date()

    # convert date to like March 12, 2014
    literal_date = convert(date)

    print("The date is below.")
    print(literal_date)


def get_date():
    date = input("Enter the date as mm/dd/yyyy: ")
    return date


def convert(date):
    # first separate the string.
    date_list = date.split("/")

    # create a list for months.
    months = ["January", "February", "March", "April", "May",
              "June", "July", "August", "September", "October",
              "November", "December"]

    new_date = str(months[int(date_list[0]) - 1]) + " " + str(
        date_list[1]) + "," + " " + str(date_list[2])
    return new_date


main()
