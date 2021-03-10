# Employee Class

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
               str(self.__id_number) + ", " + \
               self.__department + ", " + \
               self.__job_title


susan_meyers = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
mark_jones = Employee("Mark Jones", 30993, "IT", "Programmer")
joy_rogers = Employee("Joy Rogers", 81222, "Manufacturing", "Engineer")

employee_list = [susan_meyers, mark_jones, joy_rogers]

for employee in employee_list:
    print(employee)
