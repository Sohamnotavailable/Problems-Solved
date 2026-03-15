"""
Convert the binary string ’binaryValue’ to an uppercase
hexadecimal
representation without a ’0x’ prefix.
Raise ValueError if any character is not ’0’ or ’1’.
"""
def binaryToHex(binaryValue: str) -> str:
    for char in binaryValue:
        if char not in ('0', '1'):
            raise ValueError
    
    decimal_val = int(binaryValue, 2)
    return hex(decimal_val)[2:].upper()
