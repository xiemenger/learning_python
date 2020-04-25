#!/usr/bin/env python3

def main():
    tuple_list()
    str_fuctions()
    num_functions()

def num_functions():
    x = '47'
    y = -45.5
    z = 50
    print(int(x))
    print(abs(y))
    print(divmod(z, 5))  #divmod return a tuple with two values, the first value is the times, the second value is the remainder

def str_fuctions():
    s = 'Hello, World'
    print(repr(s))  # repr: represent itself

def tuple_list():
    x = (1, 2, 3, 4, 5)
    y = list(reversed(x))  # reverse x and change it to a list type
    print(x)
    print(y)
    print(sum(x))
    z = zip(x, y)
    for a, b in z:
        print(f'{a} {b}')

    animals = ('cat', 'dog', 'pig', 'cow')
    for i, v in enumerate(animals):
        print(f'{i} - {v}')


if __name__ == '__main__': main()