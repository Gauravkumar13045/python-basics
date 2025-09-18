# Count the frequency of each elements in dictionary

thing_dic = {
    "Potato": 25,
    "onion": 20,
    "tomato": 40,
    "carrot": 30,
    "onion": 20,
    "Potato": 25
}

count = {}
for i in thing_dic.values():
    if i in count:
        count[i] += 1
    else:
        count[i]=1

print(count)
