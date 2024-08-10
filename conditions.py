# # if condition:
# #   this part of code runs for truthy conditions

# a = -3
# if a > 0:
#     print('A is a positive number')

# # If else
# if a > 0:
#     print('A is a positive number')
# else:
#     print('Chai!!!')


# # ------if elif else------
# # if conditions:
# #     code
# # elif condition:
# #     code
# # else:
# #     code

# if a > 0:
#     print('A is a positive number')
# elif a < 0:
#     print('A is a negative number')
# else:
#     print('Chai!!!,na Zero')


# # combined
# a = -4
# print("A is a positive number") if a > 0 else print("A is a pessimistic and negative number")

# # nested conditions
# a = 4
# if a > 0:
#     if a % 2 == 0:
#         print('A is a positive and even integer')
#     else:
#         print('A is a positive number')
# elif a == 0:
#     print('A is zero')
# else:
#     print('A is a negative number')


# If and Or logical operators
user_name = 'James'
access_level = 3

if user_name == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')
