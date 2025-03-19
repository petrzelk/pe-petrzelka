#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 26: Reciprocal Cycles

Problem Description:
A unit fraction contains 1 in the numerator. The decimal representation of the unit 
fractions with denominators 2 to 10 are given:
1/2 = 0.5
1/3 =0.(3)
1/4 =0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 
1/7 has a 6-digit recurring cycle.
Find the value of d lt 1000 for which 1/d contains the longest recurring cycle in its 
decimal fraction part.

Functions:
vinculum_length
'''

__date__ = "25 April 2023"

# Notes:
#
# You know that you have hit a cycle, not when a decimal repeats, but the remainder
# repeats. This is what I use to drive the unit fraction cycle length function.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import vinculum_length

# User defined functions


# Solutions
def p26(limit: int = 1_000) -> int:
  """The solution.
  """
  result = [1, 1]
  for i in range(2, limit):
    if vinculum_length(i) > result[1]:
      result = [i, vinculum_length(i)]
  return (result[0])


def p26alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p26())
