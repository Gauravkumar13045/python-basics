# Check if List is sorted or not.

print()
print("To know the greatest number please input your numbers:")
print()

a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
c = int(input("Enter the number c: "))
d = int(input("Enter the number d: "))

lister = [a, b, c, d]


if lister == sorted(lister):
    print("Sorted")
else:
    print("Unsorted")
