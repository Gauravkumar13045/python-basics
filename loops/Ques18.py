# Count all letters, digits, and special symbols from a given string 
a = input("Enter a string: ")

letters = 0
number = 0
symbol = 0

for ch in  a:
    ascii_val = ord(ch)
    if(65 <= ascii_val <= 90) or (97 <= ascii_val <= 122):
        letters += 1
    elif 48 <= ascii_val <= 57:
        number += 1
    else:
        symbol += 1

print("Letters:", letters)
print("Digits:", number)
print("Symbols:", symbol)

