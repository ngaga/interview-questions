# learning about comprehension
queries = {
    1: [10, 20, 30],
    2: [40, 50, 60]
}

l = [10, 20, 30, 40]
l = [8, 59]
l = [10, 20, 30, 40, 40, 50, 60]

# for each key value pair we want the key if the list items in the value are in the l
a = [key for key, value in queries.items() 
    if all(num in l for num in value)]

print(a)
