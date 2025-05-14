#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 79: Passcode Derivation

Problem Description:
A common security method used for online banking is to ask the user for three random
characters from a passcode. For example, if the passcode was 531278, they may ask for
the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
The text file, <a href="resources/documents/0079_keylog.txt">keylog.txt, contains fifty
successful login attempts.
Given that the three characters are always asked for in order, analyse the file so as to
determine the shortest possible secret passcode of unknown length.


Functions:
None
'''

__date__ = '2 March 2024'

# Notes:
#
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p79(file_path: str = "..\\resources\\0079_keylog.txt") -> int:
  """The solution.
  """
  with open(os.path.join(os.path.dirname(__file__),file_path), 'r') as file:
    keys = file.read().split()
  possible, notPossible = set(), set()
  result=""
  while False in [i=="" for i in keys]:
    for index in range(len(keys)):
      if result and keys[index] and keys[index][0] == result[-1]:
        keys[index]=keys[index][1:]
      first = True
      for num in keys[index]:
        if first:
          possible.add(num)
          first = False
        else:
          notPossible.add(num)
    if possible:
      result += (possible-notPossible).pop()
    possible, notPossible = set(), set()
        
  return(result)


def p79alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p79())
