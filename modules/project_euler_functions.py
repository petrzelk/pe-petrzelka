#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""funcitons.py: a repository of custom functions for Project Euler"""

import sys
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.rational import rational


def linear_sum(n: int, delta: int = 1) -> int:
  """Returns the summation from i=1 to n of delta*i.
  """
  return (delta * (1 + n) * n // 2)


def gcf(*composites: int) -> int:
  """Returns the greatest common factor of the items in the list.
  """
  a = composites[0]
  for b in composites[1:]:
    while b:
      a, b = b, a % b
  return (a)


def sqrt(n: int | float, guess=0, accuracy=1.0) -> float:
  """Returns the square root of n that is acurate to +- the accuracy given.
  The process can be acelerated given a good guess.
  """
  cur = 1 if n - accuracy == 0 else n - accuracy if guess == 0 else guess
  prev = n
  while abs(cur - prev) >= accuracy:
    cur, prev = (cur + n / cur) / 2, cur
  return (cur)


def product(tuple: tuple[int, ...]) -> int:
  """Returns the product of the numbers.
  """
  result = 1
  for n in tuple:
    result *= n
  return (result)


def factors(n: int) -> dict[int, int]:
  '''Returns a distribution of prime factors.
  '''
  result = {}
  x = 2
  limit = int(sqrt(n)) + 1
  while x < limit:
    while n % x == 0:
      if x not in result:
        result[x] = 0
      result[x] += 1
      n //= x
      limit = int(sqrt(n)) + 1
    x += 1
  if n != 1:
    result[n] = 1
  return (result)


def primes(limit: int) -> list[int]:
  '''Generates a list of primes in the range of n inclusive.
  '''
  result = [2]
  for i in range(3, limit + 1, 2):
    j = 0
    limit = int(sqrt(i))
    prime = True
    while result[j] <= limit:
      if i % result[j] == 0:
        prime = False
        break
      j += 1
    if prime:
      result.append(i)
  return (result)


def is_prime(n: int) -> bool:
  '''A simple prime test.
  '''
  return all(n % x != 0 for x in range(2, int(sqrt(n)) + 1))


def vector_fetch(matrix: list[list[int]], start: tuple[int, int],
                 vector: tuple[int, int], n: int):
  """returns the n-tuple of numbers that start with the value at the start and follow 
  the vector.
  """
  return (tuple(matrix[start[0] + vector[0] * i][start[1] + vector[1] * i]
                for i in range(n)))


def triangle_number(n) -> int:
  """Returns the nth triangular number.
  """
  return ((1 + n) * n // 2)


def factor_count(n) -> int:
  """Returns the count of the number of values that are divisible.
  """
  result = 2
  index = 2
  while index <= n // index:
    if n % index == 0:
      if n // index == index:
        result += 1
      else:
        result += 2
    index += 1
  return (result)


def factorial(n: int) -> int:
  """Returns the nth factorial.
  """
  result = 1
  for i in range(1, n + 1):
    result *= i
  return (result)


def next_collatz(n: int) -> int:
  """Finds the next entry in the collatz conjecture.
  """
  return (n // 2 if n % 2 == 0 else 3 * n + 1)


def factor_sum(n) -> int:
  """Returns the sum of values that are divisible.
  """
  result = 1
  index = 2
  while index < n // index:
    if n % index == 0:
      if n // index == index:
        result += index
      else:
        result += index + n // index
    index += 1
  return (result)


def is_abundant(n: int) -> bool:
  return (n < factor_sum(n))


def vinculum_length(n: int) -> int:
  """Finds the length of the repating part of the decimal of a unit fraction. Terminating
  decimals report a length of zero.
  """
  remainders = [1]
  next = remainders[-1] * 10 % n
  while next not in remainders:
    remainders.append(next)
    next = remainders[-1] * 10 % n
  return (0 if not next else len(remainders) - remainders.index(next))


def constant_sum(n: int, delta: int = 1) -> int:
  """Returns the summation from i=1 to n of delta.
  """
  return (delta * n)


def quad_sum(n: int, delta: int = 1) -> int:
  """Returns the summation from i=1 to n of delta*i**2.
  """
  return (delta * n * (1 + n) * (2 * n + 1) // 6)


def perms(sequence: list) -> list[list]:
  '''Returns a list of all of the permutations of the input.
  '''
  if len(sequence) <= 1:
    return ([sequence])
  else:
    return ([[sequence[i]] + j for i in range(len(sequence))
             for j in perms(sequence[:i] + sequence[i + 1:])])


def concat(sequence: list[int | str]) -> str:
  '''Concatonates a list of numbers or strings.
  '''
  return ("".join([str(i) for i in sequence]))


def is_triangle(n: int) -> bool:
  '''Boolean check to see if a number is triangular.
  '''
  return (((1 + 8 * n)**.5 - 1) / 2 % 1 == 0)


def letter_value(character: str) -> int:
  '''Returns the alphabetical place value of a character.
  '''
  return (ord(character.upper()) - 64 if ord(character.upper()) > 64
          and ord(character.upper()) <= 90 else 0)


def is_square(n: int) -> bool:
  '''A simple square test.
  '''
  return (n**.5 % 1 == 0)


def is_palendromic(string: str) -> bool:
  '''A simple test for palendromic strings
  '''
  return (string == string[::-1])


def is_pandigital(n: int | str) -> bool:
  '''A simple test to see if a number is pandigital.
  '''
  string = list(str(n))
  string.sort()
  return (string == [str(i) for i in range(1, len(string) + 1)])


def is_anagramic(a: str, b: str) -> bool:
  '''String-based removal based anagramic test.
  '''
  if len(a) == len(b) and len(a) == 0:
    return (True)
  elif a[0] in b:
    return (is_anagramic(a[1:], b[:b.find(a[0])] + b[b.find(a[0]) + 1:]))
  else:
    return (False)


def get_key(val: int | str, dictionary: dict) -> list:
  '''Returns a list of all keys with the given value pair.
  '''
  keys = []
  for key, value in dictionary.items():
    if val == value:
      keys += [key]
  return (keys)


def is_lychrel(n: int, iterations=0) -> bool:
  '''Lychel number test, assuming that 50 iterations is sufficient.
  '''
  n += int(str(n)[::-1])
  if is_palendromic(str(n)):
    return (False)
  elif iterations >= 50:
    return (True)
  else:
    return (is_lychrel(n, iterations + 1))


def is_prime_concat(a: int, b: int) -> bool:
  '''A check to see if both concatinations of integers are prime.
  '''
  return (is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a))))


def next_term(n: int, a0: int, r: int, d: int) -> int:
  '''Finds the next coefficient of a continued fraction.
  Finds an+1 for:
  
                 1
     ________________________
   =           sqrt(n) + rem
     ... an + _______________
                     den
  '''
  return ((r + a0) * d // (n - r**2))


def continued_fraction_period(n: int = 23) -> int:
  '''Finds the period on the continued fraction fo an irrational root.
  '''
  a0 = int(n**.5)
  if a0**2 == n:
    return (0)
  r, d, cycle = a0, 1, (a0, 1)
  a1 = next_term(n, a0, r, d)
  cyclelength = 1
  while (a1 * (n - r**2) // d - r, (n - r**2) // d) != cycle:
    r, d = a1 * (n - r**2) // d - r, (n - r**2) // d
    a1 = next_term(n, a0, r, d)
    cyclelength += 1
  r, d = a1 * (n - r**2) // d - r, (n - r**2) // d
  return (cyclelength)


def e_coefficients(n: int) -> list[int]:
  '''Generates a list of the coefficients of the continued fraction approximation of e.
  '''
  result = [2]
  place = 1
  while place < n:
    place += 1
    if place % 3 == 0:
      result += [place // 3 * 2]
    else:
      result += [1]
  return (result)


def continued_fraction_approx(coefficients: list[int]) -> rational:
  '''Given the coefficients of a continued fraction, this will return the simiplifies
  form of the approimation.
  '''
  partial = rational(coefficients[-1], 1)
  for n in coefficients[-2::-1]:
    partial = rational(n) + partial.reciprocal()
  return (partial)


def sqrt_approx(n: int, a: int) -> list[int]:
  '''Finds the ath continued fraction approximation of the squareroot of n using the 
  continued fraction method of p64 and p65, and returns it as a rational number.
  '''
  #find the first term in the infinite continued fraction
  a0 = int(n**.5)
  #if n was a perfect square then any approximation is just a0
  if a0**2 == n:
    return ([a0, 1])
  #set up variables to represent:
  #
  #               1
  #   ________________________
  # =           sqrt(n) + rem
  #   ... an + _______________
  #                   den
  #
  #where seq is the sequence [a0,a1,...,an]
  rem = a0
  den = 1
  seq = [a0]
  #build the sequence time it has a length of a
  while len(seq) < a:
    seq += [next_term(n, a0, rem, den)]
    rem, den = seq[-1] * (n - rem**2) // den - rem, (n - rem**2) // den
  #set up the fraction which will be updated from the bottom up.
  frac = [seq[-1], 1]
  for an in seq[-2::-1]:
    #add an to (1/fraction)
    frac = [an * frac[0] + frac[1], frac[0]]
  return (frac)


def pell_test(x: int, n: int, y: int) -> bool:
  #a test to see if a set of x and y are a solution for the
  #n-pell equation.
  return (x**2 - n * y**2 == 1)


def pell_min(n: int) -> int:
  #finds the smallest non-trivial x value for a solution to
  #the n-pell equation.
  a = 1
  approx = sqrt_approx(n, a)
  while not pell_test(approx[0], n, approx[1]):
    a += 1
    approx = sqrt_approx(n, a)
  return (approx[0])


def phi(n: int) -> int:
  '''Optimized Euler Totient function.
  '''
  nrprime = {n}
  for i in range(2, n):
    if i not in nrprime and n % i == 0:
      nrprime |= {i * j for j in range(1, n // i)}
  return (n - len(nrprime))


def add_prime(prime_list: list[int]) -> None:
  '''Appends the next prime to a complete list of primes.
  '''
  def is_prime(n, prime_list):
    for p in prime_list:
      if n % p == 0:
        return (False)
      elif i < p * p - 1:
        break
    return (True)
  i = prime_list[-1] + 2
  while not is_prime(i, prime_list):
    i += 2
  prime_list.append(i)
  
  
def digital_sum(n:int)->int:
  '''Finds the sum of the digits of a number.
  '''
  return sum(int(i) for i in str(n))
  

def square_digital_sum(n:int)->int:
  '''Finds the sum of the square of each digit of a number.
  '''
  return sum(int(i)**2 for i in str(n))


def partitions(n):
  '''Finds the partitions of n.
  '''
  def p(n,start):
    if n == 1 or n == 0:
      return(1)
    result=1
    for i in range(start,1,-1):
      result += p(n-i,min(i,n-i))
    return(result)
  return p(n,n)


def int_to_roman(n: int) -> str:
  '''Converts an integer to a string of characters with the same value in roman numerals.
  '''
  numerals=[[["MMMMMMMMMM",1000],
             ["MMMMM",5000],
             ["M",1000]],
            
            [["M",1000], 
             ["D",500], 
             ["C",100]],
            
            [["C",100],
             ["L",50],
             ["X",10]],
            
            [["X",10],
             ["V",5],
             ["I",1]]]
  
  number=str(n)
  result=""
  index=-1
  for place_val in number[::-1]:
    place_val=int(place_val)
    if index>=-3:
      if place_val%5<=3:
        result=numerals[index][2][0]*(place_val%5)+result
      if place_val>=4 and place_val<=8:
        result=numerals[index][1][0]+result
      if place_val==9:
        result=numerals[index][0][0]+result
      if place_val%5==4:
        result=numerals[index][2][0]+result
    else:
      result="M"*(place_val*10**(-4-index))+result
    index-=1
  return result


def roman_to_int(s: str) -> int:
  '''Convers a string of roman numerals to an integer.
  '''
  numerals={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
  result=numerals[s[-1]]
  for i in range(-2,-len(s)-1,-1):
    if numerals[s[i]] < numerals[s[i+1]]:
      result-=numerals[s[i]]
    else:
      result+=numerals[s[i]]
  return result


def is_ortho(v1: tuple[int,int],v2: tuple[int,int]) -> bool:
  '''Tests to see if two vectors are otrthogonal.
  '''
  return v1[0]*v2[0]+v1[1]*v2[1]==0


def is_int(n:int|float)->bool:
  '''Tests to see if a value is of type int or equivilant to one.
  '''
  return bool(isinstance(n, int) or n == int(n))