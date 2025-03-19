#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""main.py: controller for the personal Project Euler challenge set"""

__author__ = "John Petrzelka (petrzelk)"
__date__ = "1 August 2024"

import os
import re
import time


def main():
  """ Main program """
  # Uncomment the following to import problems.
  '''if input('Import problem? (Y/N)\n')=='Y':
    os.system("python import_problem.py")'''
  # Find most recently modified problem
  recently_modified=('p1.py',os.path.getmtime('problems/p1.py'))
  for file in os.listdir(f'{os.getcwd()}\\problems'):
    if re.match(r'p[0-9]*.py',file) and os.path.getmtime('problems/'+file)>recently_modified[1]:
      recently_modified=(file,os.path.getmtime('problems/'+file))
      #print(recently_modified)
  problem_number = recently_modified[0][1:-3]
  #print(problem_number)    # Debug
  #problem_number = 9       # Uncomment to specify a specific problem.
  start = time.time()
  os.system(f"py problems/p{problem_number}.py")
  end = time.time()
  print(
      f"Problem {problem_number} was executed in {round(end-start,2)} seconds."
  )
  return


if __name__ == "__main__":
  main()