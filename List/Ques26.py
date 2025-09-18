# Find the second greatest element.

print()
print("To know the greatest number please input your numbers:")
print()

a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
c = int(input("Enter the number c: "))
d = int(input("Enter the number d: "))

lister = [a, b, c, d]

lister.sort()

sec_num = lister[-2]

print(f"\nThe second greatest number is : {sec_num}")
