"""
Yield the first n Fibonacci numbers starting from 0, 1.
For example, fib_generator(6) yields:
0, 1, 1, 2, 3, 5
For n <= 0, yield nothing.
"""
def fib_generator(n: int):
    if n <= 0:
        return
    
    a, b = 0, 1
    yield a
    if n > 1:
        yield b
        for _ in range(n - 2):
            a, b = b, a + b
            yield b
