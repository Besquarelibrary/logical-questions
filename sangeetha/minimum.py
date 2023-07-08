# Find the minimum sum value of a given list
lst = [4, 2, 7, 6, 9]
# To store the sum values
new_lst = 0
# To find the length of the given list
length=len(lst)
# Loop will iterate until their is only one element left in the list
while len(lst)>1:
# sorting the list in ascending order
    lst.sort()
# sum of the first two elements
    result=lst[0]+lst[1]
# Adding the result value to the new_lst
    new_lst+= result
# Removing first two elements from the list
    lst=lst[2:]
# Append the values to the list
    lst.append(result)
print(new_lst)

