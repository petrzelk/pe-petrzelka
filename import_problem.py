#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""import_problem.py: controller for the personal Project Euler challenge set"""

import os
import re
import urllib.request as urlreq

# Get problem number
problem = input('Import which project euler problem? \n')

# Validate number
while not isinstance(problem, int) or problem <= 0:
  try:
    problem = int(problem)
  except ValueError:
    print('ERROR: invalid input')
    problem = input('Import which project euler problem? \n')

# Check for file already existing.
if os.path.exists(f'problems/p{problem}.py') and input(
    'File already exists, continue and overwrite file? (Y/N) \n') != 'Y':
  exit()

# Get problem description
with urlreq.urlopen(
    f'https://projecteuler.net/minimal={str(problem)}') as page:
  description = page.read().decode('UTF-8')

# Get the title
with urlreq.urlopen(
    f'https://projecteuler.net/problem={str(problem)}') as page:
  full_page = page.read().decode('UTF-8')
title = full_page[full_page.find('<title>'):full_page.find('</title>')]
title = title[title.find(' ') + 1:-16]
#print(title) 

# Clean the discription.
to_clean = {
    '$': '',
    '\\dots': '...',
    '\\lt': '<',
    '\\le': '<=',
    '\\gt': '>',
    '\\ge': '>=',
    '^': '**',
    '\\times': '*',
    '\\mathbf': '',
    '&amp;': '',
    '\\colon': ':',
    '\\\\': '',
    '\\begin{align}': '',
    '\\end{align}': '',
    '\\displaystyle':'',
    '\\binom':'',
    '\\approx':'~',
    '\\%':'%',
    '\\,':',',
    '\\{':'{',
    '\\}':'}',
    '\\color{red}':'',
    '\\phi':'phi',
    '\\dfrac':'frac',
    '\\frac':'frac',
    '\\operatorname':'',
    '\\to':'->',
    '<ul style="list-style-type:none;">':'',
    '\\pu':'',
    '\\cdots':'...',
    '\\triangle':'triangle'
}
for to_replace in to_clean:
  #print(f'cleaned {to_replace} with {to_clean[to_replace]}')
  description = description.replace(to_replace, to_clean[to_replace])
# Regular expression to clean all '<...>'
description = re.sub(r'<[a-z|A-Z|/|=|"| ]+>', '', description)

#Format line length in the description
description_formated=''
while description:
  new_line=description.find('\n')
  if new_line < 88 and new_line!=1:
    description_formated=description_formated+description[:new_line+1]
    description=description[new_line+1:]
  else:
    space_location=description[88::-1].find(' ')
    description_formated=description_formated+description[:88-space_location]+'\n'
    description=description[89-space_location:]

# Pull the problem template.
with open('problem_template.py', 'r') as file:
  template = file.read()

# Replace the problem number and discription in the template
template = template.replace('NUM', str(problem))
template = template.replace('DISCRIPTION', description_formated)
template = template.replace('TITLE', title)
#print(template)

# Write the template
with open(f'problems/p{problem}.py', 'w') as file:
  file.write(template)
