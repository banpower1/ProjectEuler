""" Answer to https://projecteuler.net/problem=5
Finding the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 """
from functools import reduce

def gcd(a, b):
    """ Greatest common divider (returns a float, which is a mistake..) """
    d = 0
    while a % 2 == 0 and b % 2 == 0:
        a = a / 2
        b = b / 2
        d += 1
    while a != b:
        if a % 2 == 0:
            a = a / 2
        elif b % 2 == 0:
            b = b / 2
        elif a > b:
            a = (a-b) / 2
        else:
            b = (b-a) / 2
    return a * 2**d

def lcm(a, b):
    """ Uses GCD to find LCM, which is lowest common multiplum """
    return (a * b) / gcd(a, b)

print(reduce(lcm, list(range(1, 21))))
