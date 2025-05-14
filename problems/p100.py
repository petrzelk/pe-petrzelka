#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 100: Arranged Probability

Problem Description:
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red
discs, and two discs were taken at random, it can be seen that the probability of taking
two blue discs, P(BB) = (15/21) * (14/20) = 1/2.
The next such arrangement, for which there is exactly 50% chance of taking two blue
discs at random, is a box containing eighty-five blue discs and thirty-five red discs.
By finding the first arrangement to contain over 10**{12} = 1,000,000,000,000 discs in
total, determine the number of blue discs that the box would contain.


Functions:
None
'''

__date__ = '7 June 2024'

# Notes:
#
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *
from modules.rational import *

# User defined functions


# Solutions
def p100(limit=10**12) -> int:
  """The solution.
  """
  result=[[3,4]]
  n=5
  while result[-1][1]<=limit:
    a=int(sqrt(n**2/2,n))+1
    if rational(a*(a-1),n*(n-1)) == rational(1,2):
      result.append([a,n])
      if len(result)>1:
        n=n**2//result[-2][1]
    n+=1
  return(result[-1][0])


def p100alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p100())
