# Employee and ProductionWorker classes

class Employee:
    # the __init__ method initializes the data attributes
    # for the employee name and employee number
    def __init__(self, emp_name, emp_num):
        self.__employee_name = emp_name
        self.__emplyee_number = emp_num

    # the following are mutator methods for class's
    # data attributes
    def set_employee_name(self, emp_name):
        self.__employee_name = emp_name

    def set_employee_number(self, emp_num):
        self.__emplyee_number = emp_num

    # the following are accessor methods for class's
    # data attributes
    def get_employee_name(self):
        return self.__employee_name

    def get_employee_number(self):
        return self.__emplyee_number


# ProductionWorker class is a subclass of Employee.
class ProductionWorker(Employee):

    # __init__ method initializes the superclass' __init__method
    def __init__(self, emp_name, emp_num, shift_num, pay_rate):
        # initalize the superclass
        Employee.__init__(self, emp_name, emp_num)

        # initialize the new attributes
        self.__shift_number = shift_num
        self.__pay_rate = pay_rate

    # mutator method for data attributes.
    def set_shift_number(self, shift_num):
        self.__shift_number = shift_num

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    # accessor methods
    def get_shift_number(self):
        if self.__shift_number == 1:
            return "Day"
        if self.__shift_number == 2:
            return "Night"

    def get_pay_rate(self):
        return self.__pay_rate


def main():
    # get the data from user
    print("Please enter the following data.")

    emp_name = input("Employee Name: ")
    emp_num = int(input("Employee Number: "))
    shift_num = int(input("Shift Number (1 for day 2 for night): "))
    pay_rate = float(input("Enter hourly pay rate: "))
    print()

    # create an object of ProductionWorker.
    employee = ProductionWorker(emp_name, emp_num, shift_num, pay_rate)

    # display the data
    print("Here is the data that you entered.")
    print("------------------------------------")
    print("Name:", employee.get_employee_name())
    print("Employee Number:", employee.get_employee_number())
    print("Shift time:", employee.get_shift_number())
    print("Hourly pay rate: $", format(employee.get_pay_rate(), ",.2f"), sep="")


# call the main function
main()