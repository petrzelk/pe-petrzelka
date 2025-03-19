#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 7: 10001st Prime

Problem Description:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th 
prime is 13.
What is the 10001st prime number?

Functions:
sqrt
is_prime
'''

__date__ = "20 December 2019"

# Notes:
#
# The first solution utilizes a nifty prime testing function. The second is just a
# modified prime generator from problem 5 which I came up with just now.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import is_prime, sqrt

# User defined functions


# Solutions
def p7(n: int = 10_001) -> int:
  """The solution.
  """
  counter = 0
  number = 1
  while counter < n:
    number += 1
    if is_prime(number):
      counter += 1
  return (number)


def p7alt(n: int = 10_001) -> int:
  """Alternate solution.
  """
  result = [2]
  i = 3
  while len(result) < n:
    j = 0
    limit = int(sqrt(i))
    prime = True
    while result[j] <= limit:
      if i % result[j] == 0:
        prime = False
        break
      j += 1
    if prime:
      result.append(i)
    i += 2
  return (result[-1])


# Test cases
print(p7alt())
