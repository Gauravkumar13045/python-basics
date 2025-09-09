# 19. Separate each digit of a number and print it on the new line.

a = int(input("Enter the number: "))

while a > 0:
    digit = a % 10
    print(digit)
    a = a // 10
