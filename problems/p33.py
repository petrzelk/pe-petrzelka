#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 33: Digit Cancelling Fractions

Problem Description:
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, 
is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in 
value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the 
value of the denominator.

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
def is_equal_fractions(num1,den1,num2,den2):
  return num1*den2 == num2*den1
def common_digit(number1,number2):
  return set(str(number1)) & set(str(number2))
def remove_character_instance(string, character):
  for i in range(len(string)):
    if string[i] == character:
      return string[:i]+string[i+1:]
  return string
def remove_common_digit(number1,number2):
  common = common_digit(number1,number2).pop()
  return int(remove_character_instance(str(number1),common)),int(remove_character_instance(str(number2),common))

# Solutions
def p33():
  """The solution.
  """
  result=(1,1)
  for i,j in ((i,j) for i in range(10,100) for j in range(i,100)):
    factor=gcf(i,j)
    if factor>1 and i%10!=0 and i%11!=0 and len(common_digit(i,j))==1:
      k,l=remove_common_digit(i,j)
      if is_equal_fractions(i,j,k,l):
        result = (result[0]*i,result[1]*j)
        #print(i,j)
  return result[1]//gcf(result[0],result[1])


def p33alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p33())
