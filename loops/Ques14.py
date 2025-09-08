# 14. Print all the factors of a number

a = int(input("Enter the number to get the factors: "))


if(a > 0):
    for i in range(1, a+1 , 1):
        if(a % i == 0):
            print(i)

else:
    print("Please enter a valid number")