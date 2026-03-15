"""
Calculates the sum of all digits in a given integer.
e.g., for 123, the sum is 1 + 2 + 3 = 6.
"""
import math
def sum_of_digits(n):
    s=str(n)
    total=0
    for digit_char in s:
        total+=int(digit_char)
    print(total)
    return total
sum_of_digits(123)
sum_of_digits(405)
sum_of_digits(99)
