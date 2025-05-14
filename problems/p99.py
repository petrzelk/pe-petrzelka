#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 99: Largest Exponential

Problem Description:
Comparing two numbers written in index form like 2**{11} and 3**7 is not difficult, as
any calculator would confirm that 2**{11} = 2048 < 3**7 = 2187.
However, confirming that 632382**{518061} > 519432**{525806} would be much more
difficult, as both numbers contain over three million digits.
Using <a href="resources/documents/0099_base_exp.txt">base_exp.txt (right click and
'Save Link/Target As...'), a 22K text file containing one thousand lines with a
base/exponent pair on each line, determine which line number has the greatest numerical
value.
NOTE: The first two lines in the file represent the numbers in the example given above.


Functions:
None
'''

__date__ = '30 May 2024'

# Notes:
#
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p99(file_path: str = "..\\resources\\0099_base_exp.txt") -> int:
  """The solution.
  """
  with open(os.path.join(os.path.dirname(__file__),file_path), 'r') as file:
    numbers=[[int(j) for j in i.split(",")] for i in file.read().split("\n")]
  result=[1,1]
  for num in numbers:
    if num[0]>=result[0]**(result[1]/num[1]):
      result= num
  return(numbers.index(result)+1)

def p99alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p99())
