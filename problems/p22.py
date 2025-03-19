#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 22: Names Scores

Problem Description:
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing 
over five-thousand first names, begin by sorting it into alphabetical order. Then 
working out the alphabetical value for each name, multiply this value by its 
alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 
3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a 
score of 938 * 53 = 49714.
What is the total of all the name scores in the file?

Functions:
None
'''

__date__ = "23 April 2023"

# Notes:
#
# Using pythons ord() and chr() this is fairly easy, along with pythons built in sorting
# functionality


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p22(file_path: str = "..\\resources\\0022_names.txt") -> int:
  """The solution.
  """
  with open(os.path.join(os.path.dirname(__file__),file_path), 'r') as file:
    names = file.read().replace('"', '').split(',')
  names.sort()
  result = 0
  for index in range(len(names)):
    result += (index + 1) * sum(
        ord(character) - 64 for character in names[index])
  return (result)


def p22alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p22())
