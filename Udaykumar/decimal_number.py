# Prompt the user to enter a number and convert it to an integer
num = int(input("enter a number:"))

# Check if the remainder of dividing the number by 10 is greater than 5
if num % 10 > 5:
    # Calculate the difference between 10 and the remainder of num divided by 10
    diff = 10 - num % 10
    # Add the difference to the original number
    num = num + diff
    # Print the modified number
    print(num)

# Check if the remainder of dividing the number by 10 is less than 6
elif num % 10 < 6:
    # Subtract the remainder of num divided by 10 from the original number
    num = num - num % 10
    # Print the modified number
    print(num)

# If neither of the above conditions is true, print "invalid input"
else:
    print("invalid input")

