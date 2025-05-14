#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 91: Right Triangles with Integer Coordinates

Problem Description:
The points P(x_1, y_1) and Q(x_2, y_2) are plotted at integer co-ordinates and are
joined to the origin, O(0,0), to form triangle OPQ.

<img src="resources/images/0091_1.png?1678992052" alt="">

There are exactly fourteen triangles containing a right angle that can be formed when
each co-ordinate lies between 0 and 2 inclusive; that is, 0 <= x_1, y_1, x_2, y_2 <= 2.

<img src="resources/images/0091_2.png?1678992052" alt="">

Given that 0 <= x_1, y_1, x_2, y_2 <= 50, how many right triangles can be formed?

Functions:
None
'''

__date__ = '9 May 2024'

# Notes:
#
# # Let P be the point (x1,y1) and Q be the point (x2,y2). Consider the side of the 
# triangle as three vectors. Let v1 be the vector OP, v2 be the vector OQ and v3 be 
# the vector PQ. These form a right triangle iff v1 is orthogonal to v2, v2 is 
# orthogonal to v3, or v1 is orthogonal to v3.
# With a space of 50 by 50, there are approximately 50**2 positions for each P and Q. 
# There are 6.25E6 triangles to check. Each triangle needs three orthogonality checks, 
# meaning that there are at most 1.875E7 orthogonality checks. This is O(n**2). 
# To narrow this down, we need to remove duplicates from consideration. To do this, 
# I assumed that the angle iOP is less than angle iOQ. tan(theta1)=y1/x1 implies that 
# theta1=arctan(y1/x1)~y1/x1. Therefor:
#
# theta2>theta1
# arctan(y2/x2)>arctan(y1/x1)
# y2/x2>y1/x1
# y2*x1>y1*x2
#
# Later I realised that it would have been less computationally intesive and easier 
# if I just assumed that y1<y2 and x1<x2 seperately. This would have also narrowed 
# down the number of points to check.
# Check orthoganality by checkinf if (x1*x2)+(y1*y2) is zero.
# Then assuming that you iterate through all x1,y1,x2 then y2>(y1*x2)/x1
# Next notice that if v1 is orthogonal to v2, then v1=i*m and v2=j*n for some natural
# number m and n. this means that there are exactly limit**2 options for v1 to be 
# orthogonal to v2.
# For v1 orthogonal to v3 we can use the minimum integer left-hand orthogonal vector 
# discussed below. Either it will hit the y-axis first or it will reach the boundary 
# first, so we take the minimum of the two values.
#
# min( 
#      (limit-y1)//(x1//gcf(x1,y1)),      #Reaches the limit first
#      x1//(y1//gcf(x1,y1))               #Reaches the axis first
#    )
#
# FINAL SOLUTION WRITE UP:
# Let O be the origin and P and Q be points (x1,y1) and (x2,y2). Let x1,y1,x2,y2 be 
# non-negative integers less than or equal to the limit given. Let triangle OPQ be 
# a right triangle.Take cases without the loss of generality:
# Case 1: O is a right angle. If OP is orthogonal to OQ then the angle POQ is right 
# and OP and OQ are a scaled basis vector for the space. To eliminate duplicated, 
# assume that OP is n*(1,0) and OQ is m*(0,1) for some natural number n and m that 
# is les than or equal to the limit. There exist exactly limit**2 options for this 
# type of triangle. 
# Case 2: P or Q is a right angle. Without loss of generality, assume that P is the 
# right angle. Then there exsist a left-hand orthoganal vector with values (-y,x). 
# To figure out the maimum triangles find the gcf of x1,y1 and divid it out. In both 
# directions of the orthoganal vector count the number of times you can add it 
# without reaching the limit or an axis.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p91(limit:int = 50) -> int:
  """The solution.
  """
  #Start with result being case 1, angle POQ is right.
  result=limit**2
  
  #Add all possible P being on the x-axis or y-axis. Each axis has limit**2 possibilities
  result+=2*limit**2
  
  #Assume that OPQ is the right angle. Take all possible P.
  for (x,y) in [(i,j) for i in range(1,limit+1) for j in range(1,limit+1)]:
  
    #Use OP to find the smallest orthogonal vector
    #Find the smallest integer vector with the same direction
    scale=max(gcf(x,y),1)
    
    #Find the values of the smallest left-hand integer orthogonal vector
    x_ortho,y_ortho=-y//scale,x//scale
  
    #Use the left-hand orthogonal vector to find all Q such that angle iOP is less than angle iOQ
    result+=min((limit-y)//y_ortho,-x//x_ortho)
    #Use the right-hand orthogonal vector to find all Q such that angle iOP is greater than angle iOQ
    result+=min(y//y_ortho,(x-limit)//x_ortho)  
  
  return(result)


def p91alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p91())


# def PE91(limit):
#   #Start with result being case 1, angle POQ is right.
#   result=limit**2
#
#   #Find all the possible points that p could be.
#   points=[(0,j) for j in range(1, limit+1)]+[(i,j) for i in range(1,limit+1) for j in range(limit+1)]
#   
#   #Assume that OPQ is the right angle. Take all possible P.
#   for (x,y) in points:
#     
#     #Use OP to find the smallest orthogonal vector
#     #Find the smallest integer vector with the same direction
#     scale=max(gcf(x,y),1)
#     #Find the values of the left hand integer orthogonal vector
#     x_ortho,y_ortho=-y//scale,x//scale
#     
#     # If the point is not on the x-axis or y-axis
#     if y and x:
#       #Use the left hand orthogonal vector to find all Q such that angle iOP is less than angle iOQ
#       result+=min((limit-y)//y_ortho,-x//x_ortho)
#       #Use the right hand orthogonal vector to find all Q such that angle iOP is less than angle iOQ
#       result+=min(y//y_ortho,(x-limit)//x_ortho)
#     
#     # If the point is on the x-axis or y-axis, then you can draw a limit amount of triangles.
#     else:
#       result+=limit
#
# 
#
#   return(result)

# def PE91(limit):
#   #start result with all the v1 ortho v2
#   result=limit**2
#
#   #for all v1
#   for (x,y) in [(i,j) for i in range(1,limit+1) for j in range(limit+1)]:
#     #use v1 to find the smallest orthogonal vector
#     scale=gcf(x,y)
#     x_ortho,y_ortho=-y,x
#     if scale != 0:
#       x_ortho,y_ortho=-y//scale,x//scale
#     #add all v1 ortho v3
#     if x_ortho:
#       result+=min((limit-y)//y_ortho,-x//x_ortho)
#     else:
#       result+=limit
# 
#     #search for all v2 ortho v3
#     for (x2,y2) in [(i,j) for i in range(x) for j in range(max(y,1),int(y+sqrt(x**2+y**2))//2+1)]:
#       if ortho((x2,y2),(x2-x,y2-y)):
#         result+=1
#         print((x,y),(x2,y2))
#
#   return(result)
    

# def PE91(limit):
#   result=0
#   v0=(0,0) 
#   for x1 in range(1,limit+1):
#     for y1 in range(limit+1):
#       for x2 in range(limit+1):
#         for y2 in range(y1*x2//x1+1,limit+1):
#           v1,v2,v3=(x1,y1),(x2,y2),(x2-x1,y2-y1)
#           if v1==v0 or v2==v0 or v3==v0 or y2*x1<=y1*x2:
#             pass
#           elif ortho(v1,v2) or ortho(v2,v3) or ortho(v1,v3):
#             result+=1
#             #print(v1,v2)
#   return(result)

# def PE91(limit):
#   result=0
#   v0=(0,0)
#   for x1 in range(limit+1):
#     for y1 in range(limit+1):
#       for y2 in range(limit+1):
#         for x2 in range(limit+1):
#           v1,v2,v3=(x1,y1),(x2,y2),(x2-x1,y2-y1)
#           if v1==v0 or v2==v0 or v3==v0 or y2*x1<=y1*x2:
#             pass
#           elif ortho(v1,v2) or ortho(v2,v3) or ortho(v1,v3):
#             result+=1
#             #print(v1,v2)
#   return(result)