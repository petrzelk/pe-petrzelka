#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 5: Smallest Multiple

Problem Description:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
without any remainder.
What is the smallest positive number that is evenly divisible, i. e. divisible with no 
remainder, by all of the numbers from 1 to 20?

Functions:
gcf
sqrt
factors
primes
'''

__date__ = "20 December 2019"

# Notes:
#
# The original solution is shown below. I have also included a much better solution as
# the alternate solution. While the first is over complicated, it did prepare me for
# future problems at the time that I wrote it.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import factors, gcf, primes

# User defined functions


# Solutions
def p5(limit: int = 20) -> int:
  """The solution.
  """
  result_factors = {n: 0 for n in primes(limit)}
  for number in range(2, limit + 1):
    number_factors = factors(number)
    for factor in number_factors:
      result_factors[factor] = max(result_factors[factor],
                                   number_factors[factor])
  result = 1
  for factor in result_factors:
    result *= factor**(result_factors[factor])
  return (result)


def p5alt(limit: int = 20) -> int:
  """Alternate solution.
  """
  result = limit
  for n in range(1, limit):
    if result % n != 0:
      result *= n // gcf(n, result)
  return (result)


# Test cases
print(p5alt())
