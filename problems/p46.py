#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 46: Goldbach's Other Conjecture

Problem Description:
It was proposed by Christian Goldbach that every odd composite number can be written as 
the sum of a prime and twice a square.
9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2
It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and 
twice a square?

Functions:
sqrt
is_prime
is_square
'''

__date__ = "7 September 2023"

# Notes:
#
#


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import is_prime, is_square

# User defined functions


# Solutions
def p46() -> int:
  """The solution.
  """
  primes = {2}
  n = 3
  while True:
    if is_prime(n):
      primes |= {n}
    elif all(not is_square((n - p) // 2) for p in primes):
      return (n)
    n += 2


def p46alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p46())
