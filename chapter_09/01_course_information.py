# course information
# 1. Информация об учебных курсах. Напишите программу, которая создает
# словарь, содержащий номера курсов и номера аудиторий, где проводятся курсы.
# Словарь должен иметь приведенные в табл. 9 .2 пары ключ/значение.


# создаем сами номер класса и в виде списка храним инву о нем, сложно
# изменять потом
def main():
    dct_room = {'CS101': '3004', 'CS102': '4501', 'NT110': '1244'}
    dct_inst = {'CS101': 'Billy', 'CS102': 'Ali', 'NT110': 'Serge'}
    dct_meet = {'CS101': '8:00', 'CS102': '9:00', 'NT110': '10:00'}

    try:
        num_course = input("Enter a course number: ")

        print('Room number: ', dct_room[num_course.upper()])
        print('Instructor: ', dct_inst[num_course.upper()])
        print('Meeting time: ', dct_meet[num_course.upper()])

    except KeyError:
        print('Not found course')
    print()

    # желаете добавить курс?
    print('Would you like to add a course?')
    y = input("Enter y / yes, any ch / no: ")

    while y == 'y':
        creat_course(dct_room, dct_inst, dct_meet)
        y = input('Would you like to add more classes? '
                  'y / yes, any ch / no: : ')

        print(dct_room)
        print(dct_inst)
        print(dct_meet)


# сам хочу создавать курс вызываем эту функцию
def creat_course(dct_room, dct_inst, dct_meet):
    new_dct_room = {}
    new_dct_inst = {}
    new_dct_meet = {}

    num_course = int(input('How many classes do you want to enter? '))

    for c in range(num_course):
        enter_class = input('enter new num class: ')

        key_room = input('Room Number: ')
        key_inst = input('Instructor: ')
        key_meet = input('Meeting Time: ')

        new_dct_room.update({enter_class: key_room})
        new_dct_inst.update({enter_class: key_inst})
        new_dct_meet.update({enter_class: key_meet})

    return dct_room.update(new_dct_room), dct_inst.update(
        new_dct_inst), dct_meet.update(
        new_dct_meet)


main()

# # course information
#
# def main():
#     # create dictionaries
#     room_number = {"CS101": 3004, "CS102": 4501, "CS103": 6755,
#                    "NT110": 1244, "CM241": 1411}
#     instructors = {"CS101": "Haynes", "CS102": "Alvarado",
#                    "CS103": "Rich", "NT110": "Burke", "CM241": "Lee"}
#     times = {"CS101": "8:00 a.m.", "CS102": "9:00 a.m.",
#              "CS103": "10:00 a.m.", "NT110": "11:00 a.m.", "CM241": "1:00 p.m."}
#
#     # get the course number
#     course_number = input("Enter a course number: ")
#
#     # display results
#     display(room_number, instructors, times, course_number)
#
#
# def display(r, i, t, course):
#     print()
#     print("Room Number:", r[course])
#     print("Instructor:", i[course])
#     print("Meeting Time: :", t[course])
#
#
# # call the main function
# main()
