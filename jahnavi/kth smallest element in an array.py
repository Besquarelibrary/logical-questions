def find_kth_smallest(arr, k):
    n = len(arr)

    # Implement selection sort algorithm
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # Return the kth smallest element
    return arr[k - 1]


# Example usage
array = [7, 2, 1, 6, 8, 5]
kth_smallest = find_kth_smallest(array, 3)
print(kth_smallest)
