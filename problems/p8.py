#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 8: Largest Product in a Series

Problem Description:
The four adjacent digits in the 1000-digit number that have the greatest product are 
9 * 9 * 8 * 9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number that have the greatest 
product. What is the value of this product?

Functions:
product
'''

__date__ = "20 December 2019"

# Notes:
#
# This problem is short enough that any optimizations are a waste of time. The easiest 
# of these would be checking to see if there is a zero in the string to pre-emptively 
# rule it out. In fact we can rule out the next n strings if the zero is in the final 
# position of the current selection.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import product

# User defined functions


# Solutions
def p8(n: int = 13, file_path: str = "..\\resources\\0008_number.txt") -> int:
  """The solution.
  """
  with open(os.path.join(os.path.dirname(__file__),file_path), 'r') as file:
    number = file.read().replace('\n', '')
  result = 0
  for i in range(len(number) - n):
    result = max(result, product(tuple(int(x) for x in number[i:i + n])))
  return (result)


def p8alt(n: int = 13, file_path: str = "..\\resources\\0008_number.txt") -> int:
  """Alternate solution.
  """
  with open(os.path.join(os.path.dirname(__file__),file_path), 'r') as file:
    number = file.read().replace('\n', '')
  result = 0
  for i in range(len(number) - n):
    if "0" not in number[i:i + n]:
      result = max(result, product(tuple(int(x) for x in number[i:i + n])))
  return (result)


# Test cases
print(p8())
