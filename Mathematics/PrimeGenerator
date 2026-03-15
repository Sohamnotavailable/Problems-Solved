"""
Yield the first n prime numbers in ascending order.
For n <= 0, yield nothing.
"""
def prime_generator(n: int):
    
    if n <= 0:
        return
        
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1
