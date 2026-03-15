"""
Iterator that yields even numbers from 2 up to and
including n.
If n < 2, the iterator yields nothing.
"""
class EvenIterator:
    
    def __init__(self, n: int):
        self.n = n
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        
        val = self.current
        self.current += 2
        return val
