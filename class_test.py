#!/usr/bin/env python3

class Animal:
    def __int__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'cat'  # default value
        self._name = kwargs['name'] if 'name' in kwargs else 'katty'  # default value
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'  # default value

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

class RevStr(str): # inheritance the str class
    def __str__(self):  # override the __str__ method
        return self[::-1]   #return reversed self str

def main():
    print(RevStr("Hi, I am Diane"))
    cat = Animal('cat', 'katty', 'meow')
    dog = Animal('dog', 'fubao', 'wangwang')
    print_animal(cat)
    print_animal(dog)

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError("print_animal requires input as type Animal")
    print('The type {} animal, name is {}, and sound like {}'.format(o.type, o.name, o.sound))


if __name__ == '__main__': main()