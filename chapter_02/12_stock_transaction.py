# Программа расчета купли-продажи акций.

num_share = 2000
per_share_before = 40
com_rate = 0.03
per_share_after = 42.75
commission1 = per_share_before * num_share * com_rate
commission2 = per_share_after * num_share * com_rate

print("The amount of money Joe paid for the stock is $",
      num_share * per_share_before, sep='')
print(
    "The amount of commission Joe paid his broker when he bought "
    "the stock is $", num_share * per_share_before * com_rate, sep='')
print("The amount that Joe sold the stock for is $",
      num_share * per_share_after, sep='')
print(
    "The amount of commission Joe paid his broker when he sold the "
    "stock is $", num_share * per_share_after * com_rate, sep='')
print("Joe made a profit amount of $",
      ((per_share_after - per_share_before) * 2000) - (
              commission1 + commission2))
