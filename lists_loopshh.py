#########08092020_PYTHON_NOTES################################################
# # CHAPTER 4: Working with LISTS
states = ['New York', 'New Jersey', 'Connecticut', 'California']
# # COMMENT: Loops - within the loops you create repetitive actions

# # SYNTAX:FOR variable IN list_of_elements:
#    repetitive code here

# for state in states:
#    print(f"Welcome to {state}!!")
#    print(f"Welcome to {state}!!")
# # COMMENT:pass # do nothing

# # COMMENT: Things to Remember while working with LOOPS
# # COMMENT: colon at the end of 'for' line
# # COMMENT: 'in' in the 'for' line
# # COMMENT: give any name to a variable and use that variable inside the for loop code
# # COMMENT: all  lines of code that belong to for loop (repetitive code) must be indented (4 spaces)
# # COMMENT: Always check your indentation meaning (space 4 times before print) when use 'for' loop

# # COMMENT: states >> 4 members >>
#    >> 1st loop/round >> state = 'New York'  -- python does this
#    >> print(f"Welcome to {state}!!")        -- we will write this code
#    >>> Welcome to New York!!                -- this is execution

#    >> 2nd loop/round >> state = 'New Jersey'
#    >> print(f"Welcome to {state}!!")
#    >>> Welcome to Jersey!!

#     >> 3rd loop/round >> state = 'Connecticut'
#     >> print(f"Welcome to {state}!!")  --- this code we will write
#     >>> Welcome to Connecticut!!




print(states)
# # COMMENT: PyCharm: refactoring >> Shift + f6


# print(state)  # NOTE: outside of the scope of variable
# # COMMENT: SCOPE
for state in states:
    print(f"Welcome to {state.upper()}!!")

print("Enjoy your trip!!")  # NOTE: outside of loop, independent from loop
print(state)  # NOTE: Incorrect: outside of variable
print('====================================================================================')
####
# # COMMENT:TIY 4-1 Pizza exercise
# # COMMENT: TIY: TRY IT YOURSELF 4-1. Pizzas: Think of at least three kinds of your favorite pizza
# Store these pizza names in a list, and then use a for loop to print the name of each pizza .
# • Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza.
# For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
# • Add a line at the end of your program, outside the for loop, that states how much you like pizza.
# The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
pizzas = ['pepperoni', 'four cheese', 'salami', 'mashrooms']
for pizza in pizzas:
     print(f"I really love {pizza}!")
print("====================================================================================")


print()
pizzas = ["cheese", "artichoke", "mashroom"]
for pizza in pizzas:
     print(pizza)
     print(f"I like this type of pizza {pizza}!!!")
print("I really love pizza")
print("====================================================================================")
####

# # COMMENT: HW TIY 4-2


# # COMMENT: Making Numerical List
for num in range(5): # NOTE: from 0 to 4
    print(f"My current number from range(5): {num}")
print()


for num in range(3, 6): # NOTE: from 3 to 5
    print(f"My current number from range(3, 6): {num}")
print()
# # COMMENT: list(iterable) - mutable >> [4, 6, 12]
# # COMMENT: tuple - mutable >> (4, 6, 12) - immutable


friends = list()
students = []


numbers = list(range(5)) # NOTE: #1.Range >> 0, 1, 2, 3, 4  #2.List() >> [0, 1, 2, 3, 4] #3. Numbers = [0, 1, 2, 3, 4]
print(numbers)


# # COMMENT: Print squares of numbers from 5 to 12
squares = []  # squares = list()
for num in range(5, 13):
    num_sqr = num ** 2
    # squares.insert(-1, num_sqr)
    squares.append(num_sqr)
    squares.append(num**2)
    # print(num_sqr)
    # print(squares)
print(squares)

squares = list()  # NOTE: resetting list to empty list
for num in range(5, 13):
    squares.append(num ** 2)
print(squares)
print("=================================================================================")

nums = [5, 78, 456, 127, 230, 6, 5]
# # COMMENT: min(list) , max(list), sum(list)
print(f"Min number from numbers :{min(nums)}")
print(f"Max number from numbers :{max(nums)}")
print(f"Sum number from numbers :{sum(nums)}")

# # COMMENT: List comprehension

squares = []
for num in range(5, 14, 2):
    squares.append(num ** 2)


# # COMMENT: FYI
# squares = list(num ** 2 for num in range(5, 14))
squares = [num ** 2 for num in range(5, 14, 2)]
print(squares)
print("===================================================================================")

# # COMMENT: TRY IT YOURSELF: TIY 4-5: Summing a Million:
# Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and ends at one million .
# Also, use the sum() function to see how quickly Python can add a million numbers .

print("# TIY 4-5")
# for num in range(1, 1000001):
#     pass
#     # code to create a list
# print(min(num))
# print(max(num))
# print(sum(num))
# print(sum(num) / len(num))

nums = list(range(1, 1000001))
print(f"Min number is: {min(nums)}")
print(f"Max number is: {max(nums)}")
print(f"Sum number is: {sum(nums)}")
print("==================================================================================")



# # COMMENT: HW 4-6, 4-7, 4-8, 4-9
# # COMMENT: Slicing the list
name = "John Doe"
print(name[5:])  # NOTE: >>> Doe
print("=========================================")


numbers = [5, 78, 456, 127, 230, 6, 5]
print(numbers[:3])  # NOTE: indexes >> 0, 1, 2.
print(numbers[0:3])

print(numbers[3:])   # NOTE: from 3rd index to end of the list.
print(numbers[1:-2])  # NOTE: from 1st index(second element) to third from the end.

new_numbers = numbers   # NOTE: this is linking the numbers_copy to numbers list.
# NOTE: if numbers is modified numbers_copy will effected.
numbers_copy = numbers[:]  # NOTE: copying the list to a new list.

print("# copying the lists example")
print(numbers, new_numbers, numbers_copy)
numbers.append(5555)
print(numbers, new_numbers, numbers_copy)

for num in numbers[3:]:
    print(num)

print('========================================================')


# # COMMENTS: HW 4 - 2
# HW 4-6, 4 - 7, 4 - 8, 4 - 9
# HW 4-10, 4-11, 4-12


add_numbers = [1, 25, 350, 550, 750, 1000000]
print(f"Min number from numbers :{min(add_numbers)}")
print(f"Max number from numbers :{max(add_numbers)}")
# why when you use (max function) python see last number?
print(f"Sum number from numbers :{sum(add_numbers)}")


