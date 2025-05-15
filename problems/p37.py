#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 37: Truncatable Primes

Problem Description:
The number 3797 has an interesting property. Being prime itself, it is possible to 
continuously remove digits from left to right, and remain prime at each stage: 3797, 
797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and 
right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

Functions:
None
'''

__date__ = "27 April 2023"

# Notes:
#
#


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import is_prime

# User defined functions


# Solutions
def p37():
  """The solution.
  """
  n = 11
  result = []
  while len(result) < 11:
    if all(is_prime(int(str(n)[:length])) for length in range(1, len(str(n)))) and (
       all(is_prime(int(str(n)[start:])) for start in range(len(str(n))))) and (
         str(n)[0]!='1' and str(n)[-1]!='1'):
      result.append(n)
      #print(n)
    n += 2
  return (sum(result))


def p37alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p37())
