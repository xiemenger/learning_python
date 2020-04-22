#!usr/bin/env python3

# print
name = "Diane"
print("Good morning, {}".format(name))

#condition:
x = 100
y = 100
if x < y:
    print("x < y: x is {} and y is {}".format(x, y))
elif x == y:
    print("x equals to y, x = y {}".format(x))
else:
    print("x > y: x is {} and y is {}".format(x, y))


#Loops
words = ['one', 'two', 'three', 'four', 'five']
n = 0
while (n < 5):
    print(words[n])
    n += 1

for i in words:
    print(i)

#function
def calculate(x, y):
    print("x={}, y={}".format(x, y))
    return x + y

print(calculate(2, 5))
