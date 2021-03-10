# Person and Customer classes

class Person:
    def __init__(self, name, address, phone_num):
        self.__name = name
        self.__address = address
        self.__phone_num = phone_num

    # set accessor methods.
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_num(self):
        return self.__phone_num


# customer is a subclass of Person superclass
class Customer(Person):
    def __init__(self, name, address, phone_num, cust_num, mail_list):

        # pass superclass' __init__ method.
        Person.__init__(self, name, address, phone_num)

        # initialize the data attributes of subclass
        self.__cust_num = cust_num
        self.__mail_list = mail_list

        # set accessor

    def get_cust_num(self):
        return self.__cust_num

    def get_mail_list(self):
        if self.__mail_list == 1:
            status = True  # to keep status of mailing list
            return "Yes"
        else:
            status = False
            return "No"


# Person and Customer Class demo

def main():
    # get the data from the user.
    print("Please enter the following data.")
    name = input("Name: ")
    address = input("Address: ")
    phone_num = input("Phone number: ")
    cust_num = int(input("Customer number: "))
    mail_list = int(
        input("Do you want to be in our mailing list? (0=no 1=yes): "))

    # create the object with these data attributes
    customer = Customer(name, address, phone_num, cust_num, mail_list)

    # display the data.
    print()
    print("Here is the data you entered.")
    print("------------------------------")
    print("Name:", customer.get_name())
    print("Address:", customer.get_address())
    print("Phone number:", customer.get_phone_num())
    print("Customer number:", customer.get_cust_num())
    print("Mailing List:", customer.get_mail_list())


# call the main function
main()
