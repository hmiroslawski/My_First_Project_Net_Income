# print("Prices:\n"
#       "Bubblegum: $2\n"
#       "Toffee: $0.2\n"
#       "Ice cream: $5\n"
#       "Milk chocolate: $4\n"
#       "Doughnut: $2.5\n"
#       "Pancake: $3.2")

# Total earnings - last moth
bubblegum = 202
toffee = 118
ice_cream = 2250
milk_chocolate = 1680
doughnut = 1075
pancake = 80
total_income = bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake

# Expenses
# cleaner = 850
# vendor = 1120
# manager = 1300
# loader = 900
# # staff_expenses = cleaner + vendor + manager + loader
# electricity = 100
# municipal_service = 90
# security = 30
# other_expenses = electricity + municipal_service + security

# Printing area
print("\n")

print(f"Earned amount:\n"
      f"Bubblegum: ${bubblegum}\n"
      f"Toffee: ${toffee}\n"
      f"Ice cream: ${ice_cream}\n"
      f"Milk chocolate: ${milk_chocolate}\n"
      f"Doughnut: ${doughnut}\n"
      f"Pancake: ${pancake}")

print("\n")

print(f"Income: ${total_income}")
print(f"Staff expenses:")
staff_expenses = int(input())
print(staff_expenses)
print("Other expenses:")
other_expenses = int(input())
net_income = total_income - staff_expenses - other_expenses
print("Net income: $", net_income)