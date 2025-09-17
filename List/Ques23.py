# Print positive and negative elements of an List

a = int(input("Enter the number a : "))
b = int(input("Enter the number b : "))
c = int(input("Enter the number c : "))
d = int(input("Enter the number d : "))



lister = [a, b, c, d]

print("Positive numbers:")
for i in lister:
  if i > 0 :
   print(i)

print("Negative numbers:")
for i in lister:
    if i < 0:
        print(i)