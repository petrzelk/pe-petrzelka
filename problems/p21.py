#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 21: Amicable Numbers

Problem Description:
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide
evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a 
and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 
220.
Evaluate the sum of all the amicable numbers under 10000.

Functions:
factor_sum
'''

__date__ = "27 July 2020"

# Notes:
#
#


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import factor_sum

# User defined functions


# Solutions
def p21(limit: int = 10_000) -> int:
  """The solution.
  """
  result = 0
  for n in range(limit):
    pair = factor_sum(n)
    if pair > n and factor_sum(pair) == n:
      result += n
      if pair < limit:
        result += pair
  return (result)


def p21alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p21())
