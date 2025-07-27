
def ispalindrome(name):
    if name == name[::-1]:
        return "Yes it is a palindrome."
    else:
        return "No it is not a palindrome."

def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = sum(1 for ch in name if ch in vowels)
    return f"No of vowels: {count}"

def frequency_of_letters(name):
    freq = {}
    for ch in name:
        freq[ch] = freq.get(ch, 0) + 1
    formatted = ", ".join(f"{k}-{v}" for k, v in freq.items())
    return f"Frequency of letters: {formatted}"
