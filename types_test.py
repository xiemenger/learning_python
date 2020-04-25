x = 7.0
y = True
print(type(x))
print(type(y))

#String
# in python, single quote equals to double quote
x = '7'
print(type(x))

# multiple line string:
y = '''
hi,
diane
'''
print(y)
print(type(y))

# Integer
z = 7
print('z is {}'.format(z))
print(type(z))

# Float and Decimal
xx = .1 + .1 + .1 - .3
print(xx)  #5.55111512313e-17

from decimal import *
a = Decimal('0.10')
b = Decimal('0.30')
aa = a + a + a - b
print('aa is {}'.format(aa))
print(type(aa))

#sequence
x = range(5)
for i in x:
    print(i)

x = range(5, 30, 5) # start from 5, end at 30, each step is 5
for i in x:
    print(i)

#map
x = {"one":1, "two":2, "three":3, "four":4, "five":5}
for k,v in x.items():
    print("k={}, v={}".format(k, v))

x = (1, "one", [3, 3.0], "diane")
y = (1, "one", [3, 3.0], "diane")
print(id(x))
print(id(y))  #id are different
print(id(x[0]))
print(id(y[0]))  #ids are same
print(id(x[1]))
print(id(y[1]))# ids are same
print(id(x[2]))
print(id(y[2]))# ids are different
if isinstance(x, tuple):
    print("x is type tuple ")
else:
    print("x is not type tuple")

