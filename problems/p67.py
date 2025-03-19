#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 67: Maximum Path Sum II

Problem Description:
By starting at the top of the triangle below and moving to adjacent numbers on the row
below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom in triangle.txt (right click and 'Save
Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
NOTE: This is a much more difficult version of Problem 18. It isnot possible to try 
every route to solve this problem, as there are 299 altogether! If you could check one
trillion (1012) routes every second it would take over twenty billion years to check 
them all. There is an efficient algorithm to solve it. ;o)


Functions:
None
'''

__date__ = '20 January 2020'

# Notes:
#
# Literally the same solution as 18.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p67(file_path: str = "..\\resources\\0067_triangle.txt") -> int:
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


def p67alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p67())
