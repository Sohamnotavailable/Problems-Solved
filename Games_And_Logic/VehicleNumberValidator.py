"""
Return True if ’number’ has the form AA-DD-AA-DDDD
where A is an uppercase letter and D is a digit.
Otherwise return False.
"""
import re

def is_valid_vehicle_number(number: str) -> bool:
    pattern = r'^[A-Z]{2}-\d{2}-[A-Z]{2}-\d{4}$'
    return bool(re.match(pattern, number))
