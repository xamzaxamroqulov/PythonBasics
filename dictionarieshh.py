### 08/15/2020_DICTIONARIES ####
# COMMENT: DICTIONARIES - Data structure , mutable, {key1: value1, key2: value }
 # in java > Hashmap, Hashtable, Hashset >> hashing algorithm to store the
       # key-value pairs
# COMMENT: RECAP: LIST - Data structure , mutable, [a, b]
cars = ['lexus', 'bugatti', 'bmw', 'ferrari']
# COMMENT: RECAP: TUPLE - Data structure, immutable, (a, b)
cars = ('lexus', 'bugatti', 'bmw', 'ferrari')
print("=========================================================================")

# COMMENT: STORES THE VALUE AS KEY-VALUE PAIR
# COMMENT: Must Know:
# COMMENT: Create, access, modify ( add element, remove elements, reset ), loop through elements.
students = {}  # NOTE: Empty dictionary
students1 = dict()  # NOTE: Creates Empty dictionary, converts to a dictionary
print("=========================================================================")


student1 = {'name': 'Hamza', 'gpa': 3.8}
student2 = {'name': 'Alexa', 'gpa': 3.9}
# COMMENT: Accessing the values of Dictionary, as in list with >> cars[0]
print(student1)
print(student1['name'], student1['gpa'])
print(f"Next student is {student2['name']} with GPA = {student2['gpa']}")
print("=========================================================================")


# COMMENT: Assigning the value
student1['gpa'] = 3.7  # NOTE: if key is existing this will reset the value, new gpa=3.7
print(student1)
student1['state'] = 'NY'  # NOTE: if key does not exist, then it will create new key-value pair
print(student1)
print(sorted(student1))  # NOTE: only sorted keys are printed as a list


del student1['state']
print(student1)

# dict(object)
# int('3')
# str(6)
# num_list = list(range(10))  # comment: in sql converting the data type >> bdate >> birthday is : 02-29-1998" >> CAST(),CONVERT()
# str_input = int(input())
#
# for var in iterable:
#     var = var * 2  # repetitive code
#     print("I belong to for loop")
# print("I dont know For loop")
#
# [2, 4]
# {'key':'value'}






