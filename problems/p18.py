#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 18: Maximum Path Sum I

Problem Description:
By starting at the top of the triangle below and moving to adjacent numbers on the row 
below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:
[15 lines hidden]
NOTE: As there are only 16384 routes, it is possible to solve this problem by trying 
every route. However, Problem 67 is the same challenge with a triangle containing 
one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o

Functions:
None
'''

__date__ = "20 January 2020"

# Notes:
#
#


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p18(file_path: str = "..\\resources\\0018_triangle.txt") -> int:
  """The solution.
  """
  with open(os.path.join(os.path.dirname(__file__),file_path), 'r') as file:
    triangle = [[int(j) for j in i.split(' ')]
                for i in file.read().split('\n')]
  for row in range(len(triangle) - 2, -1, -1):
    triangle[row] = [
        triangle[row][i] + max(triangle[row + 1][i:i + 2])
        for i in range(row + 1)
    ]
  return (triangle[0][0])


def p18alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p18())
