#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 39: Integer Right Triangles

Problem Description:
If p is the perimeter of a right angle triangle with integral length sides, {a, b, c}, 
there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p <= 1000, is the number of solutions maximised?

Functions:
sqrt
'''

__date__ = "6 September 2023"

# Notes:
#
# Assuming a,b, and c are in accending order, the maximum that a
# can be is if the triangle is an isosceles right, with side lengths
# n, n, and sqrt(2)*n. given a perimeter of 1000, n is 292.
#
# The most that b can be, assuming again ascending order. To find
# the max of b find the minimum of a, 1, and the remaining length
# must be split between b and c. this means that the max of b is 499.
#
# If a and b are known, find the length of the hypotenuse, c.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import sqrt

# User defined functions


# Solutions
def p39(limit: int = 1_000) -> int:
  """The solution.
  """
  result = {number: 0 for number in range(limit + 1)}
  for a in range(1, int(limit * sqrt(2, accuracy=10**(-len(str(limit)))))):
    for b in range(a, limit // 2):
      c = (a**2 + b**2)**.5
      if a + b + c > limit:
        break
      elif c % 1 == 0:
        result[a + b + c] += 1
  return ([i for i in result if result[i] == (max(result.values()))][0])


def p39alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p39())
