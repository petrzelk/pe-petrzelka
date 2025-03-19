#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 23: Non-Abundant Sums

Problem Description:
A perfect number is a number for which the sum of its proper divisors is exactly equal 
to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 
+ 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it 
is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that 
can be written as the sum of two abundant numbers is 24. By mathematical analysis, it 
can be shown that all integers greater than 28123 can be written as the sum of two 
abundant numbers. However, this upper limit cannot be reduced any further by analysis 
even though it is known that the greatest number that cannot be expressed as the sum of 
two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two 
abundant numbers.

Functions:
factor_sum
is_abundant
'''

__date__ = "23 April 2023"

# Notes:
#
# All multiples of an abundant number are themselves, multiples. Conciquencely, all
# multiples of an abundant number are the sum of two smaller abundant numbers.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import factor_sum, is_abundant

# User defined functions


# Solutions
def p23(limit: int = 28_123) -> int:
  """The solution.
  """
  abundants = []
  abundant_sums = set()
  for i in range(1, limit + 1):
    if is_abundant(i):
      abundants.append(i)
      for prev_abundant in abundants:
        if i + prev_abundant < limit:
          abundant_sums.add(i + prev_abundant)
        else:
          break
  return (sum(set(range(limit)) - abundant_sums))


def p23alt(limit: int = 28_123) -> int:
  """Alternate solution.
  """
  abundants = {i for i in range(1, limit + 1) if is_abundant(i)}
  return (sum(i for i in range(1, limit + 1)
              if not any(i - a in abundants for a in abundants)))


# Test cases
print(p23alt())
