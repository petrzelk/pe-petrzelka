#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 15: Lattice Paths

Problem Description:
Starting in the top left corner of a 2 by 2 grid, and only being able to move to the 
right and down, there are exactly 6 routes to the bottom right corner.
img "0015_lattice.png"
How many such routes are there through a 20 by 20 grid?

Functions:
factorial
product
'''

__date__ = "27 Jan 2020"

# Notes:
#
# Apperently this is just 40 choose 20, as it is related to Pascal's Triangle.

# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import factorial, product

# User defined functions


# Solutions
def p15(m: int = 20, n: int = 20) -> int:
  """The solution.
  """
  result = {
      str(i) + ' ' + str(j): 0
      for i in range(m + 1)
      for j in range(n + 1)
  }
  result[str(m) + ' ' + str(n)] = 1
  done = False
  while not done:
    done = True
    for key in result:
      if key[0] != "0" and key[-2:] != " 0" and result[key]:
        done = False
        m, n = tuple(int(i) for i in key.split())
        if m == n:
          result[str(m - 1) + ' ' + str(n)] += 2 * result[key]
        else:
          result[str(m - 1) + ' ' + str(n)] += result[key]
          result[str(m) + ' ' + str(n - 1)] += result[key]
        result[key] = 0
  return (sum(result.values()))


def p15alt(m: int = 20, n: int = 20) -> int:
  """Alternate solution.
  """
  return (factorial(m + n) // factorial(m) // factorial(n))


# Test cases
print(p15alt())
