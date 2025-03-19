#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 72: Counting Fractions

Problem Description:
Consider the fraction, frac n d, where n and d are positive integers. If n < d and
{HCF}(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we
get:
frac 1 8, frac 1 7, frac 1 6, frac 1 5, frac 1 4, frac 2 7, frac 1 3, frac 3 8,
frac 2 5, frac 3 7, frac 1 2, frac 4 7, frac 3 5, frac 5 8, frac 2 3, frac 5 7,
frac 3 4, frac 4 5, frac 5 6, frac 6 7, frac 7 8
It can be seen that there are 21 elements in this set.
How many elements would be contained in the set of reduced proper fractions for d <=
1,000,000?


Functions:
primes, phi
'''

__date__ = '10 February 2024'

# Notes:
#
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import primes, phi

# User defined functions


# Solutions
def p72(d=1_000_000) -> int:
  """The solution.
  """
  def add_phi(n:int,index_1:int):
    for index_2 in range(index_1+1):
      prime=prime_list[index_2]
      if n*prime>d:
        break
      elif n*prime in phi_counts:
        pass
      #Are n and prime reltively prime?
      elif n % prime == 0:
        phi_counts[n*prime] = prime * phi_counts[n]
        add_phi(n*prime,index_1)
      else:
        phi_counts[n*prime] = (prime - 1) * phi_counts[n]
        add_phi(n*prime,index_1)
  phi_counts={}
  prime_list=primes(d+1)
  for index in range(len(prime_list)):
    phi_counts[prime_list[index]]=prime_list[index]-1
    add_phi(prime_list[index],index)
  return(sum(phi_counts.values()))
  

def p72alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p72())
