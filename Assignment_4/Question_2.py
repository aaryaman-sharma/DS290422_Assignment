# Write a Python program to triple all numbers of a given list of integers. Use Python map.


# sample list: [1, 2, 3, 4, 5, 6, 7]

# Triple of list numbers:

# [3, 6, 9, 12, 15, 18, 21]

# <------ Solutions ------->

lst1 = [1, 2, 3, 4, 5, 6, 7] 
print("Sample list: ", lst1)

result = map(lambda x: x + x + x, lst1) 

print("\nTriple of list numbers:")

print(list(result))