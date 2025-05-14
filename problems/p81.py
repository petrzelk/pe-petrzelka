#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 81: Path Sum: Two Ways

Problem Description:
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
by only moving to the right and down, is indicated in bold red and is equal to 2427.

{131}  673  234  103  18
{201}  {96}  {342}  965  150
630  803  {746}  {422}  111
537  699  497  {121}  956
805  732  524  {37}  {331}

Find the minimal path sum from the top left to the bottom right by only moving right and
down in <a href="resources/documents/0081_matrix.txt">matrix.txt (right click and "Save
Link/Target As..."), a 31K text file containing an 80 by 80 matrix.

Functions:
None
'''

__date__ = '9 March 2024'

# Notes:
#
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions
def array2d(m: int, n: int) -> list[list[int]]:
    sub : list[int] = [0]*n
    result : list[list[int]] = []
    while m > 0:
        result += [sub[:]]
        m-=1
    return(result)

# Solutions
def p81(file_path: str = "..\\resources\\0081_matrix.txt") -> int:
  """The solution.
  """
  with open(os.path.join(os.path.dirname(__file__),file_path), 'r') as file:
    test:       list[list[int]] = [[int(value) for value in row.split(",")] for row in file.read().split("\n")]
    
    
  result:     list[list[int]] = array2d(len(test),len(test[0]))
  live:       set[tuple[int]] = {(len(test)-1,len(test[1])-1)}
  growth:     set[tuple[int]] = set()
  directions: set[tuple[int]] = {(-1,0),(0,-1)}

  result[len(test)-1][len(test[1])-1]=test[len(test)-1][len(test[1])-1]
    
  while len(live) != 0:
        
    for index in live:
            
      for move in directions:
        current = (index[0]+move[0], index[1]+move[1])
                          
        if (
          current[0] in range(len(test))
          and current[1] in range(len(test[0]))
          and (
            result[current[0]][current[1]]==0
            or result[current[0]][current[1]] > test[current[0]][current[1]] + result[index[0]][index[1]]
            )
        ):
                    
          result[current[0]][current[1]] = test[current[0]][current[1]] + result[index[0]][index[1]]
          if result[0][0] == 0 or result[0][0] > result[current[0]][current[1]]:
            growth.add(current)

    live, growth = growth, set()
        
  return( result[0][0] )


def p81alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p81())
