# budget analysis

user_budget = float(input("Please enter the budgeted amount for this month: "))

keep_going = "yes"
total_expense = 0
counter = 0

while keep_going == "yes" or keep_going == "Yes":
    print("Please enter the expense", counter + 1, end='')
    expense = float(input(": "))
    total_expense += expense
    print("If you want to add another expense please type 'yes'."
          " To end type 'no'",
          end="")
    keep_going = input(": ")
    counter += 1  # this is for to make expense 1
    # expense 2 expense 3. It is better.

# Show the result
print()
print("Your budget is ", user_budget)
print("Your total expenses is ", total_expense)

if user_budget > total_expense:
    print("You are under budget.")
else:
    print("You are over budget.")
