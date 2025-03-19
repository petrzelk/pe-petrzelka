#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 66: Diophantine Equation

Problem Description:
Consider quadratic Diophantine equations of the form:
x**2 - Dy**2 = 1
For example, when D=13, the minimal solution in x is 649**2 - 13 * 180**2 = 1.
It can be assumed that there are no solutions in positive integers when D is square.
By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3**2 - 2 * 2**2 = 1
2**2 - 3 * 1**2 = 1
9**2 - 5 * 4**2 = 1
5**2 - 6 * 2**2 = 1
8**2 - 7 * 3**2 = 1

Hence, by considering minimal solutions in x for D <= 7, the largest x is obtained when
D=5.
Find the value of D <= 1000 in minimal solutions of x for which the largest value of x
is obtained.


Functions:
None
'''

__date__ = '7 December 2023'

# Notes:
#
#

# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import pell_min

# User defined functions


# Solutions
def p66(limit: int = 1_000) -> int:
  """The solution.
  """
  result = [0, 0]
  numbers = set(range(limit + 1)) - {i**2 for i in range(int(limit**.5) + 1)}
  for D in numbers:
    x = pell_min(D)
    if x > result[0]:
      result = [x, D]
  return (result[1])


def p66alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p66())
