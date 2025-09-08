# 13. Print the sum of all even & odd numbers in a range separately

a = int(input("Enter the number to get the sum: "))
odd = 0
even = 0

for i in range(1, a + 1):
    if i % 2 == 0:
        even += i
    else:
        odd += i

print("Sum of even numbers:", even)
print("Sum of odd numbers:", odd)

