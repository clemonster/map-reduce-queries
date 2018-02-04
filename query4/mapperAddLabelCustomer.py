#!/usr/bin/python
 
import sys
 
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    labelledLine = line + ',' + 'C'
    print('%s' % (labelledLine))