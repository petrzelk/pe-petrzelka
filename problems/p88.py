#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 88: Product-sum Numbers

Problem Description:
A natural number, N, that can be written as the sum and product of a given set of at
least two natural numbers, {a_1, a_2, ..., a_k} is called a product-sum number: N = a_1
+ a_2 + ... + a_k = a_1 * a_2 * ... * a_k.
For example, 6 = 1 + 2 + 3 = 1 * 2 * 3.
For a given set of size, k, we shall call the smallest N with this property a minimal
product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5,
and 6 are as follows.

k=2: 4 = 2 * 2 = 2 + 2
k=3: 6 = 1 * 2 * 3 = 1 + 2 + 3
k=4: 8 = 1 * 1 * 2 * 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 * 1 * 2 * 2 * 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 * 1 * 1 * 1 * 2 * 6 = 1 + 1 + 1 + 1 + 2 + 6
Hence for 2 <= k <= 6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30;
note that 8 is only counted once in the sum.
In fact, as the complete set of minimal product-sum numbers for 2 <= k <= 12 is {4, 6,
8, 12, 15, 16}, the sum is 61.
What is the sum of all the minimal product-sum numbers for 2 <= k <= 12000?


Functions:
None
'''

__date__ = '14 April 2024'

# Notes:
# The initial intuition on this problem falsely told me to individualize for 
# each number. The true breakthrough shown below works because I build up the
# sets of factors rather than just the prime factors as I iterate over the 
# necessary list. This greatly reduces the work that has to be done later.
#
# Initially you want to say that having the factorization of each number would 
# be helpful. But this is a trap. It is far better to build the list of ways 
# that you can multiply to each number.
# 
# Note that prime numbers are the only numbers that can't be product sum numbers.
# Only check composite numbers for product sums. If you start at the smallest 
# number and work up than if you discover a new k value, then that value is the 
# minimal product sum.
#
# If you have a set of factors of a number then:
#       k = len(factors) + number - sum(factors)
# 


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions


# Solutions
def p88(limit: int = 12000) -> int:
  """The solution.
  """
  result=dict()
  factors={i:[[i]] for i in range(2,2*limit+1)}
  number=2
  while len(result) < limit-1:
    for product in factors[number][1:]:
      k=len(product)+number-sum(product)
      if k not in result and k<=limit:
        result[k]=number
    for i in range(2,min(number,2*limit//number)+1):
      factors[number*i]+=[factor_n+factor_i 
                          for factor_n in factors[number] 
                          for factor_i in factors[i] 
                          if factor_n[-1]>=factor_i[0] 
                          and factor_n+factor_i not in factors[number*i]]
    number+=1
  return(sum(set(result.values())))


def p88alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p88())

# Test cases:
# PE88(6) -> 30
# PE88(12) -> 61
# PE88(1200) -> 126128
# PE88(12000) -> 7587457







##########################################################################################
################### PREVIOUS ATTEMPTS SHOWN BELOW THIS POINT #############################
##########################################################################################

def PE88_3(limit: int = 12000):
	result={}
	factors=gen_factorization_dict(limit*2+1)
	number=2
	while len(result) < limit-1:
		for product in factors[number][1:]:
			k=len(product)+number-sum(product)
			if k not in result and k<=limit:
				result[k]=number
		number+=1
	return(sum(set(result.values())))

#Trying a third attempt... Third times the charm.
def gen_factorization_dict(limit: int= 12000) -> dict[int,list[list[int]]]:
	factors={i:[[i]] for i in range(2,limit+1)}

	for number in range(2,limit+1):

		for i in range(2,min(number,limit//number)+1):
			factors[number*i]+=[factor_n+factor_i for factor_n in factors[number] for factor_i in factors[i] if factor_n[-1]>=factor_i[0] and factor_n+factor_i not in factors[number*i]]

	return(factors)

#From Euler's method
def gcf(a:int,b:int)->int:
	while b:
					a,b=b,a%b
	return(a)

##########################################################################################
################### PREVIOUS ATTEMPTS SHOWN BELOW THIS POINT #############################
##########################################################################################



#Built without knowing if it would be needed. Came in useful when building the code
#to take the list of prime factors and create the different factorizaitons.
def product(list_of_numbers: list[int]) -> int:
	result: int = 1
	for i in list_of_numbers:
		result *= i
	return (result)

#print(product([1,2,3]))



#Could speed up by only looking at the odd numbers after 2
def primefactors(n: int) -> list[int]:
	result = []
	i = 2
	while i <= n:
		if n % i == 0:
			n //= i
			result.append(i)
		else:
			i += 1
	return (result)

#print(primefactors(96))



#Permutations of the partitions of n except for the part "n"
#This approach failed because the first and last item are never joined
#Note that for a factorization with three unique factors, this can't
#produce the product of the first and last.
def permitions(n: int) -> list[list[int]]:
	result = []
	for i in range(1, n):
		result.append([i, n - i])
		for remainder in permitions(n - i):
			result.append([i] + remainder)
	return (result)

#print(permitions(5))



#Useful for trouble shooting in the program to extract this code
#Note that the sum(split)=len(factorization)
#Note that for a factorization with three unique factors, this can't
#produce the product of the first and last.
def partial_product(factorization,split):
	result=factorization
	for count in split:
		factor = product(result[:count])
		result=result[count:]+[factor]
	return(result)

#print(partial_product([2,2,2,2,3],[2,2,1]))



#Returns thelist of diffent ways of combining factors
def combinations(n: int) -> list[list[int]]:
	result=[]
	for i in range(n):
		result+=[[i]]
		for j in combinations(n-i-1):
			result+=[[i]+[i+k+1 for k in j]]
	return(result)

#print(combinations(2))



#After Permitions, choose a combinations method
#this method is convoluted and inevitably failed.
def factor_combinations(factors: list[int]) -> list[list[int]]:
 result=[factors]
 combos=combinations(len(factors)-1)
 combos.remove(list(range(len(factors)-1)))
 i=0
 while i<len(factors):
   for combo in combos:
     remaining = factors[i+1:]
     if max(combo)<len(remaining):
       factor = factors[i]*product([remaining[i] for i in combo])
       remaining=[remaining[i] for i in range(len(remaining)) if i not in combo]
       if len(remaining)>1:
         result+=[factors[:i]+[factor]+[product(remaining)]]
         for extra in factor_combinations(remaining):
           result+=[factors[:i]+[factor]+extra]
       else:
         result+=[factors[:i]+[factor]+remaining]
   i+=1
 return(result)



# #speed up attempted, also comments added patially.
# #ultimately this method was far to slow.
# def factor_combos(factors: list[int]) -> list[list[int]]:
#  #Initialize the result with the trivial case included
#  result=[factors]

#  #Initialize the counter
#  i=0
#  while i<len(factors):
     
#    #Set up the possible index combinations, removing the
#    #case of the product of all factors
#    combos=combinations(len(factors)-i-1)
#    to_remove=list(range(len(factors)-i-1))
#    if to_remove:
#        combos.remove(list(range(len(factors)-i-1)))
   
#    #for evey index, consider the combos of numbers remaining
#    for combo in combos:

#      #find the factors after the current factor
#      remaining = factors[i+1:]
#      factor = factors[i]*product([remaining[i] for i in combo])
#      remaining=[remaining[i] for i in range(len(remaining)) if i not in combo]
#      if len(remaining)>1:
#        result+=[factors[:i]+[factor]+[product(remaining)]]
#        for extra in factor_combinations(remaining):
#          result+=[factors[:i]+[factor]+extra]
#      else:
#        result+=[factors[:i]+[factor]+remaining]
#    i+=1
#  return(result)

# #print(factor_combinations([2,2,2]))



#PE88(1200) in .92 seconds as value 125128
def PE88_1(limit: int = 12000):
 result={}
 n=2

 #Sets up the main loop. continue checking numbers and adding them to the 
 #result if they satisfy the conditions till the result is full.
 while len(result) < limit-1:

   #Check to make sure that the number is at least a composite number.
   if len(primefactors(n)) >= 2:

     #Sets up the factorization, this will be converted for each unique 
     #way of multiplying the factors together.
     #factorization=primefactors(n)

     #Could be optemized by eliminateing duplicates
     #Example:
     #8=2*4
     #8=2*2*2
     #8=4*2
     #Functionally the first and third are equivelent

     for factors in factor_combinations(primefactors(n)):
       k=len(factors)+n-sum(factors)
       if k not in result and k<=limit:
         result[k]=n
   n+=1
 return(sum(set(result.values())))

def gen_factors(limit: int= 12000):
 factors={i:[] for i in range(2,limit+1)}

 for i in range(2,limit+1):
   if not factors[i]:
     factors[i]=[i]

   for j in range(2,min(i,limit//i)+1):
     if not factors[i*j]:
       factors[i*j]+=factors[j]+factors[i]
 return(factors)




#def PE88_2(limit: int = 12000):
# factors=gen_factors(2*limit)
# result={}
# n=4
# 
# while len(result) < limit-1:
#   if len(factors[n])>=2:
#     for factor_list in factor_combos(factors[n]):
#       k=len(factor_list)+n-sum(factor_list)
#       if k not in result and k<=limit:
#         result[k]=n
#   n+=1
# return(sum(set(result.values())))



#retrying with a dictionary of factors approach
def gen_factors_dict(limit: int= 12000) -> dict[int,dict[int,int]]:
	factors={i:{} for i in range(2,limit+1)}

	for i in range(2,limit+1):
		if not factors[i]:
			factors[i][i]=1

		for j in range(2,min(i,limit//i)+1):
			if not factors[i*j]:

				for n in factors[j]:
					factors[i*j][n]=factors[j][n]

				for n in factors[i]:
					if n in factors[j]:
						factors[i*j][n]+=factors[i][n]
					else:
						factors[i*j][n]=factors[i][n]

	return(factors)

#int(gen_factors_dict(20))



#I want a function that takes in a list of integers returns a list of all the lists that can be created
#s.t. input[i]<=output[j][i] for all j
def lower_lists(list_of_numbers: list[int]) -> list[list[int]]:
	result=[[i] for i in range(list_of_numbers[0]+1)]
	for number in list_of_numbers[1:]:
		for list_candidate in result.copy():
			result+=[list_candidate+[i] for i in range(number+1)]
			result.remove(list_candidate)
	return(result)

#print(lower_lists([0,0,0]))



#Used for debugging
def fancy_print(x: list) -> None:
	print("\n[")
	for i in x:
		print(i)
	print("]")



# #retrying with a dictionary of factors approach
# def factor_combos_dict(factors: dict[int,int],n: int = 0) -> set[int]:

# 	#find n if not given
# 	if not n:
# 			n=product([i**factors[i] for i in factors])

# 	#Initialize the result with the trivial case included
# 	result={sum(factors.values())+n-sum([i*factors[i] for i in factors])}

# 	#Initialize the counter
# 	i=0
# 	while i<len(factors):

# 		#set up the sorted factors
# 		sorted_factors=list(factors.keys())
# 		sorted_factors.sort()

# 		#begin factor set with all of the different psosibilities for the multiplicity of the lowest factor
# 		factor_set=[[[i],[factors[sorted_factors[0]]-i]] for i in range(factors[sorted_factors[0]]+1)]

# 		#for ever factor following create a new set of possibilities for each previous way of creating the factor.
# 		for factor in sorted_factors[1:]:
# 			for possible_factor in factor_set.copy():
# 				factor_set+=[[possible_factor[0]+[multiplicity],possible_factor[1]+[factors[factor]-multiplicity]] for multiplicity in range(factors[factor]+1)]

# 				#remove the old posibility
# 				factor_set.remove(possible_factor)

# 		#remove the case where no factors are left over and the case where no factors were selected.
# 		factor_set.remove([[0]*len(factors),[factors[i] for i in sorted_factors]])
# 		factor_set.remove([[factors[i] for i in sorted_factors],[0]*len(factors)])

# 		fancy_print(factor_set)
# 		while {sum(factor[-1]) for factor in factor_set}!={0}:
# 			for factor_pairing in factor_set.copy():
# 				for factor_to_add in lower_lists(factor_pairing[-1])[1:]:
# 					factor_set+=[factor_pairing[:-1]+[factor_to_add,[factor_pairing[-1][i]-factor_to_add[i] for i in range(len(factor_to_add))]]]
# 				factor_set.remove(factor_pairing)
# 				fancy_print(factor_set)

# 		print(result)

# 		#factor_set_remainders=[[]]*len(factor_set)
# 		#for index in range(len(factor_set)):
			
# 			#factor_set_remainders[index]=[factor_set[index],[sorted_counts[j]-factor_set[index][j] for j in range(len(factor_set[index]))]]
# 		#print(factor_set_remainders)
# 		input()

# #n=8
# #factor_combos_dict(gen_factors_dict(n)[n])
					

		
		#Set up the possible index combinations, removing the
		#case of the product of all factors
		#combos=combinations(len(factors)-i-1)
		#to_remove=list(range(len(factors)-i-1))
		#if to_remove:
				#combos.remove(list(range(len(factors)-i-1)))

		#for evey index, consider the combos of numbers remaining
		#for combo in combos:

			#find the factors after the current factor
			#remaining = factors[i+1:]
			#factor = factors[i]*product([remaining[i] for i in combo])
			#remaining=[remaining[i] for i in range(len(remaining)) if i not in combo]
			#if len(remaining)>1:
				#result+=[factors[:i]+[factor]+[product(remaining)]]
				#for extra in factor_combinations(remaining):
					#result+=[factors[:i]+[factor]+extra]
			#else:
				#result+=[factors[:i]+[factor]+remaining]
		#i+=1
	#return(result)