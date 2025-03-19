#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 38: Pandigital Multiples

Problem Description:
Take the number 192 and multiply it by each of 1, 2, and 3:
192 * 1 = 192
192 * 2 = 384
192 * 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 
192384576 the concatenated product of 192 and (1,2,3).
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving
the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
concatenated product of an integer with (1,2, ..., n) where n > 1?

Functions:
None
'''

__date__ = "27 April 2023"

# Notes:
#
# The upper limit is 9999 with n=2 pandigital multiples. This is an awful solution, but
# the scope of the problem is extremely small. A better upper limit is 9500 and 2*9500
# is 19000, meaning the 9 causes it to ot be pandigital. The alternate answer exploits t
# the known values and narrows down the search as we get larger.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p38():
  """The solution.
  """
  result = "123456789"
  sorted_result = result
  for n in range(10_000):
    string = str(n)
    multiple = 2
    while len(string) < 9:
      string += str(n * multiple)
      multiple += 1
    if len(string) == 9 and string > result:
      sorted = list(string)
      sorted.sort()
      if ''.join(sorted) == sorted_result:
        result = string
  return (int(result))


def p38alt():
  """Alternate solution.
  """
  # Start at the given maximum with the starting digits
  result = "918273645"
  sorted_result = "123456789"
  # We are given the maximum for single digits,
  for digits in range(2, 5):
    # The next possible chain could start what we have, no less.
    for n in range(int(result[:2]), 95 * 10**(digits - 2)):
      # Construct the concatinated multiple
      string = str(n)
      multiple = 2
      while len(string) < 9:
        string += str(n * multiple)
        multiple += 1
      # Test if it is pandigital larger than the current maximum.
      if len(string) == 9 and string > result:
        sorted = list(string)
        sorted.sort()
        if ''.join(sorted) == sorted_result:
          result = string
  # Return the result as an integer.
  return(int(result))


# Test cases
print(p38alt())
