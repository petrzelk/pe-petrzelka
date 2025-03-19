#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 71: Ordered Fractions

Problem Description:
Consider the fraction, \dfrac n d, where n and d are positive integers. If n < d and
\operatorname{HCF}(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we
get:
\frac 1 8, \frac 1 7, \frac 1 6, \frac 1 5, \frac 1 4, \frac 2 7, \frac 1 3, \frac 3 8,
{\frac 2 5}, \frac 3 7, \frac 1 2, \frac 4 7, \frac 3 5, \frac 5 8, \frac 2 3, \frac 5
7, \frac 3 4, \frac 4 5, \frac 5 6, \frac 6 7, \frac 7 8
It can be seen that \dfrac 2 5 is the fraction immediately to the left of \dfrac 3 7.
By listing the set of reduced proper fractions for d <= 1,000,000 in ascending order of
size, find the numerator of the fraction immediately to the left of \dfrac 3 7.


Functions:
None
'''

__date__ = 'DATE'

# Notes:
#
# 


# Import statments
#from project_euler_functions import *
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.matrix import matrix

# User defined functions


# Solutions
def p71() -> int:
  """The solution.
  """
  pass


def p71alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p71())
print(matrix([[1,2],[2,3,1]]))