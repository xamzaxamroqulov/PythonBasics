##08132020thursday_class####
print('Exercises Chapter3-4')
print("=================================================================================")
# # COMMENT: CHAPTER 3
print('Chapter_3')


friends = ['mark', 'john', 'jane', 400, 500]
print(friends[-1])


for b in friends:
    print(b)

# num_elements = len(friends)
# for i in range(num_elements):  # NOTE: using the index
for i in range(len(friends)):  # NOTE: using the index >> this means range
    print(f"element on index {i} is {friends[i]}")

print(i)

friend = 'anthony'
for i in friend:
    print(i)
print("============================================================================")
# --------------------------------

"""
TIY 3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""

guests = ['mark', 'john', 'jane']

print(guests)
guests.insert(0, 'David Guetta')   # NOTE: insert(index, value)
print(guests)
guests.insert(2, 'Filipp Kirkorov')
print(guests)
guests.append('Maria Kerry')
print(f"Final guests: {guests}")
print(f"We have now more space and {guests[0]} we are still waiting you for dinner!")\

print("==========================================================================")

# # TRY IT YOURSELF: TIY 3-8. Seeing the World: Think of at least five places in the world you’d like to visit .
# • Store the locations in a list . Make sure the list is not in alphabetical order .
# • Print your list in its original order.
#   Don’t worry about printing the list neatly, just print it as a raw Python list .
# • Use sorted() to print your list in alphabetical order without modifying the actual list .
# • Show that your list is still in its original order by printing it .
# • Use sorted() to print your list in reverse alphabetical order without chang- ing the order of the original list .
# • Show that your list is still in its original order by printing it again .
# • Use reverse() to change the order of your list . Print the list to show that its order has changed .
# • Use reverse() to change the order of your list again . Print the list to show it’s back to its original order .
# • Use sort() to change your list so it’s stored in alphabetical order.
#   Print the list to show that its order has been changed .
# • Use sort() to change your list so it’s stored in reverse alphabetical order.
#   Print the list to show that its order has changed .

print("# TIY 3-8 ======================== ")
dream_places = ['Belarus', 'London', 'Bali', 'Australia', 'Italy']
print(dream_places)
print('========')

print(sorted(dream_places))
print(dream_places)
print('========')

print(sorted(dream_places, reverse=True))
print(dream_places)
print('========')

dream_places.reverse()  # reverse() puts your list in reverse order, not desc order
print(dream_places)
print('========')

dream_places.sort()  # sort() order your list in ASC order
print(dream_places)
print('=========')

dream_places.sort(reverse=True)  # sort() order your list in DESC order
print(dream_places)
print('============================================================================')












