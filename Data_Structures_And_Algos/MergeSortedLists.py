"""
Merge two sorted lists into a new sorted list containing
all
elements from both lists.
"""
from typing import List, Any

def merge(list1: List[Any], list2: List[Any]) -> List[Any]:
    ans = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            ans.append(list1[i])
            i += 1
        else:
            ans.append(list2[j])
            j += 1
    
    while i < len(list1):
        ans.append(list1[i])
        i += 1
    
    while j < len(list2):
        ans.append(list2[j])
        j += 1
        
    return ans
