#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 16: Power Digit Sum

Problem Description:
2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2 ** 1000 ?

Functions:
None
'''

__date__ = "11 January 2020"

# Notes:
#
# Python makes this trivial.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p16(n: int = 2**1_000) -> int:
  """The solution.
  """
  return (sum(int(i) for i in str(n)))


def p16alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p16())
