#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 32: Pandigital Products

Problem Description:
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to
n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, 
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be 
written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it 
once in your sum.

Functions:
is_pandigital
perms
'''

__date__ = "26 April 2023"

# Notes:
#
# The first solution is brute forced. The alternate solution has the following bounds
# applied:
# - The multicand and multiplier need four digits at least since the could not produce a
#      product large enough to be pandigital.
# - The multiple cant be smaller than four digits as the product of the multicand and
#      multiplier would be much larger.
# These two observations limit the location of the equals sign to range(4,6), halving
# the amount of work to be done.
# - Let the multicand be less than the multiplier.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import is_pandigital, perms

# User defined functions


# Solutions
def p32():
  """The solution.
  """
  result = set()
  for pandigital in perms([str(i) for i in range(1, 10)]):
    for equals in range(2, 9):
      for multiplication in range(1, equals):
        if int(''.join(pandigital[:multiplication])) * int(''.join(
            pandigital[multiplication:equals])) == int(''.join(
                pandigital[equals:])):
          result.add(int(''.join(pandigital[equals:])))
          #print(''.join(pandigital[:multiplication]) + "*" +
          #      ''.join(pandigital[multiplication:equals]) + '=' +
          #      ''.join(pandigital[equals:]))
  return (sum(result))


def p32alt():
  """Alternate solution.
  """
  result = set()
  for pandigital in perms([str(i) for i in range(1, 10)]):
    for equals in range(4, 6):
      for multiplication in range(1, equals // 2 + 1):
        if int(''.join(pandigital[:multiplication])) * int(''.join(
            pandigital[multiplication:equals])) == int(''.join(
                pandigital[equals:])):
          result.add(int(''.join(pandigital[equals:])))
  return (sum(result))


# Test cases
print(p32alt())
