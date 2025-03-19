#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 53: Combinatoric Selections

Problem Description:
There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
In combinatorics, we use the notation, 5C3 = 10.
In general, nCr = n!/(r!(n-r)!), where r <= n, n! = n * (n-1) * ... * 3 * 2 *1, 
and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
How many, not necessarily distinct, values of nCr for 1 <= n <= 100, are greater than
one-million?

Functions:
None
'''

__date__ = '9 September 2023'

# Notes:
#
#


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p53(rows: int = 100, cap: int = 1_000_000) -> int:
  """The solution.
  """
  #using the definition of nCr, it is analagous to pascals triangle,
  #where n is the row of the triangle and r is term number in that row.
  n = 0
  row = [1]
  #result tracks the number of terms over a million.
  result = [0]
  #We only track the first half of the row, as it is symmetric.
  #The length of this half is n//2+1. We will proceed row by row.
  while n <= rows - 1:
    #begin by advancing the row number.
    n += 1
    #first we need to know if we need to prepend the "double" value.
    if n % 2 == 0 and not result[-1]:
      row = [row[0]] + row
    #to match the row list we need to generate the new list.
    for i in range(len(row) - 1):
      row[i] = sum(row[i:i + 2])
    #check to see if the list has a new term over one-million.
    if row[0] > cap:
      #remove the term over one-million
      row = row[1:]
      #if it is the first time, it might be a single, center number
      if not (len(result) - 1) and not n % 2:
        result += [1]
      #otherwise this is a pair
      else:
        result += [2]
      #check for an add any additional leading values greater than one-million
      while row[0] > cap:
        row = row[1:]
        result[-1] += 2
      #add on the number of values from the prior row
      if result[-2]:
        result[-1] += result[-2] + 1
    #if values have been stored in the result then we need to move them up
    elif result[-1]:
      result += [result[-1] + 1]
  #return the total count
  return (sum(result))


def p53alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p53())
