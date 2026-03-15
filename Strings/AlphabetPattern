"""
Prints a hollow alphabet pattern of height n.
"""
def print_alphabet_pattern(n):
    A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    w=2*n-1
    x=A[:2*n-1]
    print(x)
    for i in range(1,n):
        print(x[0:n-i]+" "*(2*i-1)+x[n+i-1:])

n=int(input("Enter a number : "))
print_alphabet_pattern(n)

'''
using a single loop and add substrings with spaces to make this pattern
'''
