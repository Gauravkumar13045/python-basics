#  Find the greatest element and print its index too

print()
print("To know the greatest number please input your numbers:")
print()

a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
c = int(input("Enter the number c: "))
d = int(input("Enter the number d: "))

lister = [a, b, c, d]


greatest = lister[0]
index = 0  


for i in range(len(lister)):
    if lister[i] > greatest:
        greatest = lister[i]
        index = i

print("\nGreatest element is:", greatest)
print("Its index in the list is:", index)
