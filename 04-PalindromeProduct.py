""" https://projecteuler.net/problem=4
Finding the largest palindrome made from the product of two 3-digit numbers """

import sys
def palindromCheck(x):
    """ Recursive function that checks if a list is a palindrome """
    if len(x) < 2:
        return True
    else:
        if x[0] == x[-1]:
            return palindromCheck(x[1:-1])
        else:
            return False

def palindromConv(x):
    """ Checks if a number is a palindrome """
    return palindromCheck(list(str(x)))

largestPalindrome = 0
for x in range(999, 100, -1):
    for y in range(999, x-1, -1):
        if x * y > largestPalindrome:
            if palindromConv(x * y):
                largestPalindrome = x * y
print(largestPalindrome)
