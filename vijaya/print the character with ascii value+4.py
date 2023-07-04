# Input string
input_string = "cinnamonn"

# Count the occurrences of each character
char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Find the character with the maximum even count
max_even_count = 0
max_even_char = None
for char, count in char_count.items():
    if count % 2 == 0 and count > max_even_count:
        max_even_count = count
        max_even_char = char

# Add 4 to the ASCII value of the character
resulting_ascii = ord(max_even_char) + 4

# Print the character holding the resulting ASCII value
resulting_char = chr(resulting_ascii)
print(resulting_char)
