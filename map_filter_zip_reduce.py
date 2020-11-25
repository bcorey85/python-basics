from functools import reduce

my_list = [1, 2, 3]

def multiply_by2(item):
    return item * 2

#map, similar to JS
new_list = list(map(multiply_by2, my_list))

print(new_list)


def only_odd(item):
    return item % 2 != 0

# filter, similar to JS
filtered_list = list(filter(only_odd, my_list))

print(filtered_list)

list_two = [2, 4, 6]

#combines each index of list into new list
zipped_list = list(zip(my_list, list_two))

print(zipped_list)

def accumulator(acc, cur):
    return acc + cur

reduced_list = reduce(accumulator, my_list, 0)

print(reduced_list)


#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize_pet(pet):
    return pet.capitalize()

capital_pets = list(map(capitalize_pet, my_pets))
print(capital_pets)


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

my_numbers.sort()

zipped_list = list(zip(my_strings, my_numbers))
print(zipped_list)


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def filter_above_fifty(score):
    return score > 50

filtered_scores = list(filter(filter_above_fifty, scores))
print(filtered_scores)


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def sum_nums(acc, item):
    return acc + item

all_scores = scores + my_numbers
summed_nums = reduce(sum_nums, all_scores, 0)
print(summed_nums)