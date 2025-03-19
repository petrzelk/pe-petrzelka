#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 54: Poker Hands

Problem Description:
In the card game poker, a hand consists of five cards and are ranked, from lowest to
highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
If two players have the same ranked hands then the rank made up of the highest value
wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if
two ranks tie, for example, both players have a pair of queens, then highest cards in
each hand are compared (see example 4 below); if the highest cards tie then the next
highest cards are compared, and so on.
Consider the following five hands dealt to two players:

Hand  Player 1                          Player 2             Winner
1     5H 5C 6S 7S KD                    2C 3S 8S 8D TD       Player 2
      Pair of Fives                     Pair of Eights
2     5D 8C 9S JS AC                    2C 5C 7D 8S QH       Player 1
      Highest card Ace                  Highest card Queen
3     2D 9C AS AH AC                    3D 6D 7D TD QD       Player 2
      Three Aces                        Flush  with Diamonds
4     4D 6S 9H QH QC                    3D 6D 7H QD QS       Player 1
      Pair of Queens Highest card Nine  Pair of Queens Highest card Seven
5     2H 2D 4C 4D 4S                    3C 3D 3S 9S 9D       Player 1
      Full House With Three Fours       Full House with Three Threes 

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line 
of the file contains ten cards (separated by a single space): the first five are Player 
1's cards and the last five are Player 2's cards. You can assume that all hands are 
valid (no invalid characters or repeated cards), each player's hand is in no specific 
order, and in each hand there is a clear winner.
How many hands does Player 1 win?

