#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 25: 1000-digit Fibonnaci Number

Problem Description:
The Fibonacci sequence is defined by the recurrence relation:
F_n = F_{n - 1} + F_{n - 2}, where F_1 = 1 and F_2 = 1
Hence the first 12 terms will be:
F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_{10} = 55
F_{11} = 89
F_{12} = 144
The 12th term, F_{12}, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

Functions:
None
'''

__date__ = "30 January 2020"

# Notes:
#
# Modified Problem 2. Note that the terms aproach a common factor of e.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p25(digits: int = 1_000):
  """The solution.
  """
  limit = 10**(digits - 1)
  result = 3
  a, b = 1, 2
  while b < limit:
    result += 1
    a, b = b, a + b
  return (result)


def p25alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p25())
