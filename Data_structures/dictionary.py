# 1. Write a program to add a key and value to a dictionary.   
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
print("Updated dictionary:", sample_dict)


# 2. Write a program to concatenate the following dictionaries to create a new one.  
# Sample Dictionary : 
# dic1={1:10, 2:20}  dic2={3:30, 4:40}  dic3={5:50,6:60} 
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {**dic1, **dic2, **dic3}

print("Concatenated dictionary:", result)


# 3. Write a program to check if a given key already exists in a dictionary.
my_dict = {1: 10, 2: 20, 3: 30}
key_to_check = int(input("Enter key to check: "))

if key_to_check in my_dict:
    print(f"Key {key_to_check} exists in dictionary.")
else:
    print(f"Key {key_to_check} does not exist in dictionary.")


# 4. Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.
my_dict = {1: 10, 2: 20, 3: 30}

print("Keys:")
for key in my_dict:
    print(key)

print("Values:")
for value in my_dict.values():
    print(value)

print("Key-Value pairs:")
for key, value in my_dict.items():
    print(key, ":", value)


# 5. Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of the keys.
squares = {}
for i in range(1, 16):
    squares[i] = i * i
print("Dictionary with squares:", squares)


# 6. Write a program to sum all the values in a dictionary, considering the values will be of int type.
my_dict = {1: 10, 2: 20, 3: 30}
total = sum(my_dict.values())
print("Sum of values:", total)
