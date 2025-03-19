#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 27: Quadratic Primes

Problem Description:
Euler discovered the remarkable quadratic formula:
n**2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive integer values
0 <= n <= 39. However, when n = 40, 40**2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 
41, and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.
The incredible formula n**2 - 79n + 1601 was discovered, which produces 80 primes for 
the consecutive values 0 <= n <= 79. The product of the coefficients, -79 and 1601, is 
-126479.
Considering quadratics of the form:

n**2 + an + b, where |a| < 1000 and |b| <= 1000 
where |n| is the modulus/absolute value of n 
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that 
produces the maximum number of primes for consecutive values of n, starting with n = 0.

Functions:
sqrt
product
primes
is_prime
'''

__date__ = "25 April 2023"

# Notes:
#
# For n=0 to be prime, b must be prime. Find the primes to the limit and only check for 
# b as an element of this set. Secondly, except for b=2, for n=1 to also be prime, then
# a must be odd, else n=1 will be even thus divisible by two and not prime.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import is_prime, primes, product

# User defined functions


# Solutions
def p27(limit:int=1_000) -> int:
  """The solution.
  """
  if limit%2==1:
    limit+=1
  result=[1,1,1]
  for a,b in ((a,b) for a in range(-limit+1,limit,2) for b in primes(limit)):
    n=1
    prime_candidate = n**2 + a*n + b
    while prime_candidate > 0 and is_prime(prime_candidate):
      n+=1
      prime_candidate = n**2 + a*n + b
    if n>result[0]:
      result=[n,a,b]
  return(product(tuple(result[1:])))
    

def p27alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p27())
