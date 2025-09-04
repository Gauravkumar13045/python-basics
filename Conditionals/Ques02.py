# 2. Accept the gender from the user as char and print the respective greeting message 

a = input("Enter your gender(M/F) :")

if a == "M" or a == "m":
     print("Good Morning Sir")
elif a == "F" or a == "f":
     print("Good Morning Mam")
else :
     print("Invalid gender")