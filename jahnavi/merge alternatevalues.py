array1 = [1, 3, 5]
array2 = [2, 4, 6, 8, 10]

# Initialize variables
merged_array = []
index1 = 0
index2 = 0

# Iterate until both arrays are exhausted
while index1 < len(array1) or index2 < len(array2):
    # Check if there are remaining elements in array1
    if index1 < len(array1):
        merged_array.append(array1[index1])
        index1 += 1

    # Check if there are remaining elements in array2
    if index2 < len(array2):
        merged_array.append(array2[index2])
        index2 += 1

# Print the merged array
print("Merged array:", merged_array)
