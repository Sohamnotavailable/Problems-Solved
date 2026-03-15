"""
Given a dictionary with unique values, return a new
dictionary
where keys and values are swapped.
"""
def reverse_dictionary(d: dict) -> dict:
    new_dict = {}
    for k, v in d.items():
        new_dict[v] = k
    return new_dict
