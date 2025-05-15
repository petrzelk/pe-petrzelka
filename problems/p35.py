#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 35: Circular Primes

Problem Description:
The number, 197, is called a circular prime because all rotations of the digits: 197, 
971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 
and 97.
How many circular primes are there below one million?

Functions:
None
'''

__date__ = "27 April 2023"

# Notes:
#
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions
def rotate_str(string:str,degree:int)->str:
  return string[-degree%len(string):]+string[:-degree%len(string)]

def rotate_int(integer:int,degree:int)->int:
  return int(rotate_str(str(integer),degree))

# Solutions
def p35(limit=1_000_000):
  """The solution.
  """
  result=0
  prime_set=set(primes(limit))
  for prime in prime_set:
    result+= all(is_prime(rotate_int(prime,degree)) 
           for degree in range(1,len(str(prime))))
  return(result)


def p35alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p35())
