#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 95: Amicable Chains

Problem Description:
The proper divisors of a number are all the divisors excluding the number itself. For
example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors
is equal to 28, we call it a perfect number.
Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper
divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are
called an amicable pair.
Perhaps less well known are longer chains. For example, starting with 12496, we form a
chain of five numbers:
12496 -> 14288 -> 15472 -> 14536 -> 14264 (-> 12496 -> ...)
Since this chain returns to its starting point, it is called an amicable chain.
Find the smallest member of the longest amicable chain with no element exceeding one
million.


Functions:
None
'''

__date__ = '20 May 2024'

# Notes:
#
# First build a function to find the proper divisors of a number. 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions
def divisor_sum(n:int)->int:
  """Takes in and integer n and returns the sum of all numbers that n is divisible by that are less than n."""
  start=n
  #limit=int(sqrt(n))
  result=1
  count=0
  while n%2==0:
    count+=1
    n//=2
  if count:
    result*=(2**(count+1)-1)
    #print(2,count)
  b=3
  while b<=n:
    #print(b)
    count=0
    while n%b==0:
      count+=1
      n//=b
    if count:
      result*=(b**(count+1)-1)//(b-1)
      #print(b,count)
    b+=2
  return(result-start)

def amicable_chain(n:int)->int:
  """Takes in an integer starting point and returns the amicable chain list for numbers greater than n."""
  result=[n]
  next=divisor_sum(n)
  while next>n:
    result+=[next]
    #print(result)
    next=divisor_sum(next)
  return(len(result))

def amicable_chain_limit(n:int, limit:int)->int:
  """Takes in an integer starting point and a limit which the chain cannot exceed then returns the positive amicable chain distance to the first lower or equal value."""
  result=1
  next=divisor_sum(n)
  previous={n}
  while next>n:
    if next>limit or next in previous:
      return(0)
    previous.add(next)
    result+=1
    next=divisor_sum(next)
  if next==n:
    return(result)
  else:
    return(1)

# Solutions
def p95(limit:int = 1_000_000) -> int:
  """The solution.
  """
  result=(1,1)
  for n in range(2,limit):
    if amicable_chain_limit(n,limit)>result[1]:
      result=(n,amicable_chain_limit(n,limit))
  return(result[0])


def p95alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p95())
