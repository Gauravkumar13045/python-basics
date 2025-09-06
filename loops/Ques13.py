# 13. Print the sum of all even & odd numbers in a range separately

a = int(input("Enter the number to get the sum : "))
odd = 0
even = 0

if a%2 == 0 :
    for i in range(1,a+1):
        even = even + i
        print(even)
    
else :
        for i in range(0,a,1):
         odd = odd + i 
        print(odd)