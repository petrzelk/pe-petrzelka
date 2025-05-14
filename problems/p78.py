#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 78: Coin Partitions

Problem Description:
Let p(n) represent the number of different ways in which n coins can be separated into
piles. For example, five coins can be separated into piles in exactly seven different
ways, so p(5)=7.

OOOOO
OOOO O
OOO OO
OOO O O
OO OO O
OO O O O
O O O O O

Find the least value of n for which p(n) is divisible by one million.


Functions:
None
'''

__date__ = '28 February 2024'

# Notes:
#
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions
def addPart(partitions: dict , n: None | int = None ) -> None:

    #Set up the variables for Euler's Method
    delta : int = 1
    stay : bool = True
    sign : int = 1

    #Find the next part to calculate if it is not given
    if not n:
        n = max( partitions.keys() ) + 1

    #Initialize and store the result and the results key value
    result : int = 0
    resultKey : int = n

    #Started after the first delta operation
    n -= 1

    while n >= 0:

        #Add the current value to the result
        result += sign * partitions[n]

        #Adjust n
        if stay:
            n -= delta
        else:
            delta += 1
            sign *= -1
            n -= delta*2-1

        #Invert the stay value
        stay = not stay

    partitions[resultKey]=result

# Solutions
def p78(factor: int = 1_000_000) -> int:
  """The solution.
  """
  partitions = {0:1}
  n = 0
  while partitions[n]%factor != 0:
    n+=1
    addPart( partitions, n )
  return(n)

def p78alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p78())
