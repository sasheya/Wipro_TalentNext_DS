# 1. Sort the colors

def sort_colors(color_sequence):
    color_sequence = input("Enter hyphen-separated colors: ")
    colors = color_sequence.split('-')
    colors.sort()

    return '-'.join(colors)

print(sort_colors())


# 2. Playing with names

import string_utils
name = input("Enter a name: ")

print(string_utils.ispalindrome(name))
print(string_utils.count_the_vowels(name))
print(string_utils.frequency_of_letters(name))

