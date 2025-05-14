#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 77: Prime Summations

Problem Description:
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand
different ways?


Functions:
None
'''

__date__ = '25 February 2024'

# Notes:
#
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions
def primePartition(n,end,primes):
    if n == 0 :
        return(1)
    if n == 1 :
        return(0)
    result=0
    for i in range(end,-1,-1):
        p=primes[i]
        if p <= n:
            result += primePartition(n-p,i,primes)
        #print("For",n,"at",p,"there are",result,"solutions")
        #input()
    return(result)

def nextPrime(primes):
    n=primes[-1]+2
    while True:
        result=True
        for p in primes:
            if n%p==0:
                result=False
                break
        if result:
            return(n)
        n+=2

# Solutions
def p77(limit:int=5000) -> int:
  """The solution.
  """
  #generate the primes
  primes=[2,3]

  n=2
  while primePartition(n,len(primes)-2,primes)<=limit:
        
        n+=1
        if primes[-1]<=n:
            primes.append(nextPrime(primes))
        
  return(n)


def p77alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p77())
