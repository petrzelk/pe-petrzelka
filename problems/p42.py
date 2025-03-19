#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 42: Coded Triangle Numbers

Problem Description:
The nth term of the sequence of triangle numbers is given by, t_n = (1/2)n(n+1); so the 
first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its alphabetical 
position and adding these values we form a word value. For example, the word value for 
SKY is 19 + 11 + 25 = 55 = t_{10}. If the word value is a triangle number then we shall 
call the word a triangle word.
Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing 
nearly two-thousand common English words, how many are triangle words?

Functions:
is_triangle
letter_value
'''

__date__ = "7 September 2023"

# Notes:
#
#


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import is_triangle, letter_value

# User defined functions


# Solutions
def p42(file_path: str = '..\\resources\\0042_words.txt') -> int:
  """The solution.
  """
  result = 0
  with open(os.path.join(os.path.dirname(__file__),file_path), 'r') as file:
    words = file.read().replace('"', '').split(',')
  for word in words:
    if is_triangle(sum(letter_value(c) for c in word)):
      result += 1
  return (result)


def p42alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p42())
