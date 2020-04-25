#!usr/bin/env python3

def main():
    #test_list()
    #test_dict()
    #test_set()
    test_list_comprehension()


#List [ ]
def test_list():
    game = ['game1', 'game2', 'game3', 'game4', 'game5']
    for i in game:
        print(i, end = ' ', flush = True)
    print()                      #game1 game2 game3 game4 game5

    print(game[1:5:2])           #['game2', 'game4']
    print(game.index('game2'))   #1
    game.append('game6')         #['game1', 'game2', 'game3', 'game4', 'game5', 'game6']
    print(game)                  #['game1', 'game2', 'game3', 'game4', 'game5', 'game6']
    game.insert(0, 'game-1')
    print(game)                  #['game-1', 'game1', 'game2', 'game3', 'game4', 'game5', 'game6']
    game.remove('game3')
    print(game)                  #['game-1', 'game1', 'game2', 'game4', 'game5', 'game6']
    game.pop()
    print(game)                  #['game-1', 'game1', 'game2', 'game4', 'game5']
    game.pop(2)
    print(game)                  #['game-1', 'game1', 'game4', 'game5']
    del game[0]
    print(game)                  #['game1', 'game4', 'game5']
    del  game[1:3]
    print(game)                  #['game1']
    game.append('game2')
    game.append('game3')
    game.append('game4')
    print(', '.join(game))       #game1, game2, game3, game4

# tuple (), is not mutable, cannot be changed once it's created
#y = (1, 2, 3, 4)

# Dictionary , { } a list of key-value pair
# Key and value can be any type
#
def test_dict():
    dicts = {'key1':'val1', 'key2':'val2', 'key3':'val3', 'key4':'val4'}
    print(dicts)
    for k, v in dicts.items():
        print(f'{k}:{v}')
    for k in dicts.keys():
        print(k, end = ' ')
    print()
    for v in dicts.values():
        print(v, end = ' ')
    print()
    dicts['key10'] = 'val10'
    print(dicts)

# Set { }, only contain unique values, does not allow duplicates
def test_set():
    set1 = set("I am Diane, I love gardening!")
    set2 = set("I am Fubao, I am a pet, I love love love my master Diane!")
    print(set1)    #{'r', 'g', 'v', 'l', 'i', ' ', ',', 'a', 'e', 'd', 'I', 'm', 'o', '!', 'n', 'D'}
    print(set2)    #{'v', ' ', 'a', 'u', 'p', 'm', 'F', 'n', 'D', 'l', 'b', 't', 'e', 'o', 'i', 's', 'I', '!', 'r', 'y', ','}
    print(sorted(set1))
    print(sorted(set2))
    print(set1 - set2) # print characters which is in set1 but not in set2
    print(set1 | set2) # print characters which is in set1 or in set2
    print(set1 ^ set2) # print characters which is in set1 or in set2 but not both
    print(set1 & set2) # print characters both in the set1 and set2

def test_list_comprehension():
    seq = range(5)
    seq2 = [(x, x**2) for x in seq]
    print(seq2)

if __name__ == '__main__': main()
