class Patient:

    def __init__(self, name, middle_name, last_name,
                 address, phone, contact_name, contact_name_phone):
        self.__name = name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__phone = phone
        self.__contact_name = contact_name
        self.__contact_name_phone = contact_name_phone

    # Accessor method
    def get_name(self):
        return self.__name

    def get_middle_name(self):
        return self.__middle_name

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_contact_name(self):
        return self.__contact_name

    def get_contact_name_phone(self):
        return self.__contact_name_phone

    # Mutator method

    def set_name(self, name):
        self.__name = name

    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name

    def set_age(self, last_name):
        self.__last_name = last_name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def set_contact_name(self, contact_name):
        self.__contact_name = contact_name

    def set_contact_name_phone(self, contact_name_phone):
        self.__contact_name_phone = contact_name_phone

    def __str__(self):
        return "Name: " + self.__name + " " + \
               self.__middle_name + " " + \
               self.__last_name + "\n" + \
               "Address: " + self.__address + "\n" + \
               "Phone: " + self.__phone + "\n" + \
               "Contact name: " + self.__contact_name + "\n" + \
               "Phone contact name: " + self.__contact_name_phone


class Procedure:
    def __init__(self, procedure_name, date, practitioner, charge):
        self.__procedure_name = procedure_name
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge

    def set_procedure_name(self, procedure_name):
        self.__procedure_name = procedure_name

    def set_date(self, date):
        self.__date = date

    def set_practitioner(self, practitioner):
        self.__practitioner = practitioner

    def set_charge(self, charge):
        self.__charge = charge

    def get_procedure_name(self):
        return self.__procedure_name

    def get_charge(self):
        return self.__charge

    def __repr__(self):
        return f"Procedure {self.__procedure_name}"

    def __str__(self):
        return "Procedure name: " + self.__procedure_name + "\n" + \
               "Date: " + self.__date + "\n" + \
               "Practitioner: " + self.__practitioner + "\n" + \
               "Charge: " + str(self.__charge)


patient1 = Patient("Bob", "", "Saimond", "Los Angeles, 123 Beverly str.",
                   "333-5555", "Sam", "666-7777")

print(patient1)
print()

procedure1 = Procedure("Physical Exam", "05.11.2021", "Dr. Irvine", 125)
procedure2 = Procedure("X-ray", "05.11.2021", "Dr. Jamison", 410)
procedure3 = Procedure("Blood test", "05.11.2021", "Dr. Smith", 200)

total_procedure = [procedure1, procedure2, procedure3]

for procedure in total_procedure:
    print(procedure)
    print()


def total_charge(list_obj):
    total = 0
    for inst in list_obj:
        total += Procedure.get_charge(inst)
    return total


print("Total charge: $", total_charge(total_procedure), sep="")

num_procedure = int(input("Enter the number of procedures you want to add: "))
for i in range(num_procedure):
    name_procedure = input("name_procedure: ")
    date = input("date: ")
    practitioner = input("name_practitioner: ")
    charge = int(input("charge: "))
    name_p = Procedure(name_procedure, date, practitioner, charge)
    total_procedure.append(name_p)

print(total_procedure)
for i in total_procedure:
    print(i)
