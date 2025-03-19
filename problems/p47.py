#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 47: Distinct Primes Factors

Problem Description:
The first two consecutive numbers to have two distinct prime factors are:
14 = 2 * 7
15 = 3 * 5.
The first three consecutive numbers to have three distinct prime factors are:
644 = 2**2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.
Find the first four consecutive integers to have four distinct prime factors each. What 
is the first of these numbers?

Functions:
None
'''

__date__ = "8 September 2023"

# Notes:
#
# This implimentation is length and computationally heavy.
# Improvements could be made by focusing on primes and if there is a big enough gap,
# then checking the numbers between them.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p47() -> int:
  """The solution.
  """
  primes = [2, 3]
  n = 4
  factor_counts = [1, 1, 1, 1]
  while factor_counts != [4, 4, 4, 4]:
    del factor_counts[0]
    factor_counts.append(0)
    remainder = n
    for p in primes:
      if remainder % p == 0:
        factor_counts[-1] += 1
        while remainder % p == 0:
          remainder //= p
      if remainder == 1 or p**2 > n:
        break
    if remainder == n:
      primes.append(n)
    n += 1
  return (n - 4)


def p47alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p47())
