#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 93: Arithmetic Expressions

Problem Description:
By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of
the four arithmetic operations (+, -, *, /) and brackets/parentheses, it is possible to
form different positive integer targets.
For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) - 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.
Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target
numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained
before encountering the first non-expressible number.
Find the set of four distinct digits, a < b < c < d, for which the longest set of
consecutive positive integers, 1 to n, can be obtained, giving your answer as a string:
abcd.


Functions:
None
'''

__date__ = '14 May 2024'

# Notes:
#
# To deal with grouping, for each permutation of numbers, we will build a bit-array 
# that represents which values can be made. When a value is made simply make that 
# value of the array true. For each permutation of the starting numbers, take each 
# possible operation and compute it. then take the remaining numbers and operations 
# and compute them.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions
def is_int(n:int|float)->bool:
  return bool(isinstance(n, int) or n == int(n))

def a_combos(values:list[int|float])->list[int|float]:
  if len(values)==1:
    if is_int(values[0]):
      return(values)
    else:
      return([])
  result=[]
  for pos in range(len(values)-1):
    first=values[:pos]
    last=values[pos+2:]
    num1=values[pos]
    num2=values[pos+1]
    result+=a_combos(first+[num1+num2]+last)
    if num2<num1:
      result+=a_combos(first+[num1-num2]+last)
    result+=a_combos(first+[num1*num2]+last)
    if num2>0:
      result+=a_combos(first+[num1/num2]+last)
  return(result)

def outcomes(string:str)->set[int|float]:
  result=set()
  for perm in perms(list(string)):
    num_list:list[int|float]=[int(i) for i in ''.join(perm)]
    result|=set(a_combos(num_list))
  return(result)

def consec_expr(string:str)->int:
  possible=outcomes(string)
  x=1
  while x+1 in possible:
    x+=1
  return(x)

# Solutions
def p93(limit:int=10) -> int:
  """The solution.
  """
  best=["",0]
  for candidate in [str(a)+str(b)+str(c)+str(d) 
                    for a in range(limit) 
                    for b in range(a+1,limit) 
                    for c in range(b+1,limit) 
                    for d in range(c+1,limit)]:
    
    if best[1]<consec_expr(candidate):
      best=[candidate,consec_expr(candidate)]
  return(int(best[0]))
  


def p93alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p93())
