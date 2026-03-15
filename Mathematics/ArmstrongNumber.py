"""
Checks if a 3-digit number is an Armstrong number.
An Armstrong number is one where the sum of its digits
cubed equals the number itself (e.g., 153 = 1^3 + 5^3 + 3^3).
Prints an error for non-3-digit numbers.
Returns True if it is an Armstrong number, False otherwise.
"""
def check_armstrong(n):
    s=str(n)
    sum=0
    if len(s)!=3:
        print("Error: Not a 3-digit number.")
    else:
        for i in s:
            sum=sum+int(i)**3
        if sum==n:
            print(True)
        else:
            print(False)
check_armstrong(371)
check_armstrong(99)
