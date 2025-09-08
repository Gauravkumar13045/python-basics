# Reverse a string without using in build functions.

# Accept input from user
original = input("Enter a string to reverse: ")

# Initialize an empty string to hold the reversed result
reversed_string = ""

# Loop through the original string in reverse order
for i in range(len(original) - 1, -1, -1):
    reversed_string += original[i]

# Print the reversed string
print("Reversed string:", reversed_string)
