numbers = [48, 60]

# Find the minimum number among the given numbers
min_number = min(numbers)

# Initialize variables for the H.C.F
hcf = 1

# Iterate from 1 to the minimum number
for i in range(1, min_number + 1):
    # Check if the current number divides all given numbers
    if all(num % i == 0 for num in numbers):
        # Update the H.C.F
        hcf = i

# Print the H.C.F
print("H.C.F:", hcf)
