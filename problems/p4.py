#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 4: Largest Palindrome Product

Problem Description:
A palindromic number reads the same both ways. The largest palindrome made from the 
product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.

Functions:
product
'''

__date__ = "20 December 2019"

# Notes:
#
# Casting to strings makes life easy. The first is my original solution to the problem.
# The alternate solution is starting searching from the right place and terminates at
# the correct time. While the lower limit on this problem makes it easy to solve,
# the savings become apparent when looking at just 4 digits instead of 3.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import product

# User defined functions


# Solutions
def p4(digits: int = 3) -> int:
  """The solution.
  """
  result = (int(0), int(0))
  for x in range(10**digits):
    for y in range(10**digits):
      if str(x * y) == str(x * y)[::-1] and x * y > result[0] * result[1]:
        result = (x, y)
  return (product(result))


def p4alt(digits: int = 3) -> int:
  """Alternate solution.
  """
  result = 0
  top, bottom = 10**digits, 10**(digits - 1)
  x, y = top, top
  while x > bottom and x * y > result:
    while y > bottom and x * y > result:
      if str(x * y) == str(x * y)[::-1]:
        result = x * y
      y -= 1
    x -= 1
    y = top
  return (result)


# Test cases
print(p4alt())
