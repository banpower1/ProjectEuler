""" https://projecteuler.net/problem=6
Finding the difference between
the sum of the squares of the first one hundred natural numbers
and the square of the sum """

numbers = list(range(1, 101))
sumOfSquares = sum(map(lambda x: x**2, numbers))
squareOfSums = sum(numbers)**2
print(squareOfSums - sumOfSquares)
