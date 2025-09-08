# 15. Accept a number and check if it a perfect number or not. A number whose sum of factors is equal to the number itself 

a = int(input("Enter the number to check if it is a perfect number: "))
sum = 0

if a > 0 :
    for i in range(1,a,1):
     if(a % i == 0):
      sum+= i
    if sum == a:
        print(f"{a} is a perfect number.")
    else:
        print(f"{a} is not a perfect number.")
else:
    print("Please enter a valid positive number.")