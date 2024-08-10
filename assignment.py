january_money = 30000
february_money = 23000
march_money = 26000
april_money = 10000
may_money = 3000


# Put all the money in a list
money_list = [january_money, february_money, march_money, april_money, may_money]

# How much less did I spend in february?
less_money = january_money - february_money
print(f"I spent {less_money} naira less in February")

# Add up the first 3 months
total_money = january_money + february_money + march_money
print(f"I spent {total_money} naira in the first 3 months")

# Check if I spent exactly 15000 naira
if january_money == 15000:
    print(f"I spent 15000 naira in January")
elif february_money == 15000:
    print(f"I spent 15000 naira in February")
elif march_money == 15000:
    print(f"I spent 15000 naira in March")
elif april_money == 15000:
    print(f"I spent 15000 naira in April")
elif may_money == 15000:
    print(f"I spent 15000 naira in May")
else:
    print("I didn't spend 15000 naira in any month")

# Add June money to the list
june_money = 1980
money_list.append(june_money)

# I got back 5000 naira in April
april_money = april_money - 5000
money_list[3] = april_money  # Change April's money in the list

print(f"My new money list is: {money_list}")
