"""
Remove directly consecutive duplicate elements from lst
and return
the resulting list. Non-consecutive duplicates should
remain.
Example:
[1,1,2,2,2,3,1,1] -> [1,2,3,1]
"""
def remove_consecutive_duplicates(lst: list) -> list:
    
    if not lst:
        return []
        
    result = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            result.append(lst[i])
    return result
