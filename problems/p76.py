#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 76: Counting Summations

Problem Description:
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive
integers?


Functions:
None
'''

__date__ = '25 February 2024'

# Notes:
#
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import partitions

# User defined functions


# Solutions
def p76(n=100) -> int:
  """The solution.
  """
  return(partitions(n)-1)


def p76alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p76())
