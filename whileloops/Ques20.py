# 20. Accept a number and print its reverse

a = int(input("Enter the number to reverse: "))

if(a > 0):
 rev_num = 0
 while a > 0:
    sum = a % 10 
    rev_num = rev_num * 10 + sum
    a = a // 10
    
 print("Reversed number:", rev_num)

else: 
    print("Enter the positive number")