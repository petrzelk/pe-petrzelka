#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 49: Prime Permutations

Problem Description:
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-
digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting
this property, but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this sequence?

Functions:
sqrt
primes
perms
concat
'''

__date__ = "8 September 2023"

# Notes:
#
#


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import concat, perms, primes

# User defined functions


# Solutions
def p49() -> int | None:
  """The solution.
  """
  primelist = {n for n in primes(10**4) if n > 10**3}
  for n in primelist:
    candidates = {int(concat(i)) for i in perms(list(str(n)))}
    for m in candidates:
      if n < m and (m - n) + m in candidates and m in primelist and (
          m - n) + m in primelist and n != 1_487:
        return (int(str(n) + str(m) + str((m - n) + m)))


def p49alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p49())
