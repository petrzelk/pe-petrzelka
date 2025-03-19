#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 75: Singular Integer Right Triangles

Problem Description:
It turns out that {12 cm} is the smallest length of wire that can be bent to form an
integer sided right angle triangle in exactly one way, but there are many more
examples.

{{12} {cm}}: (3,4,5)
{{24} {cm}}: (6,8,10)
{{30} {cm}}: (5,12,13)
{{36} {cm}}: (9,12,15)
{{40} {cm}}: (8,15,17)
{{48} {cm}}: (12,16,20)
In contrast, some lengths of wire, like {20 cm}, cannot be bent to form an integer sided
right angle triangle, and other lengths allow more than one solution to be found; for
example, using {120 cm} it is possible to form exactly three different integer sided
right angle triangles.

{{120} {cm}}: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L <= 1,500,000 can
exactly one integer sided right angle triangle be formed?


Functions:
None
'''

__date__ = '25 February 2024'

# Notes:
#
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import gcf

# User defined functions


# Solutions
def p75(limit:int=1_500_000) -> int:
  """The solution.
  """
  result, exclude = set(), set()
  m, n, current = 2, 1, 12
  while current <= limit:
    while current <= limit:
      if gcf(m,n) == 1:
        for multiple in range(current, limit+1, current):
          if multiple in result:
            result.remove(multiple)
            exclude.add(multiple)
          elif multiple not in exclude:
            result.add(multiple)
      m += 2
      current = 2*m*(m+n)
    n += 1
    m = n + 1
    current = 2*m*(m+n)
  return(len(result))


def p75alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p75())
