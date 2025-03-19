#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 43: Sub-string Divisibility

Problem Description:
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of 
the digits 0 to 9 in some order, but it also has a rather interesting sub-string 
divisibility property.
Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note the 
following:
d_2 d_3 d_4    =406 is divisible by 2
d_3 d_4 d_5    =063 is divisible by 3
d_4 d_5 d_6    =635 is divisible by 5
d_5 d_6 d_7    =357 is divisible by 7
d_6 d_7 d_8    =572 is divisible by 11
d_7 d_8 d_9    =728 is divisible by 13
d_8 d_9 d_{10} =289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

Functions:
None
'''

__date__ = "7 September 2023"

# Notes:
#
#


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p43(partial: str = '') -> int:
  """The solution.
  """
  primes = [1, 1, 1, 1, 2, 3, 5, 7, 11, 13, 17]
  if partial == '' or int(partial[-3:]) % primes[len(partial)] == 0:
    if len(partial) == 10:
      return (int(partial))
    else:
      result = 0
      for i in {str(c) for c in range(10)} - set(partial):
        result += p43(partial + i)
      return (result)
  else:
    return (0)


def p43alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p43())
