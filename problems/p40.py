#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 40: Champernowne's Constant

Problem Description:
An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If d_n represents the nth digit of the fractional part, find the value of the following
expression.
d_1 * d_{10} * d_{100} * d_{1000} * d_{10000} * d_{100000} * d_{1000000}

Functions:
None
'''

__date__ = "6 September 2023"

# Notes:
#
#


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p40() -> int:
  """The solution.
  """
  champernownes = "".join([str(i) for i in range(200_000)])
  result = 1
  for i in range(7):
    result *= int(champernownes[10**i])
  return (result)


def p40alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p40())
