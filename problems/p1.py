#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 1: Multiples of 3 or 5

Problem Description:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 
3, 5, 6, and 9. The sum of these multiples is 23. Find the sum of all the multiples of
3 or 5 below 1000.
 
Functions:
linear_sum
gcf
'''

__date__ = "20 December 2019"

# Notes:
# While this problem is so trivial as to not even deserving the 5% rating that it has,
# there is still a certain level of nostalgia when revisiting this problem.
#
# The limit for this problem is so low that using a list comprehension has no effect on
# the speed of the calculation.
#
# A better, still single line solution is shown as an alternative solution. Note that it
# is simply best to do this problem with pen and paper.
#
# A general solution is shown for abitrary multiples m and n.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import gcf, linear_sum

# User defined functions


# Solutions
def p1(limit: int = 1000) -> int:
  """One line solution: readable. Bad for compute and memory usage.
  """
  return (sum([i for i in range(limit) if i % 3 == 0 or i % 5 == 0]))


def p1alt(limit: int = 1000) -> int:
  """Alternate solution, algorithmically better for large n.
  """
  limit -= 1
  #Consider the set A ∪ B = A + B - (A ∩ B)
  return (linear_sum(limit // 3, 3) + linear_sum(limit // 5, 5) -
          linear_sum(limit // 15, 15))


def p1gen(limit: int = 999, factors: tuple[int] | tuple = (3, 5)) -> int:
  """General solution, for arbitrary limit and factors.
  """
  #Consider the set A ∪ B ∪ C... = A + (B ∪ C...) - A ∩ (B ∪ C...)
  if len(factors) > 0:
    f = factors[0]
    # A
    result = linear_sum(limit // f, f)
    # + (B ∪ C...)
    result += p1gen(limit, factors[1:])
    # - A ∩ (B ∪ C...)
    result -= p1gen(limit, tuple(i * f // gcf(i, f) for i in factors[1:]))
    return (result)
  else:
    return (0)


# Test cases
print(p1gen())
