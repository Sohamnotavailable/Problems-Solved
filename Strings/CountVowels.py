"""
Counts the number of vowels (a, e, i, o, u) in a string.
The function should be case-insensitive.
"""
def count_vowels(text):
    count=0
    for i in text:
        if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            count+=1
        elif i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            count+=1
    print(count)
count_vowels("Hello World")
count_vowels("PYTHON")
count_vowels("Rythm")
