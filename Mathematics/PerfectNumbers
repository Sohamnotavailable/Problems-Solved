"""
Return True if n is a perfect number (sum of proper
divisors equals n),
else False. Assume n >= 1. Note: 1 is not perfect.
"""
from typing import List

def is_perfect(n: int) -> bool:

    if n<=1:
        return False
    total = 0
    for i in range(1, n//2+1):
        if n%i==0:
            total+=i
    return total==n


def perfects_up_to(limit: int) -> List[int]:

    result = []
    for i in range(1, limit+1):
        if is_perfect(i):
            result.append(i)
    return result
