# 1. Write a program to count the number of upper and lower case letters in a String.
string = input("Enter a string: ")
upper = 0
lower = 0

for ch in string:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")


# 2. Write a program that will check whether a given String is Palindrome or not.
string = input("Enter a string: ")

if string == string[::-1]:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")


# 3. Given a string, return a new string made of n copies of the first 2 chars of the 
# original string where n is the length of the string. The string length will be >=2. 
# If input is "Wipro" then output should be "WiWiWiWiWi".
string = input("Enter a string: ")

n = len(string)
new_string = string[:2] * n
print(new_string)


# 4. Given a string, if the first or last character is 'x', return the string without 
# those 'x' character, else return the string unchanged. If the input is "xHix", then output is "Hi".
string = input("Enter a string: ")

if string.startswith('x'):
    string = string[1:]
if string.endswith('x'):
    string = string[:-1]

print(string)


# 5. Given a string and an integer n, return a string made of n repetitions of the last n 
# characters of the string. You may assume that n is between 0 and the length of the string 
# inclusive. 
# For example if the inputs are “Wipro” and 3, then the output should be “propropro”.
string = input("Enter a string: ")
n = int(input("Enter n: "))

last_part = string[-n:]
result = last_part * n
print(result)

