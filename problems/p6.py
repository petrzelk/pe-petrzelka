#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 6: Sum Square Difference

Problem Description:
The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385.
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025.
Hence the difference between the sum of the squares of the first ten natural numbers and
the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural 
numbers and the square of the sum.

Functions:
None
'''

__date__ = "20 December 2019"

# Notes:
#
# Again, an original solution and a more optimized for memory solution.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import*

# User defined functions


# Solutions
def p6(limit: int = 100) -> int:
  """The solution.
  """
  sumofsquares = sum([x**2 for x in range(limit + 1)])
  squareofsums = sum([x for x in range(limit + 1)])**2
  return (squareofsums - sumofsquares)


def p6alt(limit: int = 100) -> int:
  """Alternate solution.
  """
  sumofsquares = limit * (limit + 1) * (2 * limit + 1) // 6
  squareofsums = ((1 + limit) * limit // 2)**2
  return (squareofsums - sumofsquares)


# Test cases
print(p6alt())
