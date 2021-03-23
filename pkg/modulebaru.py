# print(module1.d)

# module1.hello()

# from module1 import d, hello

# print(d)
# hello()

from module1 import *

hello()

def root(angka):
    import math
    math.sqrt(angka)

root(4)

print(math) # error math is not defined

from pkg.module1 import hello as hi