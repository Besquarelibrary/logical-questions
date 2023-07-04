array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialize variables for even sum and odd sum
even_sum = 0
odd_sum = 0

# Iterate over each element in the array
for num in array:
    # Check if the element is even
    if num % 2 == 0:
        # Add the even element to the even sum
        even_sum += num
    else:
        # Add the odd element to the odd sum
        odd_sum += num

# Find the maximum sum between even sum and odd sum
max_sum = max(even_sum, odd_sum)

# Print the maximum sum
print("Maximum sum:", max_sum)
