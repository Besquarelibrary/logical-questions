my_str = "udaykumar"  # Define a string

new_str = ""  # Initialize an empty string to store the characters that appear exactly twice

for ele in my_str:  # Iterate over each character in the string
    if my_str.count(ele) == 2:  # Check if the character appears exactly twice in the string
        new_str = new_str + ele  # Add the character to the new string

print(new_str)  # Output the new string containing the characters that appear exactly twice

