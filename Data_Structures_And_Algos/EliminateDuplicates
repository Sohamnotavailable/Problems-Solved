"""
Remove duplicates from the list ls while preserving the
order
of first occurrence. Return the new list.
"""
from typing import List, Any

def eliminateDuplicates(ls: List[Any]) -> List[Any]:
    seen = set()
    result = []
    for item in ls:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
