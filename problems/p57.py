#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 57: Square Root Convergents

Problem Description:
It is possible to show that the square root of two can be expressed as an infinite
continued fraction.

(see problem online)

By expanding this for the first four iterations, we get:

(see problem online)

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 
1393/985, is the first example where the number of digits in the numerator exceeds the 
number of digits in the denominator.
In the first one-thousand expansions, how many fractions contain a numerator with more
digits than the denominator?

Functions:
None
'''

__date__ = '10 September 2023'

# Notes:
#
# Assume that p is the numerator and q is the denominator. 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p57() -> int:
  """The solution.
  """
  result=0
  n=1
  p,q=3,2
  while n<=1000:
      n+=1
      p,q=2*q+p,q+p
      if len(str(p))>len(str(q)):
          result+=1
  return(result)


def p57alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p57())
