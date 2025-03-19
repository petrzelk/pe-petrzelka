#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 59: XOR Decryption

Problem Description:
Each character on a computer is assigned a unique code and the preferred standard is
ASCII (American Standard Code for Information Interchange). For example, uppercase A =
65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR
each byte with a given value, taken from a secret key. The advantage with the XOR
function is that using the same encryption key on the cipher text, restores the plain
text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and
the key is made up of random bytes. The user would keep the encrypted message and the
encryption key in different locations, and without both "halves", it is impossible to
decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to
use a password as a key. If the password is shorter than the message, which is likely,
the key is repeated cyclically throughout the message. The balance for this method is
using a sufficiently long password key for security, but short enough to be memorable.
Your task has been made easy, as the encryption key consists of three lower case
characters. Using 0059_cipher.txt (right click and 'Save Link/Target As...'), a file 
containing the encrypted ASCII codes, and the knowledge that the plain text must contain
common English words, decrypt the message and find the sum of the ASCII values in the 
original text.

Functions:
None
'''

__date__ = '20 September 2023'

# Notes:
#
#


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p59(file_path: str = "..\\resources\\0059_cipher.txt") -> int:
  """The solution.
  """
  with open(os.path.join(os.path.dirname(__file__),file_path), 'r') as file:
    contents = [int(i) for i in file.read().split(",")]
  #print(type(contents[-1]))
  maxPassword = [0, 0, 0]
  maxWords = 0 
  for a, b, c in ((a, b, c) for a in range(ord("a"),
                                           ord("z") + 1)
                  for b in range(ord("a"),
                                 ord("z") + 1)
                  for c in range(ord("a"),
                                 ord("z") + 1)):
    cypherContents = []
    password = [a, b, c]
    for n in range(len(contents)):
      cypherContents += [chr(contents[n] ^ password[n % 3]).lower()]
    message = "".join(cypherContents).split(" ")
    score = message.count("the") + message.count("of") + message.count(
        "and") + message.count("a") + message.count("to")
    if score > maxWords:
      maxWords = score
      maxPassword = [a, b, c]
      #print(message)
  #print(maxPassword)
  result = 0
  for n in range(len(contents)):
    result += contents[n] ^ maxPassword[n % 3]
  return (result)


def p59alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p59())
