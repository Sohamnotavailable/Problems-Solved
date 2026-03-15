"""
Constructs an N-digit positive integer X such that:
1. It is divisible by 3.
2. It is not divisible by 9.
3. It has no leading zeros.
Returns any valid integer.
"""
def construct_number(N):
    end=0
    for e in range(0,N):
        end=end+9*(10**e)
    for i in range(10**(N-1),end):
        ch=str(i)
        sum=0
        for j in ch:
            sum=sum+int(j)
        if sum%3==0 and sum%9!=0 and i%10!=0:
            print(i)
            break
construct_number(1)
construct_number(2)
construct_number(3)
construct_number(4)
