"""
Return True if the 2D list ’values’ contains four equal
numbers in a row
horizontally, vertically, or diagonally. Otherwise return
False.
"""
from typing import List

def isConsecutiveFour(values: List[List[int]]) -> bool:
    rows = len(values)
    if rows == 0:
        return False
    cols = len(values[0])
    
    for r in range(rows):
        for c in range(cols):
            val = values[r][c]
            
            if c + 3 < cols:
                if (val == values[r][c+1] == values[r][c+2] == values[r][c+3]):
                    return True
            
            if r + 3 < rows:
                if (val == values[r+1][c] == values[r+2][c] == values[r+3][c]):
                    return True
            
            if r + 3 < rows and c + 3 < cols:
                if (val == values[r+1][c+1] == values[r+2][c+2] == values[r+3][c+3]):
                    return True
            
            if r + 3 < rows and c - 3 >= 0:
                if (val == values[r+1][c-1] == values[r+2][c-2] == values[r+3][c-3]):
                    return True
                    
    return False
