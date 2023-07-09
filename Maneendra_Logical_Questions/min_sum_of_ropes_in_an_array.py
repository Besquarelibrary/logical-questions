array = [4, 3, 2, 6]

new_array = []


def sorting():
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            # check the elements in an array
            if array[i] > array[j]:
                # swap the numbers
                array[i], array[j] = array[j], array[i]


def minimum_number_of_sum():
    # call the sorting method
    sorting()
    i = 0
    while i < len(array) - 1:
        # sum the current number & next number
        result = array[i] + array[i + 1]
        # remove the current number
        array.pop(i)
        # remove the next number which was originally the number after the current number
        array.pop(i)
        # append the result in array
        array.append(result)
        new_array.append(result)
        # sort the after modification
        sorting()


# call the minimum_number_of_sum()
minimum_number_of_sum()

print(sum(new_list))
