#!/usr/bin/env python3

import sys
import os
import random

def main():
    v = sys.version
    p = sys.platform
    print('The Python version is {}{}{}'.format(*v))
    print(p)

    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())

    print(random.randint(1, 100))

if __name__ == '__main__': main()