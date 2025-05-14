#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 92: Square Digit Chains

Problem Description:
A number chain is created by continuously adding the square of the digits in a number to
form a new number until it has been seen before.
For example,

44 -> 32 -> 13 -> 10 ->  1 ->  1
85 -> {89} -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> {89}

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What
is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
How many starting numbers below ten million will arrive at 89?


Functions:
None
'''

__date__ = '10 May 2024'

# Notes:
#
# Easy mode. No comment. Slow code.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p92(magnitude:int = 7) -> int:
  """The solution.
  """
  limit=10**magnitude
  result=3
  bitarray={1:False,4:True}
  for num in range(1,9**2*magnitude+1):
    to_add={num}
    while num not in bitarray:
      num=square_digital_sum(num)
      to_add.add(num)
    value=bitarray[num]
    for key in to_add:
      bitarray[key]=value
    if value:
      result+=1
    #print(init_num)
  
  # future improvement would be working the math to find the number of numbers 
  # that would give 1 to 9**2*magnitude as an answer rather than iterating over them.
  for num in range(9**2*magnitude+1,limit):
    result+=bitarray[square_digital_sum(num)]
  return(result)


def p92alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p92())
