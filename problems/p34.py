#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 34: Digit Factorials

Problem Description: 
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.

Functions:
factorial
'''

__date__ = "27 April 2023"

# Notes:
#
# The limit that we have to check is 10**7 because 9!*7<10**7.
# Could get this to be facster with a better limit.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import factorial

# User defined functions


# Solutions
def p34(limit: int = 10**7):
  """The solution.
  """
  fact = {str(n): factorial(n) for n in range(10)}
  result = 0
  n = 3
  while n < limit:
    if n == sum(fact[c] for c in str(n)):
      result += n
      #print(n)
    n += 1
  return (result)


def p34alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p34())
