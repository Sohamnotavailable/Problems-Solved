"""
Return the area of a regular n-sided polygon whose sides
have
length ’side’.
Formula:
(n * side**2) / (4 * tan(pi / n))
For n < 3, raise ValueError.
"""
import math

def area_polygon(n: int, side: float) -> float:

    if n<3:
        raise ValueError
    
    return (n*(side**2))/(4*math.tan(math.pi/n))
