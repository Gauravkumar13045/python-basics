a = int(input("Enter the number to check if it is a prime number: "))

if a <= 1:
    print("Enter a number greater than 1")
else:
    is_prime = True
    for i in range(2, a):
        if a % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{a} is a prime number.")
    else:
        print(f"{a} is not a prime number.")
