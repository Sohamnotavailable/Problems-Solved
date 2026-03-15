"""
Parser for simple delimited input strings.
Initialize with a raw string such as "10,20,30".
Methods:
- split(delimiter): split the stored string on the
delimiter and
return a list of substrings.
- map(dtype): convert the most recent split substrings
to the given
type (int, float, str, ...) and return the new list.
If split() has not been called, use the entire raw
string as
a single substring.
"""
class InputParser:
    
    def __init__(self, raw_string):
        self.raw_string = raw_string
        self.substrings = [raw_string]

    def split(self, delimiter):
        self.substrings = self.raw_string.split(delimiter)
        return self.substrings

    def map(self, dtype):
        return [dtype(s) for s in self.substrings]
