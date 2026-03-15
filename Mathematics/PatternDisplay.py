"""
Return the pattern:
1
2 1
3 2 1
...
n n-1 ... 2 1
Each row is one string in the returned list.
For n <= 0, return [].
"""
from typing import List

def displayPattern(n: int) -> List[str]:
    result = []
    if n<=0:
        return result
    
    for i in range(1, n+1):
        row_nums = []
        for j in range(i, 0, -1):
            row_nums.append(str(j))
        result.append(" ".join(row_nums))
    return result
