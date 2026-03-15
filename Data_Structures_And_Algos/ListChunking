"""
Split lst into consecutive chunks of size k and return a
list of
the chunks. The last chunk may be smaller.
Raise ValueError if k <= 0.
"""
def chunk_list(lst: list, k: int) -> list:
    
    if k <= 0:
        raise ValueError
    
    result = []
    for i in range(0, len(lst), k):
        result.append(lst[i:i + k])
    return result
