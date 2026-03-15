"""
Partition the list lst using the first element as the
pivot.
Rearrange elements so that all elements before the pivot
are <= pivot
and all elements after the pivot are > pivot. Return the
final
index of the pivot.
"""
from typing import List

def partition(lst: List[int]) -> int:
    if not lst:
        return 0
        
    pivot = lst[0]
    smaller = []
    larger = []
    
    for x in lst[1:]:
        if x <= pivot:
            smaller.append(x)
        else:
            larger.append(x)
            
    lst[:] = smaller + [pivot] + larger
    return len(smaller)
