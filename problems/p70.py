#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 70: Totient Permutation

Problem Description:
Euler's totient function, phi(n) [sometimes called the phi function], is used to
determine the number of positive numbers less than or equal to n which are relatively
prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
prime to nine, phi(9)=6.The number 1 is considered to be relatively prime to every
positive number, so phi(1)=1. 
Interestingly, phi(87109)=79180, and it can be seen that 87109 is a permutation of
79180.
Find the value of n, 1 < n < 10**7, for which phi(n) is a permutation of n and the
ratio n/phi(n) produces a minimum.


Functions:
None
'''

__date__ = '10 February 2024'

# Notes:
#
# -When writing a phi(n) function, finding the numbers that ARE coprime
#    is far more difficult that finding the numbers that are NOT coprime.
#    1 is always coprime, and n is always not coprime.
#
# -A factor of 2 would have at least a n/phi(n) of 2, which is already
#    matched with n=2.
#
#    *Only check odd numbers for this.
#
# -Most values of n, besides n=2817, that minimize n/phi(n)
#    are the product of two primes.
#
#    *Assume the the value that minimizes this is the product of two primes.
#
# -In order to minimize the work here, use the assumption that the first
#    prime factor is greater than the second.
#
#    *This halves the amount of work to be done.
#
# -A prime number will never satify these conditions. phi(n)=n-1, therfore
#    if n%10 is in [1,9] then a single digit has changed by one and n is not
#    a permutation of phi(n). If n%10 is 0 then ten is a factor and n is not
#    a prime number.
#
#    *Do not check primes for these properties.
#
# -If a value is know that satisfies the conditions of the problem,
#    then there must exsist enough coprime numbers for any future
#    minimizing value meaning that it can't be a multiple of any number
#    less than phi(n)/(n-phi(n)).
#
#    *Given is n=87109, which means that it cannot be a multiple of (or
#      a factor of) any number less that 9.99. This can be updated as we
#      find new minimum values.
#
# -This value can be updated as we find new minimizing values.
#
#    *The general solution should do this from 0, in order to find solutions
#      for n<87109.
#
# -Generating a list of primes up to 10**6 takes about 10 seconds using the
#    correct algorithm.
#
#    *Only generate these bacuase we know that we have a minimum prime
#      factor of 13. 10**7//13 ~ 10**6. See the previous item.
#
# -Further optimized this by seeing that we are looking for two primes that
#    are close to each other. We will only generate the primes up to the sqrt(limit)*2
#
#    *This is because we know that it can't have a factor of 2. This windowed range
#      can probably be optimized. This is one of the biggest optimizations as it reduces
#      the work done by O(sqrt(n)).
#
# -Minimize the amount of searching by disregarding all second prime factors beyond the
#    point where the product of the two prime factors is greater that the limit.
#
#    *This creates a triple boouded triangular region of two prime factors to check.
#
# -phi(prime1*prime2)=prime1*prime2-prime1-prime2+1=(prime1-1)(prime2-1).
#
#    *This single observation eliminates the need to have a general phi function.
#
# -Using this we can have phi(n)/(n-phi(n))= n/(prime1+prime2-1) -1
#
# -Prime**2 does satisfy the conditions?
#
# -For two numbers to be permutations of eachouther, they must be divisibe by 9.
#
#    *(prime1+prime2)%9==1

# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import add_prime, primes

# User defined functions


# Solutions
def p70(limit: int = 10_000_000) -> int:
  """The solution.
  """
  result = [3, 2]
  primeList = primes(int(limit**.5)+1)
  index2 = len(primeList)
  minPrime, minIndex2 = 0, 0
  index1 = index2 - 1
  add_prime(primeList)
  primeCount = index2
  prime1, prime2 = primeList[index1], primeList[index2]
  n = prime1 * prime2
  while prime1 >= minPrime:

    while n < limit:

      if (prime1 + prime2) % 9 == 1 and result[0] * (
          n - prime1 - prime2 + 1) > result[1] * n and sorted(
              str(n)) == sorted(str(n - prime1 - prime2 + 1)):

        minPrime = n / (prime1 + prime2 - 1) - 1
        minIndex2 = index2
        result = [n, n - prime1 - prime2 + 1]

      index2 += 1
      if index2 > primeCount:
        add_prime(primeList)
        primeCount += 1
      prime2 = primeList[index2]
      n = n = prime1 * prime2

    index2 = minIndex2 if minIndex2 else index1
    index1 -= 1
    prime1 = primeList[index1]
    prime2 = primeList[index2]
    n = prime1 * prime2
  return (result[0])


def p70alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p70())


"""SLOW, to much memory used to keep track of both
relative primes and non-relative primes."""
## def phi(n):
##    array={i+1:None for i in range(n)}
##    primes=set()
##    rp={1}
##    nrp={n}
##    for i in range(1,n+1):
##        if i not in rp and i not in nrp:
##            if n%i==0:
##                nrp|={i*j for j in range(1,n//i)}
##            else:
##                rp|={i*j for j in rp if i*j<n}
##                if i*i<n:
##                    rp|={i*i}
##    return(len(rp))
"""REDUNDANT, same speed as just comparing the sorted strings"""
##def unpack(s):
##    result={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
##    for c in s:
##        result[c]+=1
##    return(result)
"""SLOW, slower than comparing the size of the casted strings."""
##def size(n):
##    length=1
##    factor=10
##    while n//factor!=0:
##        length+=1
##        factor*=10
##    return(length)
"""SLOW, will not work for the full set of numbers, but is accurate,
This doesn't rely on any shakey assumptions."""
##def PE70b(limit=10**5):
##    resultn=2
##    resultphin=1
##    for n in range(3,10000,2):
##        phin=phi(n)
##        if sorted(str(n))==sorted(str(phin)) and resultn*phin>resultphin*n:
##            resultn=n
##            resultphin=phin
##            print(n,n/phin)
##    return(resultn)
"""SLOW, doesn't take into account numbers that have already been tried"""
##def PE70c(limit=10**4):
##  resultn=2
##  resultphin=1
##  primeList=primes(limit)
##  print("Primes generated")
##  for prime_1 in primeList[::-1]:
##    #print("Prime 1 is now",prime_1)
##    for prime_2 in primeList:
##      n=prime_1*prime_2
##      if n>limit:
##        break
##      phin=phi(n)
##      if sorted(str(n))==sorted(str(phin)) and resultn*phin>resultphin*n:
##        resultn=n
##        resultphin=phin
##        print(n,n/phin)
##  return(resultn)
"""SLOW, starts small goes big"""
##def PE70(limit=10**7):
##    resultn = 2
##    resultphin = 1
##    primeList = primes((2*limit)**.5)
##    upperIndex = len(primeList)
##    lowerIndex = 0
##    pointer1 = 0
##    previousPointer2=0
##    print("Primes generated, vairables initialized")
##    while pointer1<upperIndex:
##        prime1=primeList[pointer1]
##        if previousPointer2:
##            pointer2=previousPointer2
##            n=prime1*primeList[pointer2]
##        else:
##            pointer2=pointer1
##            n=primeList[pointer1]**2
##        while n>limit:
##            if pointer2<0:
##                pointer2=0
##                break
##            pointer2-=1
##            previousPointer2=pointer2
##            n=prime1*primeList[pointer2]
##        while pointer2>=lowerIndex:
##            n=prime1*primeList[pointer2]
##            phin=n-prime1-primeList[pointer2]+1
##            if sorted(str(n))==sorted(str(phin)) and resultn*phin>resultphin*n:
##                resultn=n
##                resultphin=phin
##                lowerValue=phin//(n-phin)
##                while primeList[lowerIndex]<lowerValue:
##                    lowerIndex+=1
##                #print(n,n/phin,lowerIndex,previousPointer2,prime1)
##            pointer2-=1
##        pointer1+=1
##    ##times ouit before reaching the ending point.
##    return(resultn)