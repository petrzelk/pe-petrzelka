#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 31: Coin Sums

Problem Description:
In the United Kingdom the currency is made up of pound (£) and pence (p). There are 
eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:
1*£1 + 1*50p + 2*20p + 1*5p + 1*8p + 3*1p
How many different ways can £2 be made using any number of coins?

Functions:
None
'''

__date__ = "26 April 2023"

# Notes:
#
# Recursive solution is relatively slow but works.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p31(limit = 200, coins = (1,2,5,10,20,50,100,200)):
  """The solution.
  """
  result = 0
  for index in range(len(coins)):
    if limit - coins[index] == 0:
      result+=1
    elif limit - coins[index] > 0:
      result += p31(limit - coins[index], coins[index:])
  return result


def p31alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p31())
