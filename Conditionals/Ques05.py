# Q5. Accept a year and check if it a leap year or not

a = int(input("Enter the year"))

if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print(f"{a} is a leap year")
else :
    print(f"{a} is not a leap year")    