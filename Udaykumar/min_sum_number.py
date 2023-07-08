my_list = [4, 3, 2, 6]  # Define a list of numbers

new_list = []  # Initialize an empty list

def sorting():
    """
    Sorts the my_list in ascending order using bubble sort algorithm.
    """
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] > my_list[j]:  # If the current number is greater than the next number
                my_list[i], my_list[j] = my_list[j], my_list[i]  # Swap the numbers

def minimum_number_of_sum():
    """
    Calculates the sum of minimum numbers by repeatedly summing pairs of adjacent numbers.
    """
    sorting()  # Sort the my_list
    i = 0  # Initialize the loop variable
    while i < len(my_list) - 1:  # Iterate until the second last element of the list
        result = my_list[i] + my_list[i+1]  # Sum the current number and the next number
        my_list.pop(i)  # Remove the current number
        my_list.pop(i)  # Remove the next number (which was originally the number after the current number)
        my_list.append(result)  # Append the sum to the end of the list
        new_list.append(result)  # Add the sum to the new_list
        sorting()  # Sort the my_list after the modification
        # Note: The loop will repeat until the second last element due to the condition i < len(my_list) - 1
        #       This ensures that my_list[i+1] is a valid index.

minimum_number_of_sum()  # Execute the function

print(sum(new_list))  # Output the sum of the numbers in new_list

