# 1. Write a program to remove a given item from the set

my_set = {1, 2, 3, 4, 5}
item = int(input("Enter item to remove: "))

if item in my_set:
    my_set.remove(item)
    print("Updated set:", my_set)
else:
    print("Item not found in the set")



# 2. Write a program to create an intersection of sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)


# 3. Write a program to create an union of sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)
print("Union of sets:", union_set)


# 4. Write a program to find the maximum and minimum value in a set.

my_set = {12, 45, 3, 78, 25}

print("Maximum value:", max(my_set))
print("Minimum value:", min(my_set))
