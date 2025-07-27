# 1. Write a program to read the entire content from a txt file and display it to the user.

def readContent():
    filename = input("Enter file name: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError:
        print("File not found. Please check the file name.")

readContent()

# 2.Write a program to read first n lines from a txt file. Get n as user input.

def readNLines():
    filename = input("Enter file name: ")
    n = int(input("Enter number of lines to read: "))

    try:
        with open(filename, 'r') as file:
            for i in range(n):
                line = file.readline()
                if not line:
                    break
                print(line, end="")
    except FileNotFoundError:
        print("File not found. Please check the file name.")

readNLines()

# 3.Write a program to accept input from user and append it to a txt file.

def acceptInput():
    filename = input("Enter file name: ")
    text_to_append = input("Enter text to append: ")

    with open(filename, 'a') as file:
        file.write(text_to_append + "\n")

    print("Text appended successfully.")

acceptInput()

# 4.Write a program to read contents from a txt file line by line and store each line into a list.

def storeList():
    filename = input("Enter file name: ")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        lines = [line.strip() for line in lines]
        print("Lines in list:", lines)

    except FileNotFoundError:
        print("File not found. Please check the file name.")

storeList()

# 5.write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.

def longestWordSearch():
    filename = input("Enter file name: ")

    try:
        with open(filename, 'r') as file:
            words = file.read().split()

        longest = max(words, key=len)
        print("Longest word:", longest)

    except FileNotFoundError:
        print("File not found. Please check the file name.")

longestWordSearch()

# 6.Write a program to count the frequency of a user entered word in a txt file.

def countFreq():
    filename = input("Enter file name: ")
    word_to_search = input("Enter word to search: ")

    try:
        with open(filename, 'r') as file:
            content = file.read().split()

        frequency = content.count(word_to_search)
        print(f"Frequency of '{word_to_search}' is: {frequency}")

    except FileNotFoundError:
        print("File not found. Please check the file name.")

countFreq()