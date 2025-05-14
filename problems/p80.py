#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 80: Square Root Digital Expansion

Problem Description:
It is well known that if the square root of a natural number is not an integer, then it
is irrational. The decimal expansion of such square roots is infinite without any
repeating pattern at all.
The square root of two is 1.41421356237309504880..., and the digital sum of the first
one hundred decimal digits is 475.
For the first one hundred natural numbers, find the total of the digital sums of the
first one hundred decimal digits for all the irrational square roots.


Functions:
None
'''

__date__ = '6 March 2024'

# Notes:
#
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions
def trunc_sqrt(n: int|float) -> int:
    approx=1
    while (approx+1)**2<=n:
        approx+=1
    return(approx)

def int_sqrt(n: int|float, degree: int = 17) -> int:
    approx: int = 1
    while (approx+1)**2 <= n:
        approx += 1
    approx *= 10**degree
    n = int(n*10**(degree*2))
    nextapprox = (approx+n//approx)//2
    while approx != nextapprox:
        approx, nextapprox = nextapprox, (nextapprox+n//nextapprox)//2
    return(approx)

# Solutions
def p80(n: int = 100) -> int:
  """The solution.
  """
  result: int = 0
  for j in range(1, n+1):
    if j != trunc_sqrt(j)**2:
      for i in str(int_sqrt(j,100))[:-1]:
        result += int(i)
  return (result)


def p80alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p80())
