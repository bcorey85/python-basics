def say_hello():
    print('hello')

say_hello()

def print_tree():
    picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
    ]

    for row in picture:
        for i in row:
            if (i == 0):
                print(" ", end="")
            else:
                print("*", end="")
        print('')

print_tree()
print_tree()

def say_name(name = 'Unknown Person'):
    print(f'Hello {name}')
    return f'Hello {name}'

say_name('Brandon')
say_name()
say_name(name='Bob')

greeting = say_name('Bill')
print(greeting)


def sum(num1, num2):
    num1 + num2

print(sum(1, 2))

def outer():
    a = 1
    string = 'hello'
    
    def inner(): 
        return {"a": a, "string": string}

    return inner

innerFn = outer()
print(innerFn()['string'])

def doc_strings(arg):
    '''
    Info: this comment denotes docstring for the function
    '''

    return arg

doc_strings(500)

print(doc_strings.__doc__)