# Get user input using input("Enter your age: "). If user is 18 or older,give feedback:You are old enough to drive.
# If below 18 give feedback to wait for the missing ammount of years
age = int(input("Enter your age: "))


if age in range(18, 150):
    print("You are old enough to learn to drive")
elif age in range(1, 17):
    print(f"You need {18 - age} more years to learn to drive")
else:
    print("Are you even human🧐?")

