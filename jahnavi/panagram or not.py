def is_pangram(string):
    # Create a set to keep track of the unique characters
    unique_chars = set()

    # Convert the string to lowercase
    string = string.lower()

    # Iterate over each character in the string
    for char in string:
        # Check if the character is an alphabet
        if 'a' <= char <= 'z':
            # Add the character to the set
            unique_chars.add(char)

    # Check if the length of the set is equal to 26
    if len(unique_chars) == 26:
        return True
    else:
        return False


def find_missing_chars(string):
    # Create a set with all the alphabets
    all_chars = set(chr(i) for i in range(ord('a'), ord('z') + 1))

    # Convert the string to lowercase
    string = string.lower()

    # Iterate over each character in the string
    for char in string:
        # Check if the character is an alphabet
        if 'a' <= char <= 'z':
            # Remove the character from the set
            all_chars.discard(char)

    # Return the missing characters as a sorted string
    missing_chars = ''.join(sorted(all_chars))
    return missing_chars


input_string = "The quick brown fox jumps over the lazy dog"
if is_pangram(input_string):
    print("The given string is a pangram")
else:
    missing_chars = find_missing_chars(input_string)
    print("The given string is not a pangram")
    print("Missing characters:", missing_chars)
