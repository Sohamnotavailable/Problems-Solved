"""
Raise InvalidAgeError if age < 0 or age > 150.
Otherwise return "Valid Age".
"""
class InvalidAgeError(Exception):
    pass

def check_age(age: int) -> str:
    if age < 0 or age > 150:
        raise InvalidAgeError
    return "Valid Age"
