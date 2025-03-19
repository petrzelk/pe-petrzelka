#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 58: Spiral Primes

Problem Description:
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with
side length 7 is formed.
37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49
It is interesting to note that the odd squares lie along the bottom right diagonal, but
what is more interesting is that 8 out of the 13 numbers lying along both diagonals are
prime; that is, a ratio of 8/13 ~ 62%.
If one complete new layer is wrapped around the spiral above, a square spiral with side
length 9 will be formed. If this process is continued, what is the side length of the
square spiral for which the ratio of primes along both diagonals first falls below 10%?

Functions:
None
'''

__date__ = '12 September 2023'

# Notes:
#
#


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import is_prime

# User defined functions


# Solutions
def p58() -> int:
  """The solution.
  """
  result = 3
  n = 3
  while 10 * result >= 2 * n - 1:
    n += 2
    test = n**2 - n + 1
    if is_prime(test):
      result += 1
    test += 1 - n
    if is_prime(test):
      result += 1
    test += 1 - n
    if is_prime(test):
      result += 1
  return (n)


def p58alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p58())
