#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 98: Anagramic Squares

Problem Description:
By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we
form a square number: 1296 = 36**2. What is remarkable is that, by using the same
digital substitutions, the anagram, RACE, also forms a square number: 9216 = 96**2. We
shall call CARE (and RACE) a square anagram word pair and specify further that leading
zeroes are not permitted, neither may a different letter have the same digital value as
another letter.
Using <a href="resources/documents/0098_words.txt">words.txt (right click and 'Save
Link/Target As...'), a 16K text file containing nearly two-thousand common English
words, find all the square anagram word pairs (a palindromic word is NOT considered to
be an anagram of itself).
What is the largest square number formed by any member of such a pair?
NOTE: All anagrams formed must be contained in the given text file.


Functions:
None
'''

__date__ = '3 June 2024'

# Notes:
#
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions
def is_anagram(string1,string2):
  return(len(string1)==len(string2) and 
          (len(string1)==0 or 
            (string1.count(string1[0])==string2.count(string1[0]) and
            is_anagram(string1.replace(string1[0],""),  
                       string2.replace(string1[0],"")))) )
  
def pop(string: str, index: int) -> str:
  return(string[:index]+string[index+1:])
  
def iso_anagram(word1: str, num1: str, word2: str, num2: str) -> bool:
  if not word1:
    return(True)
  target=word2.index(word1[0])
  if target==num2.index(num1[0]):
    return(iso_anagram(word1[1:],num1[1:],pop(word2,target),pop(num2,target)))
  else:
    return(False)
  
# Solutions
def p98(file_path: str = "..\\resources\\0098_words.txt") -> int:
  """The solution.
  """
  with open(os.path.join(os.path.dirname(__file__),file_path), 'r') as file:
    words=file.read().replace('"','').split(',')
  sorted_words=[]
  for word in words:
    sorted_words.append(list(word))
    sorted_words[-1].sort()
  pairs=[]
  for i in range(len(words)):
    for j in range(i+1,len(words)):
      if sorted_words[i]==sorted_words[j]:
        word1=words[i]
        pairs.append([len(word1),
                      word1,
                      words[j],
                      [word1.count(x) for x in sorted_words[i]]])

  for length in range(max([i[0] for i in pairs]),0,-1):
    current_pairs=[i for i in pairs if i[0]==length]
    #print(f"Currently searching squares with length {length}")
    upper_square=int(10**(length/2))
    lower_square=int(10**((length-1)/2))
    squares=[]
    sorted_squares=[]
    for i in range(lower_square,upper_square):
      squares.append(i**2)
      sorted_squares.append(list(str(i**2)))
      sorted_squares[-1].sort()
    
    for i in range(len(squares)-1,-1,-1):
      for j in range(i-1,-1,-1):
        if sorted_squares[i]==sorted_squares[j]:
          #print(f"Found anagramic square pair {square1} and {square2}")
          sqr1=squares[i]
          sqr2=squares[j]
          for pair in current_pairs:
            if (iso_anagram(pair[1],str(sqr1),pair[2],str(sqr2)) or iso_anagram(pair[2],str(sqr1),pair[1],str(sqr2))) and [str(squares[i]).count(x) for x in sorted_squares[i]] == pair[3]:
              #print(sqr1,pair[1],sqr2,pair[2])
              return(sqr1)


def p98alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p98())
