# Write a Python program to square the elements of a list using map() function.


# Sample List: [4, 5, 2, 9]

# Square the elements of the list:

# [16, 25, 4, 81]

# <----- Solutions ------>

def square_num(n):
  return n * n
  
lst1 = [4, 5, 2, 9]

print("Original List: ",lst1)
result = map(square_num, lst1)
print("Square the elements of the list:")
print(list(result))