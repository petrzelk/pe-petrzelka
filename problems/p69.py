#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 69: Totient Maximum

Problem Description:
Euler's totient function, phi(n) [sometimes called the phi function], is defined as the
number of positive integers not exceeding n which are relatively prime to n. For
example, as 1, 2, 4, 5, 7, and 8, are all less than or equal to nine and relatively
prime to nine, phi(9)=6.

n  Relatively Prime phi(n) n/phi(n)
2  1                1      2
3  1,2              2      1.5
4  1,3              2      2
5  1,2,3,4          4      1.25
6  1,5              2      3
7  1,2,3,4,5,6      6      1.1666...
8  1,3,7            4      2
9  1,2,4,5,7,8      6      1.5
10 1,3,7,9          4      2.5

It can be seen that n = 6 produces a maximum n/phi(n) for n<=q 10.
Find the value of n<=q 1,000,000 for which n/phi(n) is a maximum.


Functions:
None
'''

__date__ = '25 January 2024'

# Notes:
#
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p69() -> int:
  """The solution.
  """
  pass


def p69alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p69())
