#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 62: Cubic Permutations

Problem Description:
The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104
(384**3) and 66430125 (405**3). In fact, 41063625 is the smallest cube which has exactly
three permutations of its digits which are also cube.
Find the smallest cube for which exactly five permutations of its digits are cube.

Functions:
None
'''

__date__ = '23 November 2023'

# Notes:
#
#


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p62(permutation_count:int=5) -> int:
  """The solution.
  """
  digit_count = 1
  while True:
    result = {}
    boundary = (int(10**((digit_count - 1) / 3)) + 1,
                int(10**(digit_count / 3) + 1))
    for n in range(boundary[0], boundary[1]):
      digits = list(str(n**3))
      digits.sort()
      digits = ''.join(digits)
      if digits not in result:
        result[digits] = [n**3, 1]
      else:
        result[digits][1] += 1
      if result[digits][1] == permutation_count:
        return (result[digits][0])
    digit_count += 1


def p62alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p62())
