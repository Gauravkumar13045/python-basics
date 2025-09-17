# Mean of List elements
print()
print("To know the Mean please input your numbers : ")
print()
a = int(input("Enter the number a : "))
b = int(input("Enter the number b : "))
c = int(input("Enter the number c : "))
d = int(input("Enter the number d : "))



lister = [a, b, c, d]
sum = 0

for i in lister:
    sum = sum + i
    length = len(lister)
    mean = sum / length

print("Mean of the list elements is:", mean)

