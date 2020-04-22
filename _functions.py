#!usr/bin/env python3

def main():
    kitten('meow', 'grr', 'purr')
    dog(dog1='wan', dog2='wanwan', dog3='wanwanwan..')
    x =  _to_test_return()
    print(type(x), x)  #(<type 'dict'>, {'y': 2, 'x': 1, 'z': 3})
    _range()

    for i in inclusive_range(10):
        print(i, end = ' ')
    print()

def kitten(*input): #input is a tuple
    if len(input) > 0:
        for item in input:
            print(item)
    else:
        print("meow")

def dog(**input):  #input is a dictionary
    if len(input) > 0:
        for i in input:
            print('{} say {}'.format(i, input[i]))
    else:
        print("wanwanwanwan....")

def _to_test_return():
    return dict(x = 1, y = 2, z = 3)

#generator:
# is a special class of function that serves as an iterator
# return a stream of values
# key work 'yield' likes 'return', but it exclusive for generator
def _range():
    for i in range (10):
        print(i, end = ' ')
    print()

def inclusive_range(*args): #*args : list of args
    num = len(args)
    start = 0
    end = 1
    step = 1

    if num < 1 or num > 3:
        raise TypeError(f'expected as least 1 argument, got {num}')
    elif num == 1:
        end = args[0]
    elif num == 2:
        (start, end) = args[0], args[1]
    elif num == 3:
        (start, end, step) = args[0], args[1], args[2]

    while start <= end:
        yield start   # like return, but exclusively of generator
        start += step

if __name__ == '__main__': main()
