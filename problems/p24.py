#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 24: Lexicographic Permutations

Problem Description:
A permutation is an ordered arrangement of objects. For example, 3124 is one possible
permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed 
numerically or alphabetically, we call it lexicographic order. The lexicographic 
permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 
and 9?

Functions:
factorial
'''

__date__ = "24 April 2023"

# Notes:
#
# The solution is a recursive function that just figures out what the first element of 
# the item would be and passes the remaining work back into the function.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import factorial

# User defined functions


# Solutions
def p24(n: int = 1_000_000, items: None|list[int|str] = None) -> int|str:
  """The solution.
  """
  if items is None:
    items = list(range(10))
  def process(n: int, items: list[str]) -> str:
    if items:
      per_item=factorial(len(items) - 1 )
      item = items.pop(n // per_item)
      return (item + process(n % per_item, items))
    else:
      return ('')
  if any(isinstance(i,str) for i in items):
    return (process(n-1, [str(i) for i in items]))
  else:
    return (int(process(n-1, [str(i) for i in items])))


def p24alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p24())
