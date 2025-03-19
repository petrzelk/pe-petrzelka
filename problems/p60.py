#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 60: Prime Pair Sets

Problem Description:
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and
concatenating them in any order the result will always be prime. For example, taking 7
and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the
lowest sum for a set of four primes with this property.
Find the lowest sum for a set of five primes for which any two primes concatenate to
produce another prime.

Functions:
None
'''

__date__ = '18 November 2023'

# Notes:
#
#


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import is_prime, is_prime_concat, primes

# User defined functions


# Solutions
def p60(n: int = 5, limit: int = 10_000) -> int:
  """The solution.
  """
  # Generate the primes
  prime_list = primes(limit)
  # Create a dictionary of pairs of values with the given property, s.t. key < value.
  prime_pairs = {}
  for i in range(len(prime_list)):
    prime_pairs[(prime_list[i], )] = [
        prime_list[j] for j in range(i, len(prime_list))
        if is_prime_concat(prime_list[i], prime_list[j])
    ]
  # Start the result at the largest possible and search for a smaller result.
  result = limit * n
  prime_sets = prime_pairs
  # Repeat the process of building up possibilities till all possibilities found.
  # Breadth first search.
  while prime_sets:
    # The next iteration of the prime set will be built up.
    next_prime_sets = {}
    # For each key and associated candidate in the value,
    for prime_key in prime_sets:
      for candidate in prime_sets[prime_key]:
        # Add possibilities to the next prime set dictionary.
        next_prime_sets[prime_key + (candidate, )] = [
            i for i in prime_sets[prime_key]
            if i > candidate and all(i in prime_pairs[(j, )]
                                     for j in prime_key + (candidate, ))
        ]
      # Check for ending point.
      if len(prime_key) == n and sum(prime_key) < result:
        result = sum(prime_key)
    # Move the next prime set into place to repeat.
    prime_sets = next_prime_sets
  return (result)


def p60alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p60())
