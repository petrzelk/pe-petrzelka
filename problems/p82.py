#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 82: Path Sum: Three Ways

Problem Description:
<p class="small_notice">NOTE: This problem is a more challenging version of <a
href="problem=81">Problem 81.
The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left
column and finishing in any cell in the right column, and only moving up, down, and
right, is indicated in red and bold; the sum is equal to 994.

131  673  {234}  {103}  {18}
{201}  {96}  {342}  965  150
630  803  746  422  111
537  699  497  121  956
805  732  524  37  331

Find the minimal path sum from the left column to the right column in <a
href="resources/documents/0082_matrix.txt">matrix.txt (right click and "Save Link/Target
As..."), a 31K text file containing an 80 by 80 matrix.

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
def p82(file_path: str = "..\\resources\\0082_matrix.txt") -> int:
  """The solution.
  """
  with open(os.path.join(os.path.dirname(__file__),file_path), 'r') as file:
    test:       list[list[int]] = [[int(value) for value in row.split(",")] for row in file.read().split("\n")]
    
  result:     list[list[int]] = array2d(len(test),len(test[0]))
  live:       set[tuple[int]] = {(i,len(test[1])-2) for i in range(len(test))}
  growth:     set[tuple[int]] = set()
  directions: set[tuple[int]] = {(-1,0),(0,-1),(1,0)}

  for index in range(len(result)):
    result[index][-2] = sum(test[index][-2:])
    
  while len(live) != 0:
        
    for index in live:
            
      for move in directions:
        current = (index[0]+move[0], index[1]+move[1])\
                          
        if (
          current[0] in range(len(test))
          and current[1] in range(len(test[0]))
          and (
            result[current[0]][current[1]]==0
            or result[current[0]][current[1]] > test[current[0]][current[1]] + result[index[0]][index[1]]
            )
        ):
                    
          result[current[0]][current[1]] = test[current[0]][current[1]] + result[index[0]][index[1]]
          target=result[current[0]][current[1]]+1
          for row in result:
            if row[0] != 0 and row[0] < target:
              target=row[0]
                            
          if target > result[current[0]][current[1]]:
            growth.add(current)

    live, growth = growth, set()
        
  return( min({i[0] for i in result}) )

def p82alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p82())
