# RetailItem Class


# 5. Класс Retailitem. Напишите класс под названием Retailltem (Розничная
# товарная единица), который содержит данные о товаре в розничном магазине.
# Этот класс должен хранить данные в атрибутах: описание товара, количество
# единиц на складе и цена. После написания этого класса напишите программу,
# которая создает три объекта Retailltem и сохраняет в них приведенные в
# табл. 10.2 данные.
#           Описание            Количество на складе    Цена
# Товар№ 1  Пиджак 1            2                       59.95
# Товар№ 2  Дизайнерские джинсы 40                      34.95
# Товар№ 3 Рубашка              20                      24.95

class RetailItem:

    def __init__(self, descr, units, price_un):
        self.__description = descr
        self.__units_in_inventory = units
        self.__price = price_un

    def get_description(self):
        return self.__description

    def get_units_in_inventory(self):
        return self.__units_in_inventory

    def get_price(self):
        return self.__price

    def set_description(self, description):
        self.__description = description

    def set_units_in_inventory(self, units_in_inventory):
        self.__units_in_inventory = units_in_inventory

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return self.__description + ", " + \
               str(self.__units_in_inventory) + ", " + \
               str(float(self.__price))


Item1 = RetailItem("Jacket", 12, 59.95)
Item2 = RetailItem("Designer Jeans", 40, 34.95)
Item3 = RetailItem("Shirt", 20, 24.95)

item_list = [["Description", "Units_in_inventory", "Price"],
             ["Jacket", 12, 59.95],
             ["Designer Jeans", 40, 34.95],
             ["Shirt", 20, 24.95]]

# manually enter the values of the instance attributes
num_item = int(input("The number of items you want to enter?: "))
num_item_count = 1
for i in range(num_item):
    print("Item #", num_item_count)
    description = input("description: ")
    units_in_inventory = input("units_in_inventory: ")
    price = input("price: ")
    item_obj = RetailItem(description, units_in_inventory, price)
    item_list.append([item_obj.get_description(),
                      item_obj.get_units_in_inventory(),
                      item_obj.get_price()])
    num_item_count += 1

print()
# Works with a two-dimensional list.
print("item_list = ", item_list)
print()


def display_tab():
    item_num = 1
    for i in range(len(item_list)):
        for j in range(len(item_list[i])):
            if item_num == 1 and i == 0 and j == 0:
                print("{:>8}".format("  "), end=" ")

            if i > 0 and j == 0:
                print("Item # " + str(item_num), end=" ")
                item_num += 1

            if i == 0:
                print("{:>18}".format(item_list[i][j]), end=" ")

            if i > 0:
                print("{:>18}".format(item_list[i][j]), end=" ")

        print()


display_tab()


def date_for_instance(my_list, num_item):
    return RetailItem(my_list[num_item][0],
                      my_list[num_item][1],
                      my_list[num_item][2])


print()
print("Enter the number of the item that you want to display\n"
      "on the screen(number only).")
num = int(input("Num Item: "))
m = date_for_instance(item_list, num)
print(m)
