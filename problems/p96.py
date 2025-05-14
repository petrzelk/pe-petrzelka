#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Project Euler Problem 96: Su Doku

Problem Description:
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept.
Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a
similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su
Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that
each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example
of a typical starting puzzle grid and its solution grid.

<img src="project/images/p096_1.png" alt="p096_1.png" />
<img src="project/images/p096_2.png" alt="p096_2.png" />

A well constructed Su Doku puzzle has a unique solution and can be solved by logic,
although it may be necessary to employ "guess and test" methods in order to eliminate
options (there is much contested opinion over this). The complexity of the search
determines the difficulty of the puzzle; the example above is considered easy because it
can be solved by straight forward direct deduction.
The 6K text file, <a href="project/resources/p096_sudoku.txt">sudoku.txt (right click
and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in
difficulty, but all with unique solutions (the first puzzle in the file is the example
above).
By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left
corner of each solution grid; for example, 483 is the 3-digit number found in the top
left corner of the solution grid above.

Functions:
None
'''

__date__ = '29 May 2024'

# Notes:
#
# I strongly dislike my solution and plan on coming back to optimize it. Currently 
# take over a minute to solve all 50 of the sudokus.


# Import statments
import sys, os
sys.path.insert(0, sys.path[0][:-sys.path[0][::-1].find('\\')-1])
from modules.project_euler_functions import *

# User defined functions
def createPuzzle(string):
  result=[]
  for line in string.split("\n"):
    result+=[list(line)]
  return(result)

def print_puzzle(puzzle):
  for line in puzzle:
    print(line)
  print("")
  
def update_puzzle(puzzle):
  repeat=True
  while repeat:
    repeat=False
    for i,j in [(i,j) for i in range(9) for j in range(9)]:
      value=puzzle[i][j]
      if isinstance(value,set) and len(value)==1:
        value=value.pop()
        repeat=True

        #Remove the value from the column
        for row in range(9):
          target=puzzle[row][j]
          if isinstance(target,set):
            target-={value}

        #Remove the value from the row
        for column in range(9):
          target=puzzle[i][column]
          if isinstance(target,set):
            target-={value}

        #Remove the value from the sub box
        for row,column in [(3*(i//3)+row,3*(j//3)+column) for row in range(3) for column in range(3)]:
          target=puzzle[row][column]
          if isinstance(target,set):
            target-={value}

        #Set the only possibility to be the value
        puzzle[i][j]=value
        
def recursive_guess(puzzle):
  if True in {puzzle[i][j]==set() for i in range(9) for j in range(9)}:
    return(False)
  for i,j in [(i,j) for i in range(9) for j in range(9)]:
    if isinstance(puzzle[i][j],set):
      for possible in puzzle[i][j].copy():
        puzzle[i][j]={possible}
        possible_puzzle=[]
        for row in puzzle:
          possible_row=[]
          for cell in row:
            if isinstance(cell, int):
              possible_row.append(cell)
            else:
              possible_row.append(cell.copy())
          possible_puzzle.append(possible_row)
        update_puzzle(possible_puzzle)
        possible_puzzle=recursive_guess(possible_puzzle)
        
        if possible_puzzle:
          update_puzzle(possible_puzzle)
          if True not in {possible_puzzle[i][j]==set() for i in range(9) for j in range(9)}:
            #print_puzzle(possible_puzzle)
            #input()
            return(possible_puzzle)
          
  return(puzzle)

# Solutions
def p96(file_path: str = "..\\resources\\0096_sudoku.txt") -> int:
  """The solution.
  """
  with open(os.path.join(os.path.dirname(__file__),file_path), 'r') as file:
    sudokus=file.read().split("\nG")
  
  result=0
  for grid in sudokus:

    #Each grid is a string representation of the sudoku

    #Create a 2-dimensional array of numbers representing the sudoku
    beginning=[list(line) for line in grid.split("\n")[1:]]

    #Create a 2-dimensional array to store a set of possible outcomes of a square
    puzzle=[[set(range(1,10))  for square in line] for line in beginning]

    #Update to each box for box in row i and column j.
    for i,j in [(i,j) for i in range(9) for j in range(9)]:
      value=int(beginning[i][j])

      #If there is a value in a cell, make it the only option.
      if value:
        puzzle[i][j]={value}

    #Call the update function to place values in given cells and to remove given cells from their rows, columns and sub boxes.
    update_puzzle(puzzle)

    #Call the recursive solving function which takes guesses at cells and backtracks if needed.
    puzzle=recursive_guess(puzzle)

    #As long as their is a solution to the puzzle, we add its first three values to the result.
    if puzzle:
      #print_puzzle(puzzle)
      #print("".join((str(i) for i in puzzle[0][:3])))
      #input()
      
      result+=int("".join((str(i) for i in puzzle[0][:3])))

    #Catch the errors
    else:
      print("ERROR, NO SOLUTION FOUND FOR PUZZLE")
    
  return(result)


def p96alt():
  """Alternate solution.
  """
  pass


# Test cases
print(p96())
