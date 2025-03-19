#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 20: Factorial Digit Sum

Problem Description:
n! means n * (n - 1) * ... * 3 * 2 * 1.
For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800, and the sum of the digits in the 
number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!.

Functions:
factorial
'''

__date__ = "20 Jan 2020"

# Notes:
#
# Again a problem made trivial by python.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import factorial

# User defined functions


# Solutions
def p20(n: int = factorial(100)) -> int:
  """The solution.
  """
  return (sum(int(i) for i in str(n)))


def p20alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p20())
