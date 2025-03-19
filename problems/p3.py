#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 3: Largest Prime Factor

Problem Description:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

Functions:
sqrt
'''

__date__ = "20 December 2019"

# Notes:
#
# The solution that I placed here is a previous attempt.
# The alternate uses my understanding of python as of June 2024.
# Similarly, I have pulled my square root funciton from June 2024.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import sqrt

# User defined functions


# Solutions
def p3(n: int = 600_851_475_143) -> int:
  """The solution.
  """
  result = n
  for x in range(2, int(n**.5 + 1)):
    if n / x == n // x:
      result = p3(n // x)
      break
  return (result)


def p3alt(n: int = 600_851_475_143) -> int:
  """Alternate solution.
  """
  factor = 1
  limit = sqrt(n)
  while factor < limit:
    factor += 1
    while n % factor == 0:
      n //= factor
      limit = sqrt(n)
  return (n)


# Test cases
print(p3alt()) 
