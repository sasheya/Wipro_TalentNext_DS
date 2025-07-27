# 1. Write a program to print the 4th element from first and 4th element from last in a tuple.
# Program 1
tup = (10, 20, 30, 40, 50, 60, 70, 80)

print("4th element from first:", tup[3])
print("4th element from last:", tup[-4])

# 2. Write a program to check whether an element exists in a tuple or not.
tup = (10, 20, 30, 40, 50)
element = int(input("Enter element to check: "))

if element in tup:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")

# 3. Write a program to convert a list into a tuple.
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print("Tuple:", my_tuple)

# 4. Write a program to find the index of an item in a tuple.
tup = (10, 20, 30, 40, 50)
element = int(input("Enter element to find index: "))

if element in tup:
    print("Index of element:", tup.index(element))
else:
    print("Element not found in tuple.")

# 5. Write a program to replace last value of tuples in a list to 100.  
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
data = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# Replace last element of each tuple with 100
updated_data = [t[:-1] + (100,) for t in data]

print("Updated list of tuples:", updated_data)
