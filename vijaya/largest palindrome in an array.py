def isPalindrome(n):
    divisor = 1
    while (n / divisor >= 10):
        divisor *= 10
    while (n != 0):
        leading = n // divisor
        trailing = n % 10
        if (leading != trailing):
            return False

        # Removing the leading and trailing
        # digits from the number
        n = (n % divisor) // 10

        # Reducing divisor by a factor
        # of 2 as 2 digits are dropped
        divisor = divisor // 100

    return True


def largestPalindrome(A, n):

    # Sort the array
    A.sort()

    for i in range(n - 1, -1, -1):

        # If number is palindrome
        if (isPalindrome(A[i])):
            return A[i]

    # If no palindromic number found
    return -1


if __name__ == "__main__":

    A = [1, 232, 54545, 999991]
    n = len(A)

    # print required answer
    print(largestPalindrome(A, n))
