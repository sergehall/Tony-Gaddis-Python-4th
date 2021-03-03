# software sales

n_purchase = int(input("Enter the number of packages you would like to buy: "))
package_unit_cost = 99

print()

if 0 < n_purchase < 10:
    subtotal = n_purchase * package_unit_cost
    disc_rate = 0
    discounted_amount = n_purchase * package_unit_cost * disc_rate
    total = (n_purchase * package_unit_cost) - discounted_amount
    print("Your subtotal is $", subtotal, sep='')
    print("You get a discount of $", discounted_amount, sep='')
    print("Your total is $", total, sep='')
elif 10 <= n_purchase <= 19:
    subtotal = n_purchase * package_unit_cost
    disc_rate = 0.10
    discounted_amount = n_purchase * package_unit_cost * disc_rate
    total = (n_purchase * package_unit_cost) - discounted_amount
    print("Your subtotal is $", subtotal, sep='')
    print("You get a discount of $", discounted_amount, sep='')
    print("Your total is $", total, sep='')
elif 20 <= n_purchase <= 49:
    subtotal = n_purchase * package_unit_cost
    disc_rate = 0.20
    discounted_amount = n_purchase * package_unit_cost * disc_rate
    total = (n_purchase * package_unit_cost) - discounted_amount
    print("Your subtotal is $", subtotal, sep='')
    print("You get a discount of $", discounted_amount, sep='')
    print("Your total is $", total, sep='')
elif 50 <= n_purchase <= 99:
    subtotal = n_purchase * package_unit_cost
    disc_rate = 0.30
    discounted_amount = n_purchase * package_unit_cost * disc_rate
    total = (n_purchase * package_unit_cost) - discounted_amount
    print("Your subtotal is $", subtotal, sep='')
    print("You get a discount of $", discounted_amount, sep='')
    print("Your total is $", total, sep='')
elif n_purchase >= 100:
    subtotal = n_purchase * package_unit_cost
    disc_rate = 0.40
    discounted_amount = n_purchase * package_unit_cost * disc_rate
    total = (n_purchase * package_unit_cost) - discounted_amount
    print("Your subtotal is $", subtotal, sep='')
    print("You get a discount of $", discounted_amount, sep='')
    print("Your total is $", total, sep='')
else:
    print("ERROR: You entered an invalid response.")
