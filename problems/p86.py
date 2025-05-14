#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 86: Cuboid Route

Problem Description:
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F,
sits in the opposite corner. By travelling on the surfaces of the room the shortest
"straight line" distance from S to F is 10 and the path is shown on the diagram.

<img src="resources/images/0086.png?1678992052" class="dark_img" alt="">
However, there are up to three "shortest" path candidates for any given cuboid and the
shortest route doesn't always have integer length.
It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with
integer dimensions, up to a maximum size of M by M by M, for which the shortest route
has integer length when M = 100. This is the least value of M for which the number of
solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.
Find the least value of M such that the number of solutions first exceeds one million.


Functions:
None
'''

__date__ = '26 March 2024'

# Notes:
#
# for every pythagorean triple
# m>n>0, GCF(m,n)=1, m%2==0 or n%2==0
# m**2-n**2, 2*m*n, m**2+n**2
# assume i<= j<= k then the shortest distance is sqrt((i+j)**2+k**2)
# for pythagorean triple a,b,c assuming a<b<c
# we know that there are a//2 ways of splitting up a into i and j, with b being k and 
# c being the path length
# We know that there are more ways by splitting b as long as both i and j are less than a.
# a to half of b ways a-b//2+1 if positive or if a+1>b//2
# I don't need to keep track of unique prisms because using this method if two prisms
# are the same then they came from the same triple
# No prism will be generated twice as a/b is unique for all primatives
# the minimum angle of a primitive pythagorean triple triangle is unique, thus the
# tangent of that angle is unique, thus the ratio of a and b is unique


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions
def truebox(limit: int = 100) -> int:
    sum_limit: int = limit*3
    result_count: int = 0
    n,m=1,2

    while m**2-n**2+2*m*n<=sum_limit:
        while m**2-n**2+2*m*n<=sum_limit:
            a=min(m**2-n**2,2*m*n)
            b=max(m**2-n**2,2*m*n)

            if gcf(m,n)==1:

                for multiple in range(1,sum_limit//(a+b)+1):

                    current_a=a*multiple
                    current_b=b*multiple

                    if current_b<=limit:
                        result_count+=current_a//2

                    if current_a<=limit and 2*current_a>current_b-1:
                        result_count+=current_a-(current_b-1)//2

            m+=2
        n+=1
        m=n+1

    return(result_count)

#Has an error of about 0.1% Throws off the problem. Need to read Knuth to fix.
def fastbox(limit: int = 100) -> int:
    sum_limit: int = limit*3
    result_count: int = 0
    n,m=1,2

    while m**2-n**2+2*m*n<=sum_limit:
        while m**2-n**2+2*m*n<=sum_limit:
            a=min(m**2-n**2,2*m*n)
            b=max(m**2-n**2,2*m*n)

            if gcf(m,n)==1:
                ubound=limit//b
                result_count+=ubound*(1+ubound)//2*a//2-(ubound+1)//4*(a%2)
                if a>=b//2:
                    ubound=limit//a
                    result_count+=ubound+a*((ubound)*(ubound+1)//2)-b*ubound*(ubound+1)//4+(ubound+1)//4*(b%2)-(b%2)*ubound//2-(b%2)*(ubound%2)

            m+=2
        n+=1
        m=n+1

    return(result_count)

# Solutions
def p86(limit: int = 1_000_000) -> int:
  """The solution.
  """
  def subsearch(lower,upper,limit):
        #print(upper,lower)
        if upper-lower<=1:
            if truebox((lower+upper)//2)>limit:
                return(lower)
            else:
                return(upper)
        elif truebox((lower+upper)//2)>limit:
            return(subsearch(lower,(lower+upper)//2,limit))
        else:
            return(subsearch((lower+upper)//2,upper,limit))
  upper=1
  while truebox(upper)<limit:
    upper*=2
  return(subsearch(0,upper,limit))


def p86alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p86())


#def PE86(limit: int = 100) -> int:
#    #result: set[tuple[int,int,int]]=set() # the set of all prisms found
#    result_count: int = 0
#    # while result size is too small
#    while result_count<=limit:
#        n,m=1,2
#        while m**2-n**2+2*m*n<limit:
#            while m**2-n**2+2*m*n<limit:
#                a=m**2-n**2
#                b=2*m*n
#                if GCF(m,n)==1:
#                    for multiple in range(1,limit//(a+b)+1):
#                        current_a=a*multiple
#                        current_b=b*multiple
#                        result_count += current_a//2
#                        if current_a+1>current_b//2:
#                            result_count += current_a-current_b//2+1
#                m+=2
#            n+=1
#            m=n+1
#    return(result_count)

#def box_constr(limit: int = 100) -> int:
#    sum_limit: int = limit*3
#    #result: set[tuple[int,int,int]]=set() # the set of all prisms found
#    #result=[]
#    result_count: int = 0
#    n,m=1,2
#    while m**2-n**2+2*m*n<=sum_limit:
#        while m**2-n**2+2*m*n<=sum_limit:
#            a=min(m**2-n**2,2*m*n)
#            b=max(m**2-n**2,2*m*n)
#            #print((n,m),a,b,m**2+n**2) # Gives the current triple
#
#            if GCF(m,n)==1:
#                #print(sum_limit//(a+b)+1) # Gives the number of multiples of the primitve that will be used
#                for multiple in range(1,sum_limit//(a+b)+1):
#
#                    current_a=a*multiple
#                    current_b=b*multiple    #Could I simplify these counts?
#                    #print(current_a,current_b,(m**2+n**2)*multiple) # Gives the current multiple of the primitive
#
#                    for i in range(1,current_a//2+1):
#                        if current_b<=limit:
#                            #result.add((i,current_a-i,current_b))
#                            result_count+=1
#                            #result+=[(i,current_a-i,current_b)]
#
#
#                    for i in range(current_a,current_b//2-1,-1):
#                        if current_a<=limit and current_b-i<=i:
#                            #result.add((current_b-i,i,current_a))
#                            result_count+=1
#                            #result+=[(current_b-i,i,current_a)]
#
#                    #result_count += current_a//2
#                    #if current_a+1>current_b//2:
#                        #result_count += current_a-current_b//2+1
#                #print(result)
#            m+=2
#        n+=1
#        m=n+1
#
#    #print(result)
#    return(result_count)

#def box_constr(limit: int = 100) -> int:
#    sum_limit: int = limit*3
#    result_count: int = 0
#    result_2: int = 0
#    n,m=1,2
#
#    while m**2-n**2+2*m*n<=sum_limit:
#        while m**2-n**2+2*m*n<=sum_limit:
#            a=min(m**2-n**2,2*m*n)
#            b=max(m**2-n**2,2*m*n)
#
#            if GCF(m,n)==1:
#                ubound=limit//b
#                result_2+=ubound*(1+ubound)//2*a//2-(ubound+1)//4*(a%2)
#                if a>=b//2:
#                    ubound=limit//a
#                    result_2+=ubound+a*((ubound)*(ubound+1)//2)-b*ubound*(ubound+1)//4+(ubound+1)//4*(b%2)-(b%2)*ubound//2-(b%2)*(ubound%2)
#                #temp=0
#                #test=0
#                #if a>=b//2:
#                    #ubound=limit//a
#                    #test=ubound+a*((ubound)*(ubound+1)//2)-b*ubound*(ubound+1)//4+(ubound+1)//4*(b%2)-(b%2)*ubound//2-(b%2)*(ubound%2)
#                    #for i in range(1,limit//a+1):
#                        #test-=(i*b)%2
#                        #pass
#
#                for multiple in range(1,sum_limit//(a+b)+1):
#
#                    current_a=a*multiple
#                    current_b=b*multiple    #Could I simplify these counts?
#
#                    #for i in range(1,current_a//2+1):
#                        #if current_b<=limit:
#                            #result_count+=1
#
#                    if current_b<=limit:
#                        result_count+=current_a//2
#
#                    #for i in range(current_a,(current_b-1)//2,-1):
#                        #if current_a<=limit:
#                            #result_count+=1
#
#                    if current_a<=limit and 2*current_a>current_b-1:
#                        result_count+=current_a-(current_b-1)//2
#                        #temp+=current_a-(current_b-1)//2
#
#                #print(a,b,temp,test,temp==test)
#
#            m+=2
#        n+=1
#        m=n+1
#
#    return(result_count,result_2)