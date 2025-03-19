#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 63: Powerful Digit Counts

Problem Description:
The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number,
134217728=8**9, is a ninth power.
How many n-digit positive integers exist which are also an nth power?

Functions:
None
'''

__date__ = 'DATE'

# Notes:
#
# The base can't be ten, this would yeild a n+1 digit.
# This means for our upper bound we consider the base to be nine.
# What exponent of 9 yeilds an n-1 digit number? 22
#
# Exponents can be 1-22. Bases can be 1-10.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p63() -> int:
  """The solution.
  """
  result = 0
  for base in range(1, 10):
    for exponent in range(1, 22):
      if len(str(base**exponent)) == exponent:
        result += 1
  return (result)


def p63alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p63())
