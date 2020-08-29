##08022020_PYTHON_NOTES_HH################################
# # COMMENT: IDE - Integrated Development Environment
# # COMMENT: Java - Eclipse, IntellijIdea
# # COMMENT: Python - VScode, PyCharm, VIM
#   CHAPTER 3 : INTRODUCTION TO LISTS
# print("Hello World!!")
####
# # Todo: introduction to list data structure
# # Todo: creating a list
# students = ['john', 'mark', 'aziz', 'feruza', 105]
# # COMMENT: Varname assign [0, 1,        2,       3   , 4 ]
# print(students)
# print(students[2])
####
# # Todo: accessing the elements in the list
# # COMMENT: Lists hold values by index, index start with 0
# print(students[0])  # NOTE: prints the 1st element in the list
# print(students[3])  # NOTE: 'feruza' to be printed
####
# # COMMENT: Reformat the file based on PEP8 rules >> CTRL + ALT + L
####
# # COMMENT: Data structures: lists, tuples, dictionaries (HashMap, Hashset..)
# # COMMENT: Create, access the elements, modify, remove element from Data structure, organize
# print(f"Hello, {students[1].title()}! Thank you for coming.")
# print(f"Hello, {students[4]}! Thank you for coming.")
# print("Hello, " + str(students[4]) + "! Thank you for coming.")
####
# # TRY IT YOURSELF : TIY 3-3. create cars list, print different message for each car
####
# cars = ['bmw', 'mercedes', 'ferrari', 'tesla']
# print(f"My first car was {cars[0]}.Then few years later i leased {cars[1]}.But my dream car was always {cars[2]}.Cars like {cars[3]} was never my type.")
# print("================================================================================")
# cars = ['bmw', 'nissan', 'mazda', 'honda']
# print(f"I would travel on {cars[0]}")
# print("================================================================================")
# cars = ['Honda', 'Volvo', 'BMW']
# print(f"Hello Mark! would you like to drive {cars[0]} or {cars[1]} or {cars[2]}")
# print("================================================================================")
# car = ['honda', 'toyota', 'ford']
# print(f"I would like to own a " + str(car[2]) + " car")
# print("================================================================================")
####
# # COMMENT: MODIFY LISTS
cars = ['bmw', 'nissan', 'mazda', 'honda']
print(f"before: {cars}")
cars[2] = 'tesla'
print(f"after: {cars}")  # NOTE: in this case car #2(mazda) in list was replaces with tesla
print("==================================================================================")
####
# # COMMENT: ADDING ELEMENT
# # Appending
cars.append('lexus')
print(cars)  # NOTE: lexus car in this case ADDED to end of the list
print("==================================================================================")
####
# # COMMENT: INSERTING
cars.insert(2, 'toyota')
print(cars)  # NOTE:  INSERT toyota as car #2 in car list.Other objects moved to left.Nothing lost.
print("==================================================================================")
####
# # COMMENT: REMOVE FROM THE LIST
# # COMMENT: DELETE BY INDEX
print(cars[5])
del cars[4]
print(f"after del {cars}")
# print(cars[5])  # NOTE: You will get >> IndexError: list index out of range.
# # COMMENT: To COMMENT the line where your cursor is >> COMMAND + / or CTRL + /

cars.pop()  # NOTE: returns the value that is being removed
print(f"after pop: {cars}")

cars.pop(2)
print(f"after pop(2): {cars}")

# # COMMENT: DELETE BY VALUE
cars.remove('nissan')
print(f"after remove {cars}")
print("==================================================================================")
####
# # TRY IT YOURSELF: TIY 3-4 and 3-5
# # COMMENT: Print(f"welcome to the dinner {guests[0]}").
# Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite?
# Make a list that includes at least three people you’d like to invite to dinner.
# Then use your list to print a message to each person, inviting them to dinner.
# 3-4
print("============================ TIY 3 - 4 ========================================")
guests = ['D.Trump', 'Putin', 'Messi', 'CRonaldo', 'Alex Morgan']
print(f"welcome to the dinner {guests[0]}!")
print(f"welcome to the dinner {guests[1]}!")
print(f"welcome to the dinner {guests[2]}!")
print(f"welcome to the dinner {guests[3]}!")
print(f"welcome to the dinner {guests[4]}!")
print("=================================================================================")
##
# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who #is still
# in your list.
# 'M.Sharapova'
guests_not_coming = []
guests_not_coming.append(guests[0])
guests[0] = 'M.Sharapova'  # NOTE: here put the name of a guest you replacing with.

print("================= 3-5 =========================")
print(f"{guests[4]} sorry to hear that, please come next time.")  # NOTE: here put the number of guest who not coming.
print(f"Guests are coming: {guests}")
print(f"Guests are NOT coming: {guests_not_coming}")
print(f"welcome to the dinner {guests[0]}!")
print(f"welcome to the dinner {guests[1]}!")
print(f"welcome to the dinner {guests[2]}!")
print(f"welcome to the dinner {guests[3]}!")
print(f"welcome to the dinner {guests[4]}!")
print('===============================================================================')
####
# # COMMENT: HomeWork (TIY: 3 -6, 3 - 7)
# # COMMENT: Organazing your list.
# # COMMENT: Temporary and permenant sorting.
print('===============================================================================')
print(sorted(guests))  # NOTE: temp sorting, sorted() works for some other data structure.
sorted_guests = sorted(guests) # NOTE: sorted() - returns you the copy of the list but sorted in asc.
print(sorted_guests)
print(guests)  # NOTE: do  not effects original list.

guests.reverse()
print(f"Reversing the list: {guests}")  # NOTE: changing the list in reversed order.


guests.sort() # NOTE; only works for list.Does not return anything,just effects the original list.
print(f"Perm sorting with list.sort(): {guests}")
guests.sort(reverse=True)
print(f"Perm reverse (desc) sorting with list.sort() : {guests}")
print('===============================================================================')

####
# list.reverse() - reverses but not desc order
# list.sort(reverse=True) - sorts in desc order
print()
nums = [4, -10, 9, 5, 6, 1, 0, 44]
print(nums)
nums.reverse()
print(nums)
nums.sort(reverse=True)
print(nums)
# nums[8] = 100  # NOTE: IndexError: list assignment index out of range
nums.insert(8, 100)
print(nums)
print('===============================================================================')


print()
print(f"Number of elements in my 'nums' list :{len(nums)}")
num_elements = len(nums)
print(nums[-1])
print(nums[-5])
print(nums[-10]) # IndexError: list index out of range
print('===============================================================================')


# # COMMENT: All you need to know about the LIST
# # COMMENT: list_name = [] - creating an empty list
# # COMMENT: list.append(newValue)
# # COMMENT: list.insert(ind, value)
# # COMMENT: del list[ind]
# # COMMENT: list.remove(value)
# # COMMENT: list.pop() - removes and returns the last element, list.pop(ind)
# # COMMENT: list[ind] = value  - assigning a new value to existing Index
# # COMMENT: list.sort(), list.sort(reverse=True)
# # COMMENT: sorted(list) -  copies the list and returns sorted copy of the list
# # COMMENT: list.reverse()
# # COMMENT: len(list) - returns the length of your list (how big is list, i.e. number of elements)
# # COMMENT: list[-n] - index start from the end of the list, last element is list[-1]


# HW: 3-6, 3-7
# HW TIY 3-8