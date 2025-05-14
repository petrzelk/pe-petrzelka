#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 90: Cube Digit Pairs

Problem Description:
Each of the six faces on a cube has a different digit (0 to 9) written on it; the same
is done to a second cube. By placing the two cubes side-by-side in different positions
we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed:

<img src="resources/images/0090.png?1678992052" class="dark_img" alt="">

In fact, by carefully choosing the digits on both cubes it is possible to display all of
the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube
and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an
arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square
numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not
the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last
example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming
2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to
be displayed?

Functions:
None
'''

__date__ = '3 May 2024'

# Notes:
#
# Set 0 in list one and 1 in list two, otherwise all 
# options will be duplicated. Use this pair because it
# has no 6 or 9 as a digit.
# 
# Add in the following pairs in both orders:
# 04
# 09 or 06
# 16 or 19
# 25
# 36 or 39
# 49 or 46
# 64 or 94
# 81
# 
# Comine all outcomes as a set of sets of dice, and for 
# every dice that was created figure out how many 
# variations can be created.
#
# If I'm able to make 49, I am able to make 64!
#
# For a defined amount of sides n of a dice, there are 
# something like (11-n)!/5! (This is incorrect, finish
# later as combinations not permutations)
#
# CORRECTION: for a dice with n defined sides:
# (10-n)!/((6-n)!*4!)
# =(7-n)*(8-n)*(9-n)*(10-n)/24
#
# This will lead to dice being double counted though. 
# Assume the remaining numbers on the dice have to be
# larger than the max required number. This means the
# the previous equation works iff n is the max of the 
# required sides and not the number of required sides.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions
def n_choose_r(n:list[int],r:int)->list[list[int]]:
  if r==0:
    return([[]])
  if r==1:
    return([[i] for i in n])
  else:
    result=[]
    for i in range(len(n)):
      result+=[[n[i]]+j for j in n_choose_r(n[i+1:],r-1)]
    return(result)

# Solutions
def p90() -> int:
  """The solution.
  """
  #populated the result with possible dice pairs with  only the required number
  def delta(togo:list[list[str]],prev:list[str]) -> None:
    if not len(togo):
      dice=[{int(i[0]) for i in prev},{int(i[1]) for i in prev}]
      global result
      if len(dice[0])<=6 and len(dice[1])<=6 and dice not in result and dice[::-1] not in result:
        result+=[dice]
    else:
      for pair in togo[0]:
        delta(togo[1:],prev+[pair])

  #create the factor list to feed into the delta function
  factor_list=[]
  for i in [i for i in range(1,10) if i!=7]:
    i_squared=str(i**2)
    if len(i_squared)<2:
      i_squared+='0'
    if '6' in i_squared:
      factor_list += [[i_squared, 
                  i_squared[::-1], 
                  i_squared.replace('6','9'), 
                  i_squared.replace('6','9')[::-1]]]
    elif '9' in i_squared:
      factor_list += [[i_squared, 
                  i_squared[::-1], 
                  i_squared.replace('9','6'), 
                  i_squared.replace('9','6')[::-1]]]
    else:
      factor_list+=[[i_squared,i_squared[::-1]]]

  #create the result to store the different dice combinations.
  global result
  result=[]

  #call the delta function to populate the result.
  delta(factor_list[1:],['01'])

  #print(len(result))
  
  #counter=0
  #iterate back through all the possible dice
  for dice_pair in result.copy():
    for dice_1_remaining in n_choose_r(list(set(range(10))-dice_pair[0]), 6-len(dice_pair[0])):
      for dice_2_remaining in n_choose_r(list(set(range(10))-dice_pair[1]), 6-len(dice_pair[1])):
        dice_pair_to_add=[dice_pair[0]|set(dice_1_remaining),dice_pair[1]|set(dice_2_remaining)]
        if dice_pair_to_add not in result and dice_pair_to_add[::-1] not in result:
          result.append(dice_pair_to_add)
          #print("Added",dice_pair_to_add,"with lengths",len(dice_pair[0]),len(dice_pair[1]))
    if len(dice_pair[0])<6 or len(dice_pair[1])<6:
      result.remove(dice_pair)
    #ounter+=1
    #print(counter)
    
    
  #return the answer.
  return(len(result))


def p90alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p90())
