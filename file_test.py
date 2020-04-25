#!/usr/bin/env python3

def main():
    f = open('lines.txt') # open() return a file object, default read the file with read only mode
    # f = open('lines.txt', 'w') open the open with a write mode, if the file has content, empty the file.
    # if the file does not exist, create the file
    # f = open('lines.txt', 'a') # open the open with a write mode, but not remove the existing content
    # f = open('lines.txt', 'rt') # open the open with a write and text mode,

    for l in f:   #  the file obejct itself is an iterator, so we can iterate it.
        print(l.rstrip(), end = '')  # rstrip method is to remove white spaces in the end of the line

if __name__ == '__main__': main()