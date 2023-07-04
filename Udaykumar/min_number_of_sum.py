# Define a list of numbers
my_list = [4, 3, 2, 6]

# Initialize an empty list
new_list = []

def sorting():
    """
    Sorts the my_list in ascending order using bubble sort algorithm.
    """
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            # If the current number is greater than the next number
            if my_list[i] > my_list[j]:
                # Swap the numbers
                my_list[i], my_list[j] = my_list[j], my_list[i]

def minimum_number_of_sum():
    """
    Calculates the sum of minimum numbers by repeatedly summing pairs of adjacent numbers.
    """
    # Sort the my_list
    sorting()
    # Initialize the loop variable
    i = 0
    # Iterate until the second last element of the list
    while i < len(my_list) - 1:
        # Sum the current number and the next number
        result = my_list[i] + my_list[i+1]
        # Remove the current number
        my_list.pop(i)
        # Remove the next number (which was originally the number after the current number)
        my_list.pop(i)
        # Append the sum to the end of the list
        my_list.append(result)
        # Add the sum to the new_list
        new_list.append(result)
        # Sort the my_list after the modification
        sorting()
        # Note: The loop will repeat until the second last element due to the condition i < len(my_list) - 1
        #       This ensures that my_list[i+1] is a valid index.

# Execute the function
minimum_number_of_sum()

# Output the sum of the numbers in new_list
print(sum(new_list))



