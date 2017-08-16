""" Answer to https://projecteuler.net/problem=1 """
from functools import reduce

THREES = set([(x+1)*3 for x in range(333)])
FIVES = set([(x+1)*5 for x in range(199)])

PROD = lambda x, y: x+y


print(reduce(PROD, THREES|FIVES))
