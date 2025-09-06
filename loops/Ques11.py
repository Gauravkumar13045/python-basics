# 11. Sum up to n terms

a = int(input("Enter the number to get the sum: "))
b = 0
for i in range(1, a + 1, 1):
    b = b + i

print("The final sum is:", b)
