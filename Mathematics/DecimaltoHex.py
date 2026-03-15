"""
Convert a non-negative integer n to its uppercase
hexadecimal string
without the ’0x’ prefix. For n == 0, return ’0’.
For n < 0, raise ValueError.
"""
def decimal_to_hex(n: int) -> str:
    if n<0:
        raise ValueError
    if n==0:
        return "0"
    return hex(n)[2:].upper()
