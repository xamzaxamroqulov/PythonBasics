######08132020_thursday_tuples_examples#######################
coordinates = (234, 432)

print(coordinates[0])
print(coordinates[1])

# coordinates.append(300)
# print(coordinates)  # ERROR: 'tuple' object has no attribute 'append' (means cannot be changed/immutable)

# coordinates.append(300)
# del coordinates[1]          # ERROR: Traceback (most recent call last):
#  File "/Users/macbookhh/dev/PythonBasics/tuples_exampleshh.py", line 11, in <module>
#    del coordinates[1]
# TypeError: 'tuple' object doesn't support item deletion

print(coordinates)
coordinates = (789, 654)
print(coordinates)


for coord in coordinates:
    print(coord)







