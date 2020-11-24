#slicing - start index included, but not end index
mystring = "aaaaCOPYMEaaaa"
print(mystring[4:10])

# negative slice
negative_slice = '00000a'
print(negative_slice[-1])

# 'new style'
string_1 = "Insert another string here: {}".format("Insert ME")
print(string_1)

string_2 = "Item One: {} Item Two: {}".format('INSERT ME', 'INSERT ME AGAIN')
print(string_2)

# 'old style'
word = 'ADDED'
word2 = 'ALSO ADDED'
string_3 = "This is word is injected: %s and this one too: %s" % (word, word2)
print(string_3)



# string interpolation / 'f' string
name = 'Bob'
code = 'Secret'

string_3 = f"this is {name}'s secret code: {code}"
print(string_3)

