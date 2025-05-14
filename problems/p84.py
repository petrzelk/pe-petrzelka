#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 84: Monopoly Odds

Problem Description:
In the game, Monopoly, the standard board is set up in the following way:

<img src="resources/images/0084_monopoly_board.png?1678992052"
alt="0084_monopoly_board.png">

A player starts on the GO square and adds the scores on two 6-sided dice to determine
the number of squares they advance in a clockwise direction. Without any further rules
we would expect to visit each square with equal probability: 2.5%. However, landing on
G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.
In addition to G2J, and one card from each of CC and CH, that orders the player to go
directly to jail, if a player rolls three consecutive doubles, they do not advance the
result of their 3rd roll. Instead they proceed directly to jail.
At the beginning of the game, the CC and CH cards are shuffled. When a player lands on
CC or CH they take a card from the top of the respective pile and, after following the
instructions, it is returned to the bottom of the pile. There are sixteen cards in each
pile, but for the purpose of this problem we are only concerned with cards that order a
movement; any instruction not concerned with movement will be ignored and the player
will remain on the CC/CH square.
Community Chest (2/16 cards):
Advance to GO
Go to JAIL

Chance (10/16 cards):
Advance to GO
Go to JAIL
Go to C1
Go to E3
Go to H2
Go to R1
Go to next R (railway company)
Go to next R
Go to next U (utility company)
Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular square. That
is, the probability of finishing at that square after a roll. For this reason it should
be clear that, with the exception of G2J for which the probability of finishing on it is
zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to
another square, and it is the final square that the player finishes at on each roll that
we are interested in. We shall make no distinction between "Just Visiting" and being
sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of
jail", assuming that they pay to get out on their next turn.
By starting at GO and numbering the squares sequentially from 00 to 39 we can
concatenate these two-digit numbers to produce strings that correspond with sets of
squares.
Statistically it can be shown that the three most popular squares, in order, are JAIL
(6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three
most popular squares can be listed with the six-digit modal string: 102400.
If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit
modal string.


Functions:
None
'''

__date__ = '12 March 2024'

# Notes:
#
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions
def delta(l1: list, l2: list) -> list:
    if len(l1)==len(l2):
        result = []
        for i in range(len(l1)):
            result.append(abs(l1[i]-l2[i]))
        return(result)

# Solutions
def p84(diceSides: int = 4) -> int:
    """The solution.
    """
    current = [2500 for i in range(40)]
    next = [0 for i in range(40)]
    dice = list(range(diceSides))+list(range(diceSides,0,-1))
    outcomes = sum(dice)
    #iterations=0
    while max(delta(current,next))>.01:
        next = [0 for i in range(40)]
        for index in range(len(current)):
            total=current[index]
            next[10]+=total/(diceSides**3)
            total*=(diceSides**3-1)/(diceSides**3)
            for role in range(len(dice)):
                landing=(index+role+1)%len(current)
                match landing:
                    case 30:
                        next[10]+=total*dice[role]/outcomes
                    case 2 | 17 | 33:
                        next[landing]+=total*dice[role]*7/(outcomes*8)
                        next[0]+=total*dice[role]/(outcomes*16)
                        next[10]+=total*dice[role]/(outcomes*16)
                    case 7 | 22 | 36:
                        next[landing]+=total*dice[role]*3/(outcomes*8)
                        next[0]+=total*dice[role]/(outcomes*16)
                        next[10]+=total*dice[role]/(outcomes*16)
                        next[11]+=total*dice[role]/(outcomes*16)
                        next[24]+=total*dice[role]/(outcomes*16)
                        next[39]+=total*dice[role]/(outcomes*16)
                        next[5]+=total*dice[role]/(outcomes*16)
                        match landing:
                            case 7:
                                next[15]+=total*dice[role]/(outcomes*8)
                                next[12]+=total*dice[role]/(outcomes*16)
                                next[4]+=total*dice[role]/(outcomes*16)
                            case 22:
                                next[25]+=total*dice[role]/(outcomes*8)
                                next[28]+=total*dice[role]/(outcomes*16)
                                next[19]+=total*dice[role]/(outcomes*16)
                            case 36:
                                next[5]+=total*dice[role]/(outcomes*8)
                                next[12]+=total*dice[role]/(outcomes*16)
                                next[33]+=total*dice[role]*7/(outcomes*128)
                                next[0]+=total*dice[role]/(outcomes*256)
                                next[10]+=total*dice[role]/(outcomes*256)
                    case _:
                        next[landing]+=total*dice[role]/outcomes
        current,next=next,current
        #iterations+=1
        #print(current)
    #print(iterations)
    #print(current)
    sorted=current[:]
    sorted.sort()
    modalList=[current.index(i) for i in sorted[::-1]]
    modalDict={current.index(i):i/1000 for i in sorted[::-1]}
    modalString=""
    for poss in modalList:
        if poss<10:
            modalString+="0"
        modalString+=str(poss)
    result=''
    for _ in range(3):
      high=max(modalDict.values())
      for i in modalDict.keys():
        if modalDict[i]==high:
          value=i
      result+=str(value)
      del modalDict[value]
    return(result)


def p84alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p84())
