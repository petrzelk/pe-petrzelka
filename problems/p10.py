#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 10: Summation of Primes

Problem Description:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Functions:
sqrt
primes
'''

__date__ = "20 December 2019"

# Notes:
#
# Easy with the previous work on generating primes in problem 5.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import primes, is_prime

# User defined functions


# Solutions
def p10(limit: int = 2_000_000) -> int:
  """The solution.
  """
  result = 2
  for i in range(3, limit, 2):
    if is_prime(i):
      result += i
  return (result)


def p10alt(limit: int = 2_000_000) -> int:
  """Alternate solution.
  """
  return (sum(primes(limit)))


# Test cases
print(p10alt())
