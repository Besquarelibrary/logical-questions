# To find a number which is repeated many times in a given list.
def findMajority(arr, size):
    # To store and count the repeated values.
    m = {}
    for i in range(size):
        # If arr[i] is in m then increment the value.
        if arr[i] in m:
            m[arr[i]] += 1
        else:
            m[arr[i]] = 1
    # checking if the count of the value is more than the half of the length of the array
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
