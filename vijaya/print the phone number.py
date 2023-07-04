def print_phone_keyboard_pattern(string):
    # Define the phone keyboard mapping
    keyboard_mapping = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
    }

    # Convert the string to uppercase
    string = string.upper()

    # Iterate over each character in the string
    for char in string:
        # Check if the character is a letter
        if 'A' <= char <= 'Z':
            # Print the corresponding phone keyboard integer
            print(keyboard_mapping[char], end='')
        else:
            # Print the character as is
            print(char, end='')


input_string = "Jahnavi"
print_phone_keyboard_pattern(input_string)
