#!/usr/bin/env python3

class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        self._start = 0
        self._step = 1

        if numargs < 1:
            raise TypeError('excepted at least 1 argument, got {}'.format(numargs))
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start, self._stop, self._step) = args
        else:
            raise TypeError('excepted less than or equal to 3 arguments, got {}'.format(numargs))

        self._next = self._start

    def __iter__(self):  #identify this object is an iterator
        return self

    def __next__(self):
        if self._next > self._stop:
            raise StopIteration
        else:
            _r = self._next
            self._next += self._step
            return _r

def main():
    for i in inclusive_range(1, 10):
        print(i, end = ' ')
    print()


if __name__ == '__main__':main()