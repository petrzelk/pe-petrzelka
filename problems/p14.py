#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 14: Longest Collatz Sequence

Problem Description:
The following iterative sequence is defined for the set of positive integers:
n -> n/2 (n is even)
n -> 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting 
numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.

Functions:
next_collatz
'''

__date__ = "11 January 2020"

# Notes:
#
# I love this problem.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import next_collatz

# User defined functions


# Solutions
def p14(limit: int = 1_000_000) -> int:
  """The solution.
  """
  map = {1: 1}
  result = 1
  for n in range(1, limit):
    length = 0
    current = n
    while current not in map:
      length += 1
      if current % 2 == 0:
        current //= 2
      else:
        current *= 3
        current += 1
    map[n] = map[current] + length
    if map[n] > map[result]:
      result = n
  return (result)


def p14alt(limit: int = 1_000_000) -> int:
  """Alternate solution.
  """
  map = {1: 1}
  result = 1
  for n in range(1, limit):
    length = 0
    current = n
    while current not in map:
      length += 1
      current = next_collatz(current)
    map[n] = map[current] + length
    if map[n] > map[result]:
      result = n
  return (result)


# Test cases
print(p14alt())
