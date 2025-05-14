#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 97: Large Non-Mersenne Prime

Problem Description:
The first known prime found to exceed one million digits was discovered in 1999, and is
a Mersenne prime of the form 2**{6972593} - 1; it contains exactly 2,098,960 digits.
Subsequently other Mersenne primes, of the form 2**p - 1, have been found which contain
more digits.
However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207
digits: 28433 * 2**{7830457} + 1.
Find the last ten digits of this prime number.


Functions:
None
'''

__date__ = '13 May 2024'

# Notes:
#
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions
def large_exp_trunc(b: int = 2, x:int = 7830457, n: int = 10):
  n=10**n
  powers={}
  exponent=1
  while exponent<x:
    powers|={exponent:b}
    b=(b**2)%(n)
    exponent*=2
  exponent//=2
  result=1
  while exponent>=1:
    if x>=exponent:
      x-=exponent
      result=(result*powers[exponent])%n
    exponent//=2
  return(result)

# Solutions
def p97(n:int=10) -> int:
  """The solution.
  """
  result=large_exp_trunc(2,7830457,n)
  result*=28433
  result%=(10**n)
  result+=1
  return(result)


def p97alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p97())
