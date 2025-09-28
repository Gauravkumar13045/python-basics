# Write a Python program to combine two dictionary by adding values for common keys.

student = {"name1": "Gaurav", "age": 20 }
teacher = {"name2": "krishna", "age": 50}

combine = student.copy()

for i, value in teacher.items():
    if i in combine :  
        combine[i] += value
    else:
        combine[i] = value

print("Combined dictionary:", combine)