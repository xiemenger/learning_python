#!/usr/bin/env python3

def main():
    print('hello, world'.upper())
    print('DIANE'.lower())
    print('i am fubao'.title())
    print('FuBao'.swapcase())

    s = 'This is a long string with a bunch of words in it.'
    print(s.split())  #default, space is the splitter
    print(s.split('long'))
    l = s.split()
    print(':'.join(l))

if __name__ == '__main__': main()