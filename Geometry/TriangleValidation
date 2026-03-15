"""
Return True if the three sides can form a triangle.
Condition: the sum of any two sides must be greater than
the third.
"""
import math

def isValid(side1: float, side2: float, side3: float) -> bool:

    return (side1 + side2 > side3) and \
           (side1 + side3 > side2) and \
           (side2 + side3 > side1)


def area(side1: float, side2: float, side3: float) -> float:

    if not isValid(side1, side2, side3):
        raise ValueError
    
    s = (side1 + side2 + side3) / 2
    return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
