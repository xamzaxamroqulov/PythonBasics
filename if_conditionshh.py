# 08/15/2020 IF CONDITIONS ####

cars = ['lexus', 'bugatti', 'bmw', 'ferrari']
for car in cars:
    if car == 'bmw':  # NOTE: car == 'bmw' >> expression to return TRUE or FALSE.
        print(car.upper())  # NOTE: if expression returns TRUE, else case is skipped.
    else:
        print(car.title())  # NOTE: if expression returns FALSE, if case is skipped.
print('================================================================================')

# # if expression:
# #     code to execute when expression is True
# # elif expression2:
# #     code to execute when expression2 is True
# # else:
# #     code to execute for all other cases

is_bmw_listed = ('bmw' in cars)  # NOTE: use this syntax to see if needed car in the list.
print(is_bmw_listed)
print('bmw' in cars)             # NOTE: execute statement TRUE car is there FALSE it is not.
print('==============================================================================')
if ('bmw5' not in cars):  # NOTE: use this syntax to add a new car in list.
    cars.append('bmw5')
print(cars)               # NOTE: then use print syntax to see the added car in list when execute.
print('==============================================================================')
# --------
print()

for car in cars:
    if 'bmwx5' != car.lower():
        print(f"{car} is not bmwx5 ")
    else:
        cars.append('bmwx5')

print(cars)

status = False
if status:
    print('it is true')
else:
    print('it is not true')
print("=======================================================================================")

# # COMMENT: Multiple condition
age = int('25')   # NOTE: if age > 20
states_17 = ['NY', 'CA', 'NC', 'VA', 'CT']
states_16 = ['NJ', 'WA', 'MA', 'TX', 'VT']

for i in range(3):
    print("************* DL check starts *************************")
    age = int(input("Enter your age: "))
    state = input("Enter your state: ").upper()
    if age >= 16 and state in states_16:  # NOTE: True and True >> True.True and False >> False
       print(f'You are eligible to apply for Driving Licence in following states: \n{states_16}')
       print("Available cars in these states: ")
       for car in cars[:2]:
           print(f"\t{car}")

    elif age >= 17 and state in states_17:  # NOTE: True and True >> True
        print(f'You are eligible to apply for Driving Licence in in following states: \n{states_17}')
        print("Available cars in these states: ")
        for car in cars[2:]:
           print(f"\t{car}")

    else:
        # diff = 17 - age
        # print(f'You will be eligible to apply for DL in {diff} years.')
        print(f'You are not eligible to apply for DL yet.')


print("******************** Program ends *******************************")










