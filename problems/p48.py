#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 48: Self Powers

Problem Description:
The series, 1**1 + 2**2 + 3**3 + ... + 10**{10} = 10405071317.
Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**{1000}.

Functions:
None
'''

__date__ = "8 September 2023"

# Notes:
#
#


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p48(n: int = 1_000) -> int:
  """The solution.
  """
  result = 0
  for i in range(1, n + 1):
    result += i**i
  return (result % (10**10))


def p48alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p48())
