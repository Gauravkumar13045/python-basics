# Reverse a string without using in build functions.


original = input("Enter a string to reverse: ")
reversed_string = ""


for i in range(len(original) - 1, -1, -1):
    reversed_string += original[i]


print("Reversed string:", reversed_string)
