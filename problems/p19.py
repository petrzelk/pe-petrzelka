#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 19: Name

Problem Description:
You are given the following information, but you may prefer to do some research for 
yourself.

  - 1 Jan 1900 was a Monday.
  - Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  - A leap year occurs on any year evenly divisible by 4, but not on a century unless 
    it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century 
(1 Jan 1901 to 31 Dec 2000)?

Functions:
None
'''

__date__ = "27 July 2020"

# Notes:
#
# Original solution shown.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p19() -> int:
  """The solution.
  """
  months = {
      0: 31,
      1: 28,
      2: 31,
      3: 30,
      4: 31,
      5: 30,
      6: 31,
      7: 31,
      8: 30,
      9: 31,
      10: 30,
      11: 31
  }
  result = 0
  date = [1, 0, 1_900]
  while date[2] < 2_000:
    date[0] = (date[0] + months[date[1]]) % 7
    date[1] += 1
    if date[1] == 1 and date[2] % 4 == 0 and date[2] % 100 == 0 and date[
        2] % 400 != 0:
      date[0] += 1
    if date[1] // 12 != 0:
      date[1] %= 12
      date[2] += 1
    if date[0] == 0:
      result += 1
  return (result)


def p19alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p19())
