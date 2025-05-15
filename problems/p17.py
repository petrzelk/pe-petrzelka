#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 17: Number Letter Counts

Problem Description:
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there 
are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used? 
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of 
"and" when writing out numbers is in compliance with British usage.

Functions:
None
'''

__date__ = "16 July 2020"

# Notes:
#
#


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions
def int_to_str(n:int)->str:
  '''Takes an integer from 1-1000 inclusive and returns the spoken version of the 
  number as a string.
  '''
  digits={'1':'one',
          '2':'two',
          '3':'three',
          '4':'four',
          '5':'five',
          '6':'six',
          '7':'seven',
          '8':'eight',
          '9':'nine'}
  teens={'0':'ten',
          '1':'eleven',
          '2':'twelve',
          '3':'thirteen',
          '4':'fourteen',
          '5':'fifteen',
          '6':'sixteen',
          '7':'seventeen',
          '8':'eighteen',
          '9':'nineteen'}
  tens={'1':'ten',
          '2':'twenty',
          '3':'thirty',
          '4':'forty',
          '5':'fifty',
          '6':'sixty',
          '7':'seventy',
          '8':'eighty',
          '9':'ninety'}
  result=''
  number=str(n)
  if len(number)==4 and number[0]!='0':
    result += digits[number[0]]+' thousand '
    number = number[1:]
  if len(number)==3 and number[0]!='0':
    result += digits[number[0]]+' hundred '
    number=number[1:]
  if n//100 > 0 and n%100 > 0:
    result+='and '
  if len(number)==2:
    if number[0] == '1':
      result += teens[number[1]]+' '
      number = number[1:]
    elif number[0] != '0':
      result += tens[number[0]]+' '
    number = number[1:]
  if len(number)==1 and number[0]!='0':
    result += digits[number[0]]+' '
    number = number[1:]
  return(result[:-1])
  
  
  

# Solutions
def p17(limit:int=1000)->int:
  """The solution.
  """
  result=0
  for i in range(1,limit+1):
    print(i, int_to_str(i))
    result += len(int_to_str(i).replace(' ',''))
  return result


def p17alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p17())
