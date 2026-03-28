# today_is_opposite_day = False

# # Set say_it_is_opposite_day based on today_is_opposite_day:
# if today_is_opposite_day == True:
#     say_it_is_opposite_day = True
# else:
#     say_it_is_opposite_day = False

# # If it is opposite day, toggle say_it_is_opposite_day:
# if today_is_opposite_day == True:
#     say_it_is_opposite_day = not say_it_is_opposite_day

# # Say what day it is:
# if say_it_is_opposite_day == True:
#     print('Today is Opposite Day.')
# else:
#     print('Today is not Opposite Day.')


# print('Enter TB or GB for the advertised unit:')
# unit = input('>')

# if unit == 'TB' or unit == 'tb':
#     discrepancy = 1000000000000 / 1099511627776
# elif unit == 'GB' or unit == 'gb':
#     discrepancy = 1000000000 / 1073741824

# print('Enter the advertised capacity:')
# advertised_capacity = input('>')
# advertised_capacity = float(advertised_capacity)

# real_capacity = str(round(advertised_capacity * discrepancy, 2))

# print('The actual capacity is ' + real_capacity + ' ' + unit)

x = int(input("enter 1,2 or any other number: "))
if x == 1:
    print("Hello")
elif x == 2:
    print("Howdy")
else:
    print("greetings")