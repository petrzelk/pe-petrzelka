#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 73: Counting Fractions in a Range

Problem Description:
Consider the fraction, frac n d, where n and d are positive integers. If n < d and
{HCF}(n, d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we
get:
frac 1 8, frac 1 7, frac 1 6, frac 1 5, frac 1 4, frac 2 7, frac 1 3, {frac 3 8},
frac 2 5, frac 3 7}, frac 1 2, frac 4 7, frac 3 5, frac 5 8, frac 2 3, frac 5 7,
frac 3 4, frac 4 5, frac 5 6, frac 6 7, frac 7 8
It can be seen that there are 3 fractions between frac 1 3 and frac 1 2.
How many fractions lie between frac 1 3 and frac 1 2 in the sorted set of reduced proper
fractions for d <= 12,000?



Functions:
None
'''

__date__ = '10 February 2024'

# Notes:
#
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import gcf

# User defined functions


# Solutions
def p73(limit:int=12000) -> int:
  """The solution.
  """
  result=0
  factors={i:set() for i in range(2,limit+1)}
  for i in range(2,limit+1):
    if not factors[i]:
      for multiple in range(i*2,limit+1,i):
        factors[multiple]|={i}
    coprimes={n for n in range(1,i)}
    for factor in factors[i]:
      coprimes-=set(range(factor,i,factor))
    low=i//3
    high=i//2+i%2
    for num in coprimes:
      #More number are going to be higher
      if num<high and num>low:
        result+=1
  return(result)


def p73alt(limit:int=10000):
  """Alternate solution.
  """
  count=0
  for n in range(5,limit):
    for k in range(n//3+1,(n-1)//2):
      if gcf(n,k) == 1:
        count+=1
  return(count)


# Test cases
print(p73())
