import string

filename = input("Enter file name: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
  
    line_count = len(lines)

    if line_count <= 12:
        meeting_time = f"{line_count} AM"
    else:
        meeting_time = f"{line_count - 12} PM"

    text = " ".join(lines)
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    meeting_place_word = max(freq, key=freq.get)

    print(f"Meeting time: {meeting_time}")
    print(f"Meeting place: {meeting_place_word.capitalize()} Street")

except FileNotFoundError:
    print("File not found. Please check the file name.")
