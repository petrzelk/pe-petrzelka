#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 13: Large Sum

Problem Description:
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
[100 lines hidden]

Functions:
None
'''

__date__ = "20 Jan 2020"

# Notes:
#
# Python makes this problem trivial. The alternate solution makes an attempt an making
# the size of the numbers more managable.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p13(n: int = 10, file_path: str = '..\\resources\\0013_numbers.txt') -> int:
  """The solution.
  """
  with open(os.path.join(os.path.dirname(__file__),file_path), 'r') as file:
    numbers = [int(i) for i in file.read().split("\n")]
  return (int(str(sum(numbers))[:n]))


def p13alt(n: int = 10, file_path: str = '..\\resources\\0013_numbers.txt') -> int:
  """Alternate solution.
  """
  with open(os.path.join(os.path.dirname(__file__),file_path), 'r') as file:
    numbers = [int(i[:n + 1]) for i in file.read().split("\n")]
  return (int(str(sum(numbers))[:n]))


# Test cases
print(p13())
