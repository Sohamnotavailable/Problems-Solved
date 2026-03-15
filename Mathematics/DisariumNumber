"""
A Disarium number is one where the sum of its digits
raised to their respective positions equals the number itself.
e.g. 175: 1^1 + 7^2 + 5^3 = 175
"""
def is_disarium(n):
    sum=0
    s=str(n)
    fv=1
    for i in s:
        sum=sum+int(i)**fv
        fv+=1
    if sum==n:
        return True
    else:
        return False
print(is_disarium(175))
print(is_disarium(89))
print(is_disarium(100))
