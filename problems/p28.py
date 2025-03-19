#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 28: Number Spiral Diagonals

Problem Description:
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 
spiral is formed as follows:
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the 
same way?

Functions:
constant_sum
linear_sum
quadratic_sum
'''

__date__ = "25 April 2023"

# Notes:
#
# The North East is easily shown to be quadratic, being (2*n+1)**2 where
#                    0 <= n <= limit//2
# The North West is less easy to see (2*n+1)**2-2*n with the same n
# The South West is (2*n+1)**2-4*n
# The South East is (2*n+1)**2-6*n
# The sum of these, for each ring, is 4*(2*n+1)**2-12*n


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import constant_sum, linear_sum, quad_sum

# User defined functions


# Solutions
def p28(box_size: int = 1_001) -> int:
  """The solution.
  """
  # Start with the center
  result = 1
  # Add each ring
  for n in range(1, (box_size - 1) // 2 + 1):
    result += 4 * (2 * n + 1)**2 - 12 * n
  # Not actually necessary for the problem, just feels complete
  if box_size % 2 == 0:
    result += (2 * ((box_size + 1) // 2) + 1)**2 - 6 * ((box_size + 1) // 2)
  return (result)


def p28alt(limit: int = 1_001) -> int:
  """Alternate solution.
  """
  # Could express this as -3 + the sum from 0 to limit//2 of 16*n**2+4*n+4
  n = limit // 2
  if limit % 2 == 1:
    return (-3 + quad_sum(n, 16) + linear_sum(n, 4) + constant_sum(n + 1, 4))
  # Again, not necessary for the problem, but for completeness
  else:
    limit -= 1
    return (-3 + quad_sum(n, 16) + linear_sum(n, 4) + constant_sum(n + 1, 4) -
            (3 * (2 * n + 1)**2 - 6 * n))


def p28alt2(limit: int = 1_001) -> int:
  """Second alternate solution.
  """
  n = limit // 2
  #Simplified the algebraic expressions from above.
  return ((16 * n**3 + 30 * n**2 + 26 * n + 3) // 3 -
          #Completeness clause
          ((limit + 1) % 2) * (12 * n**2 + 6 * n + 3))


# Test cases
print(p28alt2())
