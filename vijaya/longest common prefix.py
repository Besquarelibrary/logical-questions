def longest_common_prefix(arr):
    # Check if the array is empty
    if len(arr) == 0:
        return ""

    # Get the minimum length among the array elements
    min_length = min(len(s) for s in arr)

    # Iterate over the characters in the first element
    for i in range(min_length):
        char = arr[0][i]

        # Check if the character is the same in all elements
        for j in range(1, len(arr)):
            if arr[j][i] != char:
                return arr[0][:i]

    # If all characters match, return the first element
    return arr[0]


array = ["flower", "flow", "flight"]
common_prefix = longest_common_prefix(array)
print(common_prefix)
