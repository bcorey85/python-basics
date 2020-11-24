num_list = [1, 2, 3, 4, 5]

for item in num_list:
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

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0
for item in my_list:
    sum += item

print(sum)


for num in range(0, 5):
    print(num)


for i, char in enumerate(list(range(100))):
    if (char == 50):
        print(f'index of 50 is {i}')


i = 0
while i < 5:
    print(i)
    i += 1

