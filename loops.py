list = [1, 2, 3, 4, 5]

for item in list:
    print(item)

user = {
    "name": "Bob",
    "age": 5006,
    "swimming": False
}

for key, value in user.items():
    print(key, value)

for key in user.keys():
    print(key)

for value in user.values():
    print(value)
