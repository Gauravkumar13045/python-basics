# Accept a number and check if it is a pallindromic number.

a = int(input("Enter the number to check whether it is palindrome or not: "))
real = a
rev_num = 0

if a > 0:
    while a > 0:
        digit = a % 10
        rev_num = rev_num * 10 + digit
        a = a // 10

    if real == rev_num:
        print("It is a palindrome number")
    else:
        print("Not a palindrome")
else:
    print("Non-positive number not supported")
