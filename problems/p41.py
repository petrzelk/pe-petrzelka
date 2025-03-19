#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 41: Pandigital Prime

Problem Description:
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to
n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?

Functions:
sqrt
perms
concat
is_prime
'''

__date__ = "9 September 2023"

# Notes:
#
# 9-digit and 8-digit pandigital numbers are all divisible by 3,
# following the 3 divisibility rule. The sums of their digits
# would be 36 and 45 respectively. This has time savings by a factor
# of about 40 times.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import concat, is_prime, perms

# User defined functions


# Solutions
def p41(limit: int = 7) -> int:
  """The solution.
  """
  result = []
  for perm in [
      i for length in range(1, limit + 1)
      for i in perms(list(range(1, length + 1)))
  ]:
    if is_prime(int(concat(perm))):
      result.append(int(concat(perm)))
  return (max(result))


def p41alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p41())
