#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 36: Double-base Palindromes

Problem Description:
The decimal number, 585 = '0b1001001001' (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)

Functions:
None
'''

__date__ = "27 April 2023"

# Notes:
#
#


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import is_palendromic

# User defined functions


# Solutions
def p36(limit: int = 1_000_000):
  """The solution.
  """
  result = 0
  for n in range(limit):
    if is_palendromic(str(n)) and is_palendromic(bin(n)[2:]):
      result += n
  return (result)


def p36alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p36())
