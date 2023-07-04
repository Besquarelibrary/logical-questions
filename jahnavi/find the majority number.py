def findMajority(arr, size):
    m = {}
    for i in range(size):
        if arr[i] in m:
            m[arr[i]] += 1
        else:
            m[arr[i]] = 1
    is_majority_present = False
    for key in m:
        if m[key] > size / 2:
            is_majority_present = True
            print("Majority found :-", key)
            break
    if not is_majority_present:
        print("No Majority element")


arr = [2, 2, 2, 2, 5, 5, 3, 3, 3, 3, 3, 3, 3]
n = len(arr)
findMajority(arr, n)
