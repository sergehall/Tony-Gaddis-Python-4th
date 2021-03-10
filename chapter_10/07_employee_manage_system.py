# Employee Management System

class Employee:

    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def __str__(self):
        return self.__name + ", " + \
               self.__id_number + ", " + \
               self.__department + ", " + \
               self.__job_title


import pickle

LOOK = 1
ADD = 2
CHANGE = 3
DELETE = 4
CLEAN = 5
QUIT = 6


def main():
    dict_employees = reactivate_dict()
    while True:

        print("Look up an employee in the dictionary:...1")
        print("Add a new employee:......................2")
        print("Change name, department, and job title:..3")
        print("Delete an employee:......................4")
        print("Clean dic:...............................5")
        print("Quit: ...................................6")

        num_pr = int(input("Enter number:\n "))

        if num_pr == QUIT:
            break

        if num_pr == LOOK:
            look_up(dict_employees)

        if num_pr == ADD:
            n = int(input("How many employees do you want to add?:\n "))
            add_dic_employee(dict_employees, n)

        if num_pr == CHANGE:
            change_name_id_number_department_job_title(dict_employees)

        if num_pr == CLEAN:
            clean(dict_employees)

        if num_pr == DELETE:
            delete_an_employee(dict_employees)

    print_dic_obj(dict_employees)
    # консервируем фаил
    preserve_dict(dict_employees)


def clean(dict_employees):
    dict_employees.clear()


def print_dic_obj(dict_employees):
    print("All object in dictionary:")
    for i in dict_employees:
        print(i, ":", dict_employees[i])
    if dict_employees == {}:
        print("The dictionary is empty.")


def reactivate_dict():
    dict_employees = {}
    end_of_file = False
    try:
        input_file = open('employees.dat', 'rb')
        while not end_of_file:
            try:
                # Расконсервировать следующий объект.
                employees = pickle.load(input_file)
                dict_employees.update(employees)
            except EOFError:
                # Установить флаг, чтобы обозначить, что бьm
                # достигнут конец файла.
                end_of_file = True
        # close file
        input_file.close()
        print("The current dictionary taken from the binary file and \n"
              "are put in the dictionary dict_employees.")

    except FileNotFoundError:
        print("File not found creat empty dictionary 'dict_employees'.")
        dict_employees = {}

    return dict_employees


def preserve_dict(dict_employees):
    # Открыть файп для двоичной записи.
    output_file = open("employees.dat", 'wb')
    pickle.dump(dict_employees, output_file)
    output_file.close()
    print("The dict_employees dictionary is "
          "preserved in the employees.dat file.")


def look_up(dict_employees):
    # Для управления повторением цикла
    again = 'y'
    while again == 'y':
        id_number = input('What id_number you looking for:? ')
        if id_number in dict_employees:
            print(dict_employees[id_number])
        else:
            print("Not found id_number:")
        again = input('Would you like to try again? If yes = y, no = any ')
    return dict_employees


def add_dic_employee(dict_employees, n):
    for i in range(n):
        print("employee #" + str(i + 1))
        name = input("name: ")
        id_number = input("id_number: ")
        department = input("department: ")
        job_title = input("job_title: ")
        i = Employee(name, id_number, department, job_title)
        dict_employees.update({id_number: i})
    return dict_employees


def change_name_id_number_department_job_title(dict_employees):
    again = "y"
    while again == "y":
        id_num = input("What id_number you looking for?:\n")
        if id_num in dict_employees:
            name = input("name: ")
            id_number = input("id_number: ")
            department = input("department: ")
            job_title = input("job_title: ")
            id_num_new = Employee(name, id_number, department, job_title)
            # Обновить запись.
            del dict_employees[id_num]
            dict_employees[id_number] = id_num_new
            print('Информация обновлена.')
            again = input('Would you to change again? If yes = y, no = any ')

        else:
            print("Not found id_number:")
            again = input('Would you to change again?  If yes = y, no = any ')

    return dict_employees


def delete_an_employee(dict_employees):
    again = 'y'
    while again == 'y':
        id_number = input('What id_number you looking for:? ')
        if id_number in dict_employees:
            print(dict_employees[id_number])
            del dict_employees[id_number]
            print("dict_employees[id_number] DELETED")
        else:
            print("Not found id_number:")
        again = input('Would you like to try again? If yes = y, no = any ')
    return dict_employees


main()
