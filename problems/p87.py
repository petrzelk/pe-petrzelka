#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 87: Prime Power Triples

Problem Description:
The smallest number expressible as the sum of a prime square, prime cube, and prime
fourth power is 28. In fact, there are exactly four numbers below fifty that can be
expressed in such a way:

28 = 2**2 + 2**3 + 2**4
33 = 3**2 + 2**3 + 2**4
49 = 5**2 + 2**3 + 2**4
47 = 2**2 + 3**3 + 2**4

How many numbers below fifty million can be expressed as the sum of a prime square,
prime cube, and prime fourth power?


Functions:
None
'''

__date__ = '6 April 2024'

# Notes:
#
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p87(limit: int = 50_000_000) -> int:
  """The solution.
  """
  prime_list=primes(int(sqrt(limit-24)))
  result=set()

  for a in prime_list:
        for b in prime_list:
            for c in prime_list:
                number=a**2+b**3+c**4
                if number<limit:
                    result.add(number)
                else:
                    break
        #if a**2+b**3+c**4>=limit:
            #break

  return(len(result))


def p87alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p87())
