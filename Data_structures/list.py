# 1. Write a program to create a list of 5 integers and display the list items. Access individual elements through index.
def createAndDisplay():
    ls = []
    for i in range(5):
        num = int(input(f"Enter integer {i+1}: "))
        ls.append(num)

    print("List of integers:", ls)

    for i in range(len(ls)):
        print(f"Element at index {i}: {ls[i]}")


# 2. Write a program to append a new item to the end of the list
