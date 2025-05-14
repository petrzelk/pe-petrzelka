#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 94: Almost Equilateral Triangles

Problem Description:
It is easily proved that no equilateral triangle exists with integral length sides and
integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square
units.
We shall define an almost equilateral triangle to be a triangle for which two sides are
equal and the third differs by no more than one unit.
Find the sum of the perimeters of all almost equilateral triangles with integral side
lengths and area and whose perimeters do not exceed one billion (1,000,000,000).


Functions:
None
'''

__date__ = '17 May 2024'

# Notes:
#
# The perimeter of an almost equilateral triangle will be even and of the form 3n+1 or 3n-1
# Check each triangle from n=1 to 333 333 333.
# Each valid triangle will be two pythagorean triples.
# Let the triangle have the side lengths of a, b, and c. The area of the triangle is 
# A=sqrt((a+b+c)(a+b-c)(a-b+c)(-a+b+c))/4
#
# That means that for a=n b=n and c=n+1:
# A=sqrt((3n+1)(n-1)(n+1)(n+1))/4
# or A=(n+1)*sqrt((3n+1)(n-1))/4
#
# And for a=n b=n and c=n-1:
# A=sqrt((3n-1)(n+1)(n-1)(n-1))/4
# or A=(n-1)*sqrt((3n-1)(n+1))/4
#
# As Wikipedia states for integer triangles, the sides of this triangle must be on integer 
# co-ordinates in the cartesian plane. Further more, if we take the base and altitude of 
# said triangle, at least one must be even.
# 
# I was stumped by this problem, with the correct answer for several days because I failed 
# to read the question close enough to understand that it was asking fro the sum of the 
# perimeters.
#
# Old implimentation took 10 seconds for 10**7.
# New is 5 seconds without pre-generating the squares.
# With pre-generating the squares it took 3 seconds.
#for n in range(10**7):
#  sqrt_dict(n)
# 10**9 would be prohibitively slow. Need to find a faster way. 
#
# From Wikipedia's entry on Isosceles Heronian Triangles:
# All isosceles Heronian triangles are decomposable. They are formed by joining two 
# congruent Pythagorean triangles along either of their common legs such that the 
# equal sides of the isosceles triangle are the hypotenuses of the Pythagorean triangles, 
# and the base of the isosceles triangle is twice the other Pythagorean leg. Consequently, 
# every Pythagorean triangle is the building block for two isosceles Heronian triangles 
# since the join can be along either leg. All pairs of isosceles Heronian triangles are 
# given by rational multiples of:
#
# a=2(u**2-v**2),
# b=u**2+v**2
# c=u**2+v**2
# and
# a=4uv
# b=u**2+v**2
# c=u**2+v**2
# for coprime integers u and v with u >v and u+v odd.

# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p94(limit:int= 1_000_000_000) -> int:
  """The solution.
  """
  x=2+sqrt(3)
  limit=int(sqrt(limit/(12*x)))
  result=0
  for v in range(1,limit):
      
    u=(3*v**2+1)**.5
    if is_int(u):
      #print("HIT sqr",u,v,u**2+v**2,2*(u**2-v**2))
      result+=4*u**2
      
      u+=2*v
      #print("HIT prdct",u,v,u**2+v**2,4*u*v)
      result+=2*(u**2+v**2)+4*u*v
      
    u=(3*v**2-1)**.5
    if is_int(u):
      #print("HIT sqr",u,v,u**2+v**2,2*(u**2-v**2))
      result+=4*u**2
      
      u+=2*v
      #print("HIT prdct",u,v,u**2+v**2,4*u*v)
      result+=2*(u**2+v**2)+4*u*v
      
  return(int(result))


def p94alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p94())
