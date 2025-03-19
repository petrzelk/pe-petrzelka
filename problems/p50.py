#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 50: Consecutive Prime Sum

Problem Description:
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13.
This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime, contains 
21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive 
primes?

Functions:
primes
'''

__date__ = "8 September 2023"

# Notes:
#
#


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import primes

# User defined functions


# Solutions
def p50(limit: int = 1_000_000) -> int:
  """The solution.
  """
  result = []
  prime_list = primes(limit)
  for i in range(len(prime_list)):
    for j in range(i + 1 + len(result), len(prime_list) - i):
      prime_sum = sum(prime_list[i:j])
      if prime_sum > limit:
        break
      if prime_sum in prime_list:
        result = prime_list[i:j]
  return (sum(result))


def p50alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p50())
