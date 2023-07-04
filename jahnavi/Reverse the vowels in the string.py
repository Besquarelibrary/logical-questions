string = "Good Morning"

# Convert the string to a list for easy modification
string_list = list(string)

# Define the vowels
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# Initialize two pointers
left = 0
right = len(string_list) - 1

# Iterate over the string from both ends
while left < right:
    # Check if the characters at both pointers are vowels
    if string_list[left] in vowels and string_list[right] in vowels:
        # Swap the vowels
        string_list[left], string_list[right] = string_list[right], string_list[left]
        # Move the pointers
        left += 1
        right -= 1
    else:
        # Move the left pointer if the character at the left is not a vowel
        if string_list[left] not in vowels:
            left += 1
        # Move the right pointer if the character at the right is not a vowel
        if string_list[right] not in vowels:
            right -= 1

# Convert the modified list back to a string
reversed_vowels_string = ''.join(string_list)

# Print the string with reversed vowels
print("String with reversed vowels:", reversed_vowels_string)
