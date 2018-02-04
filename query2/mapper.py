#!/usr/bin/python


#SELECT DISTINCT name FROM Customer WHERE month(startDate)=7
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    if line is None:
        break
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words

    id, date, name = line.split(',', 2)
    day, month, year = date.split('/', 2)

    if month == '07':
    	print(name)

