""" https://projecteuler.net/problem=3
Finding the largest prime factor from a number """

from functools import reduce
from math import sqrt, ceil

# 600851475143

#find primes

def find_primes(number):
    """ Finds primes up to number by removing all the numbers that are hit by other numbers"""
    result = [2, 3, 5, 7]
    searcharea = range(9, number, 2)
    for number in searcharea:
        isprime = True
        for prime in result:
            if number % prime == 0:
                isprime = False
                break
        if isprime:
            result.append(number)
    return result

def split_to_primes(number):
    """ Finds all primes products of a number"""
    result = [1]
    for prime in find_primes(ceil(sqrt(number))):
        if number % prime == 0:
            result.append(prime)
    return result


print(reduce(lambda x, y: x if x > y else y, split_to_primes(600851475143)))
