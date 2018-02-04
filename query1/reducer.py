#!/usr/bin/python

import sys

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    date, name = line.split(',', 1)
    day, month, year = date.split('/')

    if month == '07':
    	print(name)