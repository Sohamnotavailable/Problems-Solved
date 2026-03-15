"""
Group words by their length.
Return a dictionary mapping length -> list of words of
that length.
Preserve the original order within each list.
"""
def group_by_word_length(words: list) -> dict:
    
    result = {}
    for w in words:
        length = len(w)
        if length not in result:
            result[length] = []
        result[length].append(w)
    return result
