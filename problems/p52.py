#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 52: Permuted Multiples

Problem Description:
It can be seen that the number, 125874, and its double, 251748, contain exactly the same
digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the
same digits.

Functions:
None
'''

__date__ = '9 September 2023'

# Notes:
#
# Check each set of numbers between the powers of ten, as the they must contain the same
# number of digits. The starting number must be in the first nth portion for n multiples
# having the same digits.

# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import is_anagramic

# User defined functions


# Solutions
def p52(multiples: int = 6) -> int:
  """The solution.
  """
  digits = 1
  # Check each set of numbers where they have the same number of digits till the lowest
  # is found.
  while True:
    # The starting number must be within the first sixth of the set of numbers as any
    # larger number would cause 6x to have more digits
    for n in range(10**(digits - 1), 10**digits // multiples):
      # Test multiples for anagramy
      if all(
          is_anagramic(str(n), str(n * i)) for i in range(2, multiples + 1)):
        return (n)
    digits += 1
    #print(digits)


def p52alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p52())
