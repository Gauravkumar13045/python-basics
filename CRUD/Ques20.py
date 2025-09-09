a = int(input("Tell me your age : "))

if(a >= 18) :
    r = open("./CRUD/Voter.txt", 'a')

    r.write(f"{a} is the eligible age")

else:
    print("not eligible")
