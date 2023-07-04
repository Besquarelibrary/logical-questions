"""
   Find the Missing element in a given array
"""

# implemented the missing_number logic
def missing_number(arr):
    missing_element = []
    maximum = max(arr)
    for i in range(1, maximum+1):
        if i not in arr:
            missing_element += [i]
    print("Missing Element:", missing_element)
        
# calling the missing_number function        
def main():
    missing_number([2, 4, 6, 9, 3, 8])


# call main function
if __name__ == "__main__":
    main()
