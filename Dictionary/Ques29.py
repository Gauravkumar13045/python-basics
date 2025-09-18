# Write a Python program to sum all the values in a dictionary

thing_dic = {
    "Potato": 25,
    "onion": 20,
    "tomato": 40,
    "carrot": 30
}

sum = 0
for i in thing_dic:
    sum = sum + thing_dic[i]

print(sum)