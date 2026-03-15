"""
Given three sides a, b, c, calculates the three angles
A, B, C of the triangle. Each angle should be rounded
up to the next integer (’ceil’).
Returns a tuple (angleA, angleB, angleC).
"""
import math
def calculate_angles(a, b, c):
    if a+b<c or a+c<b or b+c<a:
        return "Not a valid triange"
    cosA=(b*b+c*c-a*a)/(2*b*c)
    cosB=(c*c+a*a-b*b)/(2*a*c)
    cosC=(a*a+b*b-c*c)/(2*a*b)
    A=math.acos(cosA)
    B=math.acos(cosB)
    C=math.acos(cosC)
    A=math.degrees(A)
    B=math.degrees(B)
    C=math.degrees(C)
    return (math.floor(A),math.floor(B),math.floor(C))
print(calculate_angles(3,4,5))
print(calculate_angles(3,3,3))
print(calculate_angles(1,1,3))
