#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 68: Magic 5-gon Ring

Problem Description:
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line
adding to nine.

Working clockwise, and starting from the group of three with the numerically lowest
external node (4,3,2 in this example), each solution can be described uniquely. For
example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.
It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There
are eight solutions in total.

Solution Set
9   4,2,3; 5,3,1; 6,1,2
9   4,3,2; 6,2,1; 5,1,3
10  2,3,5; 4,5,1; 6,1,3
10  2,5,3; 6,3,1; 4,1,5
11  1,4,6; 3,6,2; 5,2,4
11  1,6,4; 5,4,2; 3,2,6
12  1,5,6; 2,6,4; 3,4,5
12  1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum string
for a 3-gon ring is 432621513.
Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and
17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?

Functions:
None
'''

__date__ = '24 January 2024'

# Notes:
#
# The original solution could be better. 
# I made it better. 
# Old solution deleted.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.ring import ring

# User defined functions


# Solutions
def p68(n: int = 5) -> int:
  """The solution.
  """
  def place_first(n_gon:ring):
    for start_val in range(n+1,0,-1):
      n_gon[1]=start_val
      #print(f'the starting val is now {start_val}')
      answer = place_odd(n_gon,3)
      if answer:
        return(answer)

  def place_odd(n_gon:ring, index:int):
    for value in range(2*n,n_gon[1],-1):
      if value not in n_gon:
        n_gon[index]=value
        if 0 not in n_gon[1:2*n+1:2]:
          answer=place_even(n_gon)
          if answer:
             return(answer)
        else:
          answer = place_odd(n_gon,index+2)
          if answer:
             return(answer)
    n_gon[index]=0
          
  def place_even(n_gon:ring):
    for value1,value2 in ((i,j) 
                          for i in range(2*n,0,-1) 
                          for j in range(2*n,0,-1) 
                          if i!=j 
                          and i not in n_gon 
                          and j not in n_gon):
      n_gon[0]= value1
      n_gon[2]= value2
      line_total=sum(n_gon[0:3])
      for index in range(4,2*n,2):
        next_value=line_total-sum(n_gon[index-2:index])
        if next_value not in n_gon and next_value>0:
          n_gon[index]=next_value
        else:
          break
      if 0 not in n_gon:
         return(format(n_gon))
      for index in range(0,2*n,2):
         n_gon[index]=0
      
  def format(n_gon):
    return( ''.join([str(n_gon[2*i+1])+str(n_gon[2*i])+str(n_gon[2*i+2]) for i in range(n)]) )

  n_gon = ring([0]*2*n)
  return(place_first(n_gon))


def p68alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p68())
