""" https://projecteuler.net/problem=2
Finding all the even fibonnaci numbers below four million and summing them """

from functools import reduce

# def fib(number):
#     """Fibonacci calculator, not optimized at all"""
#     if number == 0 or number == 1:
#         return 1
#     else:
#         return fib(number-1) + fib(number-2)

# def fibonnaci(number):
#     """Generates all the fibbonaci numbers"""
#     counter = 1
#     result = [1]
#     while result[len(result)-1] < number:
#         result.append(fib(counter))
#         counter = counter + 1
#     result.pop()
#     return result

def fibinplace(number):
    """ Generates all fibonnaci numbers up to (but not including)
    the specified number, in place, to avoid stack overflow """
    counter = 2
    result = [1, 2]
    while result[len(result)-1] < number:
        result.append(result[counter-1] + result[counter-2])
        counter = counter + 1
    result.pop()
    return result

FIB = fibinplace(4000000)
RESULT = reduce(lambda x, y: x + y, filter(lambda x: True if x % 2 == 0 else False, FIB))
print(RESULT)
