#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 51: Prime Digit Replacements

Problem Description:
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine
possible values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is
the first example having seven primes among the ten generated numbers, yielding the
family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being
the first member of this family, is the smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily adjacent
digits) with the same digit, is part of an eight prime value family.

Functions:
is_prime
perms
primes
'''

__date__ = '14 September 2024'

# Notes:
#
# The solution shown is slow, and quite aweful. It would be better to generate all the
# primes and then connect primes that share the pattern rather than testing if each is
# a prime. The issue with that approach is developing an upper bound.
# 
# As noted on the form by Pythia, two and four repeating digits do not need to be 
# checked, but this is not generalized for prime families less than 8.
#
# Also note that you don't need to check one repeating number... Duh.
#
# This would be shorter if I pre-calculated the prime list.

# Import statments
import sys, os
from typing import Iterator
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import is_prime, perms, primes

# User defined functions


# Solutions
def p51(loopCount: int = 8) -> int:
  """The bad solution. 
  """

  def genNumbers(remaining, result=[]):
    if len(remaining) == 0:
      return (result)
    if remaining[0] == "N":
      if len(result):
        return (genNumbers(remaining[1:],
                           [j + str(i) for j in result for i in range(10)]))
      else:
        return (genNumbers(remaining[1:], [str(i) for i in range(1, 10)]))
    if remaining[0] == "X":
      if len(result):
        return (genNumbers(remaining[1:], [j + "X" for j in result]))
      else:
        return (genNumbers(remaining[1:], ["X"]))

  digits = 2
  finalAnswers = set()
  while True:
    for candidate in ["N" * i + "X" * (digits - i) for i in range(1, digits)]:
      print(candidate)
      for permutedCandidate in perms(list(candidate)):
        #print(permutedCandidate)
        permutedCandidate = ''.join(permutedCandidate)
        for numberedCandidate in genNumbers(permutedCandidate):
          #print(numberedCandidate)
          result = 10
          if numberedCandidate[0] == 'X':
            result -= 1
            for loopValue in range(1, 10):
              if result < loopCount:
                break
              elif not is_prime(
                  int(numberedCandidate.replace("X", str(loopValue)))):
                #print(int(numberedCandidate.replace("X",str(loopValue))))
                result -= 1
            if result >= loopCount:
              for loopValue in range(1, 10):
                if is_prime(int(numberedCandidate.replace("X",
                                                          str(loopValue)))):
                  finalAnswers.add(
                      int(numberedCandidate.replace("X", str(loopValue))))
          else:
            for loopValue in range(10):
              if result < loopCount:
                break
              elif not is_prime(
                  int(numberedCandidate.replace("X", str(loopValue)))):
                #print(int(numberedCandidate.replace("X",str(loopValue))))
                result -= 1
            if result >= loopCount:
              for loopValue in range(10):
                if is_prime(int(numberedCandidate.replace("X",
                                                          str(loopValue)))):
                  finalAnswers.add(
                      int(numberedCandidate.replace("X", str(loopValue))))
    if len(finalAnswers):
      return (min(finalAnswers))
    else:
      digits += 1


def p51alt(prime_value_family:int = 8):
  """Alternate solution.
  """
  def recurring_family(n : int) -> Iterator:
    counts = {str(n).count(c):c for c in str(n)}
    recurring_digit = counts[max(counts.keys())]
    return(int(str(n).replace(recurring_digit,str(i))) for i in range(10))
  prime_list = primes(1_000_000)
  n_recurring_digits = { i : set() for i in range(2,20)}
  prime_value_families= { i : set() for i in range(11)}
  for prime in prime_list:
    if any(str(prime).count(i) > 1 for i in str(prime)):
      for n in range(2,max(str(prime).count(i) for i in str(prime))+1):
        n_recurring_digits[n].add(prime)
  for recurring_set in n_recurring_digits.values():
    for recurring_prime in recurring_set:
      family = sum(i in recurring_set for i in recurring_family(recurring_prime))
      prime_value_families[family].add(recurring_prime)
  return(min(prime_value_families[prime_value_family]))

# Test cases
print(p51alt())
