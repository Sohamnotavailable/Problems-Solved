"""
Return the list of prime factors of n in non-decreasing
order.
For n < 2, return an empty list.
Examples:
120 -> [2, 2, 2, 3, 5]
97 -> [97]
1 -> []
"""
from typing import List

def prime_factors(n: int) -> List[int]:
    factors = []
    if n < 2:
        return factors
    
    d=2
    temp=n
    while d*d<=temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d+=1
    if temp>1:
        factors.append(temp)
    return factors
