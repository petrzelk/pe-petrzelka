#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 9: Special Pythagorean Triplet

Problem Description:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2.
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the 
product abc.

Functions:
None
'''

__date__ = "20 December 2019"

# Notes:
#
# My original solution is shown. Maybe some day I will return to this problem and solve
# it using diophantine equations.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p9(n: int = 1_000) -> int|None:
  """The solution.
  """
  for i in range(1, n // 2):
    for j in range(1, i):
      if i**2 + j**2 == (n - i - j)**2:
        return (i * j * (n - i - j))


def p9alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p9())