Functions:
get_key
win
'''

__date__ = '10 September 2023'

# Notes:
#
# This problem just sucks. just a whole bunch of different checks to see what hands each
# player has.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import get_key


# User defined functions
def win(p1: list, p2: list):
  #Does player 1 beat player 2? This funciton takes two lists of tuples,
  #made up of a card value and suit, numerically represented.

  #First compute the list of suits and values for each player
  p1val = {card[0]: [card[0] for card in p1].count(card[0]) for card in p1}
  p2val = {card[0]: [card[0] for card in p2].count(card[0]) for card in p2}
  p1suits = {card[1] for card in p1}
  p2suits = {card[1] for card in p2}
  #print(p1val,p1suits)
  #print(p2val,p2suits)

  #Royal Flush
  p1cond = len(p1suits) == 1 and p1val.keys() == set(range(10, 15))
  p2cond = len(p2suits) == 1 and p2val.keys() == set(range(10, 15))
  if p1cond or p2cond:
    return (p1cond)
  #print("no royal flush")

  #Straight Flush
  p1cond = (len(p1suits) == 1
            and p1val.keys() == set(range(min(p1val),
                                          min(p1val) + 5)))
  p2cond = (len(p2suits) == 1
            and p2val.keys() == set(range(min(p2val),
                                          min(p2val) + 5)))
  if p1cond or p2cond:
    if p1cond and p2cond:
      if max(p1val) != max(p2val):
        return (max(p1val) > max(p2val))
    else:
      return (p1cond)
  #print("no straight flush")

  #Four of a Kind
  p1cond = 4 in p1val.values()
  p2cond = 4 in p2val.values()
  if p1cond or p2cond:
    if p1cond and p2cond:
      if get_key(4, p1val) != get_key(4, p2val):
        return (get_key(4, p1val) > get_key(4, p2val))
      elif get_key(1, p1val) != get_key(1, p2val):
        return (get_key(1, p1val) > get_key(1, p2val))
    else:
      return (p1cond)
  #print("no four of a kind")

  #Full House
  p1cond = (2 in p1val.values()) and (3 in p1val.values())
  p2cond = (2 in p2val.values()) and (3 in p2val.values())
  if p1cond or p2cond:
    if p1cond and p2cond:
      if get_key(3, p1val) != get_key(3, p2val):
        return (get_key(3, p1val) > get_key(3, p2val))
      elif get_key(2, p1val) != get_key(2, p2val):
        return (get_key(2, p1val) > get_key(2, p2val))
    else:
      return (p1cond)
  #print("no full house")

  #Flush
  p1cond = len(p1suits) == 1
  p2cond = len(p2suits) == 1
  if p1cond or p2cond:
    if p1cond and p2cond:
      p1remain = set(p1val.keys())
      p2remain = set(p2val.keys())
      while len(p1remain):
        if max(p1remain) != max(p2remain):
          return (max(p1remain) > max(p2remain))
        else:
          p1remain.remove(max(p1remain))
          p2remain.remove(max(p2remain))
    else:
      return (p1cond)
  #print("no flush")

  #Straight
  p1cond = p1val.keys() == set(range(min(p1val), min(p1val) + 5))
  p2cond = p2val.keys() == set(range(min(p2val), min(p2val) + 5))
  if p1cond or p2cond:
    if p1cond and p2cond:
      if max(p1val) != max(p2val):
        return (max(p1val) > max(p2val))
    else:
      return (p1cond)
  #print("no straight")

  #Three of a Kind
  p1cond = 3 in p1val.values()
  p2cond = 3 in p2val.values()
  if p1cond or p2cond:
    if p1cond and p2cond:
      if get_key(3, p1val) != get_key(3, p2val):
        return (get_key(3, p1val) > get_key(3, p2val))
      else:
        p1remain = set(p1val.keys())
        p1remain.remove(get_key(3, p1val)[0])
        p2remain = set(p2val.keys())
        p2remain.remove(get_key(3, p2val)[0])
        while len(p1remain):
          if max(p1remain) != max(p2remain):
            return (max(p1remain) > max(p2remain))
          else:
            p1remain.remove(max(p1remain))
            p2remain.remove(max(p2remain))
    else:
      return (p1cond)
  #print("no three of a kind")

  #Two Pair
  p1cond = list(p1val.values()).count(2) == 2
  p2cond = list(p2val.values()).count(2) == 2
  if p1cond or p2cond:
    if p1cond and p2cond:
      if max(get_key(2, p1val)) != max(get_key(2, p2val)):
        return (max(get_key(2, p1val)) > max(get_key(2, p2val)))
      elif min(get_key(2, p1val)) != min(get_key(2, p2val)):
        return (min(get_key(2, p1val)) > min(get_key(2, p2val)))
      elif get_key(1, p1val)[0] != get_key(1, p2val)[0]:
        return (get_key(1, p1val)[0] > get_key(1, p2val)[0])
    else:
      return (p1cond)
  #print("no two pair")

  #One Pair
  p1cond = 2 in p1val.values()
  p2cond = 2 in p2val.values()
  if p1cond or p2cond:
    if p1cond and p2cond:
      if get_key(2, p1val) != get_key(2, p2val):
        return (get_key(2, p1val) > get_key(2, p2val))
      else:
        p1remain = set(p1val.keys())
        p1remain.remove(get_key(2, p1val)[0])
        p2remain = set(p2val.keys())
        p2remain.remove(get_key(2, p2val)[0])
        while len(p1remain):
          if max(p1remain) != max(p2remain):
            return (max(p1remain) > max(p2remain))
          else:
            p1remain.remove(max(p1remain))
            p2remain.remove(max(p2remain))
    else:
      return (p1cond)
  #print("no one pair")

  #High Card
  p1remain = set(p1val.keys())
  p2remain = set(p2val.keys())
  while len(p1remain):
    if max(p1remain) != max(p2remain):
      return (max(p1remain) > max(p2remain))
    else:
      p1remain.remove(max(p1remain))
      p2remain.remove(max(p2remain))
  #print("no high card")


# Solutions
def p54(file_path:str="..\\resources\\0054_poker.txt") -> int:
  """The solution.
  """
  cardvalues = {
      "2": 2,
      "3": 3,
      "4": 4,
      "5": 5,
      "6": 6,
      "7": 7,
      "8": 8,
      "9": 9,
      "T": 10,
      "J": 11,
      "Q": 12,
      "K": 13,
      "A": 14
  }
  cardsuits = {"H": 0, "D": 1, "C": 2, "S": 3}
  with open(os.path.join(os.path.dirname(__file__),file_path), 'r') as file:
    hands = file.read().split('\n')
  result = 0
  for line in hands[:-1]:
    p1 = []
    p2 = []
    for card in line.split()[:5]:
      p1 += [(cardvalues[card[0]], cardsuits[card[1]])]
    for card in line.split()[5:]:
      p2 += [(cardvalues[card[0]], cardsuits[card[1]])]
    if win(p1, p2):
      result += 1
  return (result)


def p54alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p54())
