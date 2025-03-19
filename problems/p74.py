#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 74: Digit Factorial Chains

Problem Description:
The number 145 is well known for the property that the sum of the factorial of its
digits is equal to 145:
1! + 4! + 5! = 1 + 24 + 120 = 145.
Perhaps less well known is 169, in that it produces the longest chain of numbers that
link back to 169; it turns out that there are only three such loops that exist:

169 -> 363601 -> 1454 -> 169
871 -> 45361 -> 871
872 -> 45362 -> 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a
loop. For example,

69 -> 363600 -> 1454 -> 169 -> 363601 (-> 1454)
78 -> 45360 -> 871 -> 45361 (-> 871)
540 -> 145 (-> 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest
non-repeating chain with a starting number below one million is sixty terms.
How many chains, with a starting number below one million, contain exactly sixty
non-repeating terms?


Functions:
digital_sum, factorial
'''

__date__ = '12 February 2024'

# Notes:
#
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import digital_sum, factorial

# User defined functions
def digit_factorial_sum(n:int)->int:
  result=0
  for d in str(n):
      result+=factorial(int(d))
  return(result)

def loop_length(n:int)->int:
  loop=set()
  while n not in loop:
    loop.add(n)
    n=digit_factorial_sum(n)
  return(len(loop))
  
# Solutions
def p74(limit:int=1_000_000,target:int=60) -> int:
  """The solution.
  """
  result=0
  for i in range(1,limit+1):
    if loop_length(i)==target:
      result+=1
      #print(i)
  return(result)


def p74alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p74())
