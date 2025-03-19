#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 56: Powerful Digit Sum

Problem Description:
A googol (10**100) is a massive number: one followed by one-hundred zeros; 100**100
is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the
sum of the digits in each number is only 1.
Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum
digital sum?

Functions:
None
'''

__date__ = '10 September 2023'

# Notes:
#
#


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p56() -> int:
  """The solution.
  """
  result = 0
  for a, b in ((a, b) for a in range(100) for b in range(100)):
    result = max([result] + [sum([int(i) for i in str(a**b)])])
  return (result)


def p56alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p56())
