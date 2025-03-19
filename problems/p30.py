#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 30: Digit Fifth Powers

Problem Description:
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

Functions:
None
'''

__date__ = "27 February 2020"

# Notes:
#
# The upper bound on this is tricky.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p30(power: int = 5) -> int:
  """The solution.
  """
  limit = 0
  digits = 0
  while digits <= len(str(limit)):
    digits += 1
    limit += 9**power
  result = 0
  for n in range(10, limit):
    if n == sum(int(i)**power for i in str(n)):
      result += n
  return (result)


def p30alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p30())
