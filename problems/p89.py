#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 89: Roman Numerals

Problem Description:
For a number written in Roman numerals to be considered valid there are basic rules
which must be followed. Even though the rules allow some numbers to be expressed in more
than one way there is always a "best" way of writing a particular number.
For example, it would appear that there are at least six ways of writing the number
sixteen:
IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI
However, according to the rules only XIIIIII and XVI are valid, and the last example is
considered to be the most efficient, as it uses the least number of numerals.
The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one 
thousand numbers written in valid, but not necessarily minimal, Roman numerals; see 
About... Roman Numerals for the definitive rules for this problem.
Find the number of characters saved by writing each of these in their minimal form.
Note: You can assume that all the Roman numerals in the file contain no more than four
consecutive identical units.


Functions:
None
'''

__date__ = '18 April 2024'

# Notes:
# Only need to create an encoder and decoder and then the
# following work is trivial.
# 
# A faster, less fun, way of doing this is just searching 
# for sequences that could be condensed.
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p89(file_path: str = "..\\resources\\0089_roman.txt") -> int:
  """The solution.
  """
  with open(os.path.join(os.path.dirname(__file__),file_path), 'r') as file:
    numerals=file.read().split()
  result=0
  for line in numerals:
    result+=len(line)-len(int_to_roman(roman_to_int(line)))
  return(result)


def p89alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p89())
