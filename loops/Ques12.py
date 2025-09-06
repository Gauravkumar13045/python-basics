# 12. Factorial of a number

a = int(input("Enter the number to get the factorial : "))   
b = 1

if a < 0:
    print("Factorial does not exist for negative numbers.")
elif a == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, a + 1):
        b = b * i
    print("The factorial of", a, "is", b)